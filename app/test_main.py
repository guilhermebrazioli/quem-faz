import os
import tempfile

os.environ["DB_PATH"] = os.path.join(tempfile.mkdtemp(), "teste.db")

from fastapi.testclient import TestClient  # noqa: E402

from main import app  # noqa: E402


def test_fluxo_principal():
    with TestClient(app) as client:
        assert client.get("/health").json() == {"status": "ok"}

        categorias = client.get("/api/categorias").json()
        assert len(categorias) == 5
        categoria_id = categorias[0]["id"]

        profissionais = client.get(f"/api/categorias/{categoria_id}/profissionais").json()
        assert profissionais

        resposta = client.post(
            "/api/solicitacoes",
            json={"categoria_id": categoria_id, "titulo": "Trocar chuveiro", "descricao": "Chuveiro queimado, preciso trocar."},
        )
        assert resposta.status_code == 201

        resposta = client.post(f"/api/profissionais/{profissionais[0]['id']}/avaliacoes", json={"nota": 5})
        assert resposta.status_code == 201


def test_validacoes():
    with TestClient(app) as client:
        assert client.post("/api/profissionais/1/avaliacoes", json={"nota": 9}).status_code == 422
        assert client.get("/api/categorias/999/profissionais").status_code == 404
        assert client.get("/metrics").status_code == 200
