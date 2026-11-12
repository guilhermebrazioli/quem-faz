import html
import os
import sqlite3
from contextlib import asynccontextmanager, closing

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel, Field

DB_PATH = os.getenv("DB_PATH", "/app/data/quemfaz.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS profissionais (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    categoria_id INTEGER NOT NULL REFERENCES categorias(id)
);
CREATE TABLE IF NOT EXISTS avaliacoes (
    id INTEGER PRIMARY KEY,
    profissional_id INTEGER NOT NULL REFERENCES profissionais(id),
    nota INTEGER NOT NULL CHECK (nota BETWEEN 1 AND 5),
    comentario TEXT,
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS solicitacoes (
    id INTEGER PRIMARY KEY,
    categoria_id INTEGER NOT NULL REFERENCES categorias(id),
    titulo TEXT NOT NULL,
    descricao TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'aberta',
    criado_em TEXT DEFAULT CURRENT_TIMESTAMP
);
"""

# Dados fictícios, identificados como [DEMO] (nenhum dado pessoal real)
CATEGORIAS = ["Elétrica", "Hidráulica", "Limpeza", "Montagem de móveis", "Pintura"]
PROFISSIONAIS = [
    ("[DEMO] Ana Souza", "Instalações e reparos elétricos residenciais", 1),
    ("[DEMO] Bruno Lima", "Troca de disjuntores e quadros de energia", 1),
    ("[DEMO] Carla Dias", "Vazamentos, torneiras e caixas d'água", 2),
    ("[DEMO] Diego Alves", "Limpeza residencial e pós-obra", 3),
    ("[DEMO] Elisa Rocha", "Montagem de móveis planejados e modulares", 4),
    ("[DEMO] Fábio Nunes", "Pintura interna e externa", 5),
]
AVALIACOES = [
    (1, 5, "Pontual e caprichosa"), (1, 4, None), (2, 4, "Resolveu rápido"),
    (3, 5, None), (4, 3, "Bom, mas atrasou"), (5, 5, None), (6, 4, None),
]

SQL_PROFISSIONAIS = """
SELECT p.id, p.nome, p.descricao, c.nome AS categoria,
       ROUND(AVG(a.nota), 1) AS media, COUNT(a.id) AS total_avaliacoes
FROM profissionais p
JOIN categorias c ON c.id = p.categoria_id
LEFT JOIN avaliacoes a ON a.profissional_id = p.id
"""


def conectar():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def consultar(sql, params=()):
    with closing(conectar()) as conn:
        return [dict(linha) for linha in conn.execute(sql, params).fetchall()]


def executar(sql, params=()):
    with closing(conectar()) as conn:
        with conn:
            return conn.execute(sql, params).lastrowid


def obter_ou_404(sql, params, mensagem):
    linhas = consultar(sql, params)
    if not linhas:
        raise HTTPException(status_code=404, detail=mensagem)
    return linhas[0]


def inicializar_banco():
    pasta = os.path.dirname(DB_PATH)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with closing(conectar()) as conn:
        conn.executescript(SCHEMA)
        with conn:
            if conn.execute("SELECT COUNT(*) FROM categorias").fetchone()[0] == 0:
                conn.executemany("INSERT INTO categorias (nome) VALUES (?)", [(c,) for c in CATEGORIAS])
                conn.executemany(
                    "INSERT INTO profissionais (nome, descricao, categoria_id) VALUES (?, ?, ?)", PROFISSIONAIS
                )
                conn.executemany(
                    "INSERT INTO avaliacoes (profissional_id, nota, comentario) VALUES (?, ?, ?)", AVALIACOES
                )


@asynccontextmanager
async def lifespan(_app):
    inicializar_banco()
    yield


app = FastAPI(title="Quem Faz", version="0.1.0", lifespan=lifespan)

# Métricas de requisições (latência, tráfego e erros) + métricas do processo (saturação) em /metrics
Instrumentator(excluded_handlers=["/metrics", "/health"]).instrument(app).expose(app, include_in_schema=False)


class SolicitacaoIn(BaseModel):
    categoria_id: int
    titulo: str = Field(min_length=5, max_length=100)
    descricao: str = Field(min_length=10, max_length=1000)


class AvaliacaoIn(BaseModel):
    nota: int = Field(ge=1, le=5)
    comentario: str | None = Field(default=None, max_length=500)


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def inicio():
    profissionais = consultar(SQL_PROFISSIONAIS + " GROUP BY p.id ORDER BY c.nome, media DESC")
    itens = "".join(
        f"<li><strong>{html.escape(p['nome'])}</strong> — {html.escape(p['categoria'])}: "
        f"{html.escape(p['descricao'])} · nota {p['media'] or '-'} ({p['total_avaliacoes']} avaliações)</li>"
        for p in profissionais
    )
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Quem Faz</title></head>
<body style="font-family:sans-serif;max-width:760px;margin:2rem auto;line-height:1.5">
<h1>Quem Faz</h1>
<p>Encontre profissionais por categoria ou publique o serviço de que você precisa.</p>
<p><em>Ambiente de demonstração acadêmica: todos os dados são fictícios.</em></p>
<h2>Profissionais</h2><ul>{itens}</ul>
<p><a href="/docs">API interativa</a>: publicar solicitações e avaliar profissionais.</p>
</body></html>"""


@app.get("/health")
def health():
    consultar("SELECT 1")
    return {"status": "ok"}


@app.get("/api/categorias")
def listar_categorias():
    return consultar("SELECT id, nome FROM categorias ORDER BY nome")


@app.get("/api/categorias/{categoria_id}/profissionais")
def listar_profissionais(categoria_id: int):
    obter_ou_404("SELECT id FROM categorias WHERE id = ?", (categoria_id,), "Categoria não encontrada")
    return consultar(SQL_PROFISSIONAIS + " WHERE p.categoria_id = ? GROUP BY p.id ORDER BY media DESC", (categoria_id,))


@app.get("/api/profissionais/{profissional_id}")
def detalhar_profissional(profissional_id: int):
    profissional = obter_ou_404(
        SQL_PROFISSIONAIS + " WHERE p.id = ? GROUP BY p.id", (profissional_id,), "Profissional não encontrado"
    )
    profissional["avaliacoes"] = consultar(
        "SELECT nota, comentario, criado_em FROM avaliacoes WHERE profissional_id = ? ORDER BY id DESC",
        (profissional_id,),
    )
    return profissional


@app.post("/api/profissionais/{profissional_id}/avaliacoes", status_code=201)
def avaliar_profissional(profissional_id: int, avaliacao: AvaliacaoIn):
    obter_ou_404("SELECT id FROM profissionais WHERE id = ?", (profissional_id,), "Profissional não encontrado")
    novo_id = executar(
        "INSERT INTO avaliacoes (profissional_id, nota, comentario) VALUES (?, ?, ?)",
        (profissional_id, avaliacao.nota, avaliacao.comentario),
    )
    return {"id": novo_id, "profissional_id": profissional_id, **avaliacao.model_dump()}


@app.get("/api/solicitacoes")
def listar_solicitacoes():
    return consultar(
        "SELECT s.id, c.nome AS categoria, s.titulo, s.descricao, s.status, s.criado_em "
        "FROM solicitacoes s JOIN categorias c ON c.id = s.categoria_id ORDER BY s.id DESC"
    )


@app.post("/api/solicitacoes", status_code=201)
def publicar_solicitacao(solicitacao: SolicitacaoIn):
    obter_ou_404("SELECT id FROM categorias WHERE id = ?", (solicitacao.categoria_id,), "Categoria não encontrada")
    novo_id = executar(
        "INSERT INTO solicitacoes (categoria_id, titulo, descricao) VALUES (?, ?, ?)",
        (solicitacao.categoria_id, solicitacao.titulo, solicitacao.descricao),
    )
    return {"id": novo_id, "status": "aberta", **solicitacao.model_dump()}
