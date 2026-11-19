# Quem Faz

Projeto acadêmico de demonstração para conectar pessoas a profissionais por categoria e permitir a publicação de solicitações de serviços.

Desenvolvido no contexto das disciplinas CitizenTech e Secure DevOps da FIAP.

## Links da entrega

- Repositório público: [Quem Faz no GitHub](https://github.com/guilhermebrazioli/quem-faz)
- Aplicação pública na Azure: [Acessar Quem Faz](https://quem-faz.whiteocean-1daba118.eastus.azurecontainerapps.io)
- Pipeline com falha: [Execução nº 2](https://github.com/guilhermebrazioli/quem-faz/actions/runs/43329604038)
- Pipeline aprovado: [Execução nº 5](https://github.com/guilhermebrazioli/quem-faz/actions/runs/43753163827)
- Evidências: PDF único entregue no portal da disciplina; as capturas não precisam ser publicadas no repositório.
- Dashboard exportado: `quem-faz-observabilidade.json`.

## Ficha técnica do MVP — Quem Faz

### 1. Nome do produto

**Quem Faz** — Plataforma de conexão entre contratantes e prestadores de serviços.

### 2. Cidadão e território

Moradores, empresas e profissionais prestadores de serviços da cidade de **São Paulo (SP)**.

### 3. Problema, em uma frase

A dificuldade de encontrar profissionais adequados e confiáveis para a contratação de serviços, enquanto prestadores enfrentam obstáculos para divulgar suas habilidades e conquistar novos clientes.

### 4. Proposta de valor

O Quem Faz propõe uma plataforma que aproxima contratantes e prestadores de serviços por meio da exploração de categorias profissionais e da publicação de solicitações. Os usuários poderão consultar perfis, solicitar propostas e avaliar experiências após a conclusão dos serviços.

No módulo de Secure DevOps, a proposta é publicar o MVP de forma segura e reproduzível: cada alteração passa por testes e verificações de segurança antes de chegar à nuvem, e a aplicação publicada é monitorada continuamente.

### 5. Arquitetura: componentes

- **Aplicação:** Python, FastAPI e Uvicorn, com SQLite para os dados de demonstração.
- **Container:** Docker com construção em múltiplos estágios e execução com usuário não root.
- **Nuvem:** Azure Container Apps (East US), com 0,25 vCPU, 0,5 GiB e de 0 a 1 réplica.
- **Entrega:** GitHub Actions com pytest, Gitleaks, Semgrep e Trivy; imagem aprovada publicada no Docker Hub e implantada com autenticação OIDC.
- **Infraestrutura como código:** Terraform, com os recursos existentes incorporados por importação.
- **Observabilidade:** Prometheus e Grafana locais coletando as métricas do MVP público via HTTPS.

**Fluxo de entrega:** GitHub → GitHub Actions (testes e segurança) → Docker Hub → Azure Container Apps → Prometheus e Grafana.

### 6. Fontes de dados

Dados exclusivamente fictícios, identificados como [DEMO]: profissionais, categorias e avaliações carregados na inicialização da aplicação. Nenhum dado pessoal real é armazenado.

### 7. Modelos de IA utilizados

Não se aplica a este módulo. A inteligência artificial do Quem Faz está nos módulos de Generative AI (assistente de contratação segura) e Maker Lab (Smart Point).

### 8. URL do MVP e repositório

- **MVP público:** https://quem-faz.whiteocean-1daba118.eastus.azurecontainerapps.io/
- **Repositório:** https://github.com/guilhermebrazioli/quem-faz

### 9. Indicadores de impacto

O pipeline impede a publicação de imagens com vulnerabilidades críticas, e os quatro sinais de ouro (tráfego, erros, latência e saturação) são monitorados, com regra de alerta no Grafana. O custo estimado é de até cerca de US$ 14 por mês com uma réplica ativa em tempo integral. **Esses indicadores são técnicos**: o impacto social da plataforma ainda não foi medido com usuários reais.

### 10. ODS conectados

**ODS 9 — Indústria, Inovação e Infraestrutura**

O Quem Faz contribui para esse objetivo ao propor uma solução tecnológica que digitaliza processos e facilita a conexão entre profissionais e contratantes. No módulo de Secure DevOps, a infraestrutura em nuvem, a entrega automatizada e o monitoramento contínuo sustentam essa solução de forma segura e escalável.

**ODS 10 — Redução das Desigualdades (Meta 10.2)**

O Quem Faz busca ampliar as oportunidades de trabalho e geração de renda para profissionais autônomos e informais, inclusive aqueles que atuam em bairros periféricos de São Paulo. A plataforma oferece um espaço para que esses profissionais divulguem suas habilidades, encontrem novos clientes e construam sua reputação por meio de avaliações vinculadas aos serviços realizados.

**ODS 11 — Cidades e Comunidades Sustentáveis**

O Quem Faz se conecta a esse objetivo ao propor melhorias no acesso a serviços locais na cidade de São Paulo, facilitando o encontro entre moradores, empresas e profissionais da própria comunidade.

As contribuições aos ODS representam os objetivos e benefícios potenciais da solução, ainda não resultados sociais comprovados em operação real.

## Escopo e dados de demonstração

A aplicação utiliza dados fictícios. Os nomes dos profissionais de demonstração estão identificados com `[DEMO]`.

Funcionalidades implementadas:

- Listagem de categorias de serviços.
- Consulta de profissionais por categoria.
- Consulta de detalhes e avaliações dos profissionais.
- Cadastro de avaliações.
- Publicação e listagem de solicitações de serviços.
- Documentação interativa da API.
- Verificação de saúde e exposição de métricas.

O escopo desta etapa concentra-se na implementação e demonstração técnica da proposta em ambiente acadêmico.

Utilizar somente dados fictícios nos campos livres de comentários, títulos ou descrições. O uso de dados identificados como `[DEMO]` integra os cuidados de tratamento de dados descritos neste documento.

## Tecnologias

- Python e FastAPI.
- Uvicorn.
- SQLite.
- Docker e Docker Compose.
- GitHub Actions.
- Docker Hub.
- Azure Container Apps.
- Terraform.
- Pytest, Gitleaks, Semgrep e Trivy.
- Prometheus e Grafana.

## Organização do repositório

- `app/main.py`: aplicação, acesso ao SQLite e instrumentação.
- `app/test_main.py`: testes automatizados.
- `app/requirements.txt`: dependências da aplicação.
- `app/requirements-dev.txt`: dependências para testes.
- `app/Dockerfile`: construção da imagem em múltiplos estágios.
- `docker-compose.yml`: execução local da aplicação.
- `docker-compose.monitoramento.yml`: serviços locais de monitoramento.
- `prometheus.yml`: configuração da coleta HTTPS do MVP publicado.
- `quem-faz-observabilidade.json`: dashboard exportado do Grafana.
- `alerta grafana.json`: exportação da regra de alerta; conferir o conteúdo antes de versionar.
- `.github/workflows/devsecops.yml`: workflow DevSecOps.
- `infra/providers.tf`: configuração de providers do Terraform.
- `infra/imports.tf`: declarações de importação de recursos.
- `infra/generated.tf`: configuração Terraform dos recursos incorporados.
- `infra/.terraform.lock.hcl`: versões e verificações de integridade dos providers.

As capturas de evidências são mantidas localmente para compor o PDF. Não fazem parte dos arquivos necessários à execução do projeto.

## Arquitetura da solução

A solução é composta pelos seguintes fluxos:

1. O usuário acessa o endereço público HTTPS do Azure Container Apps.
2. O ingresso encaminha as requisições para a aplicação FastAPI na porta interna `8000`.
3. A aplicação consulta e grava dados no SQLite, no caminho definido por `DB_PATH`, cujo padrão é `/app/data/quemfaz.db`.
4. O GitHub Actions executa testes, análise de segredos, análise estática, construção e análise de vulnerabilidades.
5. Quando as validações são aprovadas na branch `main`, o pipeline publica a imagem no Docker Hub e atualiza o Container App.
6. O deploy autentica na Azure por OIDC e direciona o tráfego para a revisão mais recente.
7. O Prometheus local coleta `/metrics` do endereço público por HTTPS.
8. O Grafana local consulta o Prometheus e apresenta o dashboard e a regra de alerta.
9. A configuração do ambiente Container Apps referencia um Log Analytics Workspace.

O Terraform gerencia a configuração da infraestrutura adotada por importação. O pipeline gerencia a versão da imagem implantada.

A descrição da arquitetura e dos fluxos compõe o PDF de entrega.

## Execução local da aplicação

Pré-requisitos:

- Git.
- Docker com Docker Compose.

Procedimento:

1. Clone o repositório e abra a pasta principal.
2. Inicie o Docker.
3. Execute `docker compose up -d --build`.
4. Acesse a aplicação no navegador usando o host local `127.0.0.1` e a porta `8000`, salvo alteração de `APP_PORT`.

Rotas disponíveis:

- `/`: página inicial.
- `/docs`: documentação interativa da API.
- `/health`: verificação de saúde, incluindo consulta ao banco.
- `/metrics`: métricas em formato compatível com Prometheus.
- `/api/categorias`: consulta de categorias.
- `/api/solicitacoes`: consulta e publicação de solicitações.

As demais operações estão descritas em `/docs`.

A porta local da aplicação pode ser ajustada pela variável `APP_PORT`. O Compose original publica essa porta nas interfaces disponíveis do host; para uso exclusivamente local, recomenda-se restringir a publicação ao endereço de loopback.

### Armazenamento nos ambientes

O serviço local da aplicação utiliza o volume nomeado `dados`, montado em `/app/data`.

O banco SQLite é inicializado no início da aplicação. Os dados iniciais de demonstração são inseridos quando a tabela de categorias está vazia.

Não execute comandos de remoção de volumes sem avaliar a perda dos dados locais.

Na implantação Azure apresentada, o banco permanece no ambiente de execução do container, sem volume persistente explicitamente configurado nos arquivos Terraform. Os registros da demonstração pública são descartáveis e podem ser reinicializados após a substituição de réplicas ou revisões.

## Testes automatizados

Com Python e um ambiente virtual ativado:

1. Na raiz do projeto, execute `python -m pip install -r app/requirements-dev.txt`.
2. Entre na pasta `app`.
3. Execute `python -m pytest -v`.

O workflow também executa os testes e produz um relatório JUnit.

## Segurança do container

Medidas presentes na configuração:

- Construção em múltiplos estágios.
- Execução da aplicação com usuário sem privilégios, UID `10001`.
- Atualização dos pacotes do sistema durante a construção da imagem.
- Healthcheck HTTP na rota `/health`.
- Sistema de arquivos somente leitura no Compose.
- Diretórios temporários separados com `tmpfs`.
- Remoção de todas as capacidades Linux no Compose.
- Bloqueio de novos privilégios no Compose.
- Banco local armazenado em volume separado.

Essas medidas integram a estratégia de defesa em profundidade, em conjunto com as verificações automatizadas e a política de tratamento de vulnerabilidades.

As restrições de filesystem, capacidades Linux e novos privilégios descritas para o Docker Compose correspondem à configuração do ambiente local. A configuração do ambiente Azure é documentada separadamente nos arquivos Terraform.

## Pipeline DevSecOps

O workflow está em `.github/workflows/devsecops.yml`.

O fluxo implementado inclui:

1. Obtenção do código e histórico.
2. Busca de segredos com Gitleaks.
3. Instalação das dependências e execução de testes.
4. Análise estática com Semgrep.
5. Construção da imagem da aplicação para Linux AMD64.
6. Relatório completo de vulnerabilidades HIGH e CRITICAL com Trivy.
7. Bloqueio de qualquer CRITICAL.
8. Bloqueio de HIGH com correção disponível.
9. Publicação da imagem aprovada no Docker Hub.
10. Atualização da aplicação no Azure Container Apps.
11. Direcionamento de tráfego para a revisão mais recente.
12. Disponibilização dos relatórios como artefatos.

### Gatilhos e condições de deploy

- A validação executa em todo `push`.
- Também executa em `pull_request` destinado à branch `main`.
- É possível iniciar o workflow manualmente.
- A publicação da imagem e o deploy exigem sucesso das validações.
- A publicação e o deploy executam apenas na branch `main`, em eventos de `push` ou execução manual.
- O job de deploy depende do job de validação.

A etapa final exibe o endereço público. A verificação HTTP de saúde após o deploy é realizada separadamente do workflow.

### Evidências de bloqueio e aprovação

- Execução nº 2, commit `9796158`: falha na etapa de análise de vulnerabilidades com Trivy.
- Execução nº 5, commit `3af9f56`: validação e deploy concluídos com sucesso.

Os links estão na seção de entrega. Os prints e os relatórios correspondentes compõem as evidências do PDF.

A execução aprovada atendeu à política de vulnerabilidades documentada, que contempla aceitação temporária de achados HIGH sem correção informada.

### Credenciais

Foram configurados os seguintes GitHub Secrets:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `AZURE_CLIENT_ID`
- `AZURE_TENANT_ID`
- `AZURE_SUBSCRIPTION_ID`

A autenticação de implantação na Azure utiliza identidade federada com OIDC.

Não versionar tokens, senhas, arquivos `.env`, estados Terraform ou arquivos de variáveis que contenham valores sensíveis.

Os relatórios do workflow possuem retenção configurada de 14 dias. As evidências necessárias à entrega devem ser preservadas antes da expiração.

## Infraestrutura na Azure e Terraform

Recursos utilizados:

- Resource Group: `rg-quem-faz`.
- Azure Container App: `quem-faz`.
- Ambiente do Azure Container Apps: `env-quem-faz`.
- Log Analytics Workspace: `workspace-rgquemfazArrv`.
- Região configurada: `eastus`.

Os arquivos Terraform estão na pasta `infra/`.

### Adoção dos recursos existentes

A infraestrutura Azure foi incorporada ao gerenciamento do Terraform por importação dos recursos existentes.

A configuração foi validada com `terraform validate`. Após separar a responsabilidade pela imagem, o plano apresentou:

`No changes. Your infrastructure matches the configuration.`

A validação e o plano sem mudanças registram o alinhamento dos atributos gerenciados com a configuração declarada. A abordagem adotada neste projeto foi incorporar recursos existentes ao Terraform por importação.

### Separação de responsabilidades

- Terraform: configuração da infraestrutura.
- Pipeline DevSecOps: versão da imagem implantada.
- O atributo `template[0].container[0].image` está em `ignore_changes` no recurso do Container App.

Isso evita que um plano de infraestrutura reverta a imagem aplicada pelo pipeline.

A imagem declarada no Terraform continua sendo considerada numa criação inicial. Antes de provisionar um novo ambiente, é necessário revisar essa referência e utilizar uma imagem aprovada.

### Validação

A partir da raiz do projeto:

1. Autentique-se na Azure com uma identidade autorizada.
2. Selecione a assinatura correta e configure a autenticação exigida pelo provider.
3. Para uma nova cópia do repositório, execute `terraform -chdir=infra init`.
4. Execute `terraform -chdir=infra validate`.
5. Execute `terraform -chdir=infra plan`.
6. Revise todas as ações antes de considerar um `apply`.

As versões observadas na validação foram Terraform `1.17.2` e provider AzureRM `5.13.0`. O arquivo de lock está versionado.

Não executar `apply` ou `destroy` sem revisar o plano, o estado utilizado e os impactos sobre a aplicação pública.

Arquivos de estado e planos Terraform podem conter informações sensíveis e não devem ser publicados.

## Observabilidade do MVP publicado

Prometheus e Grafana executam localmente. A aplicação observada é o MVP publicado na Azure, e não o serviço local `app:8000`.

A aplicação expõe métricas em `/metrics` utilizando `prometheus-fastapi-instrumentator`.

O Prometheus coleta o destino `quem-faz.whiteocean-1daba118.eastus.azurecontainerapps.io:443` por HTTPS:

- Caminho: `/metrics`.
- Intervalo de coleta: cinco segundos.
- Timeout de coleta: quatro segundos.
- Job: `quem-faz`.
- Validação TLS não desabilitada.

O Grafana consulta o serviço Prometheus pela rede interna do Compose.

### Inicialização

1. Defina `GRAFANA_ADMIN_PASSWORD` na sessão do terminal com uma senha forte.
2. Não grave a senha no repositório.
3. Execute `docker compose -f docker-compose.yml -f docker-compose.monitoramento.yml up -d --build`.
4. Confirme que a aplicação pública está disponível.
5. No Prometheus, confira que o destino público aparece como `UP`.

Interfaces locais:

- Prometheus: host `127.0.0.1`, porta `9090`.
- Grafana: host `127.0.0.1`, porta `3000`.

As portas dos serviços de monitoramento são publicadas apenas no endereço de loopback.

O usuário administrador inicial do Grafana é `admin`. A senha vem da variável de ambiente.

A inicialização conjunta também sobe a aplicação local, mas o destino de coleta definido em `prometheus.yml` é a aplicação pública.

### Configuração do dashboard

1. Adicione uma fonte de dados do tipo Prometheus.
2. Configure o servidor como `http://prometheus:9090`.
3. Execute `Save & test`.
4. Importe `quem-faz-observabilidade.json` pela área de dashboards.
5. Se solicitado, selecione a fonte de dados Prometheus configurada.

O JSON exportado preserva a definição do dashboard. O histórico das métricas e as demais configurações do Grafana são armazenados separadamente.

### Painéis validados

- Coleta da aplicação: sucesso da última coleta, com `1 = OK`.
- Tráfego: taxa de requisições por segundo.
- Erros HTTP 5xx: percentual de respostas de erro do servidor.
- Latência p95: estimativa do percentil 95 do tempo de resposta.
- Saturação de descritores: percentual do limite de descritores de arquivo utilizado pelo processo.

O dashboard apresenta as quatro métricas de ouro e um indicador adicional de sucesso da coleta.

A medida de saturação utiliza a expressão:

`100 * process_open_fds{job="quem-faz"} / process_max_fds{job="quem-faz"}`

O indicador de saturação adotado mede o percentual de utilização do limite de descritores de arquivo do processo.

A validação funcional do monitoramento utilizou requisições de demonstração contra a aplicação pública.

Ausência de tráfego pode produzir taxa zero e deixar painéis baseados em divisão ou percentis sem valor.

### Alerta de demonstração

Foi criada e validada a regra:

`[DEMO] Quem Faz — tráfego acima do limite de teste`

Configuração utilizada na demonstração:

- Consulta: `sum(rate(http_requests_total{job="quem-faz"}[1m]))`.
- Condição: resultado acima de `0.2` requisição por segundo.
- Período pendente configurado para o teste: 30 segundos.
- Geração de tráfego por consultas de leitura à API pública.
- Avaliação da condição em `Firing` registrada na captura, com cabeçalho da regra em `Pending` no momento apresentado.
- Captura da avaliação preservada para o PDF.

O limite foi reduzido exclusivamente para demonstrar o funcionamento do alerta. Não representa capacidade máxima, degradação do serviço ou incidente real.

A demonstração abrange a avaliação da condição de alerta no Grafana; a entrega de notificações externas permanece como evolução operacional.

A regra foi exportada para `alerta grafana.json`. O arquivo deve ser revisado antes de sua publicação e importado ou provisionado separadamente do dashboard, conforme as opções compatíveis da versão do Grafana.

### Configuração e cuidados operacionais

- Prometheus e Grafana executam com UID `10001`.
- O sistema de arquivos principal permanece somente leitura.
- O armazenamento do monitoramento utiliza `tmpfs` e é temporário.
- Parar ou recriar os containers pode apagar métricas, usuários, fontes de dados, dashboards e regras configuradas.
- Exporte o dashboard e a regra de alerta antes de interromper o ambiente.
- A pasta de plugins do Grafana possui uma montagem específica com execução permitida, necessária para os plugins de backend baixados.
- A verificação de assinaturas dos plugins não foi desativada.
- As imagens de monitoramento utilizam a tag móvel `latest`; a reprodução de versões específicas depende da fixação de tags ou digests validados.
- A coleta depende do computador local, dos containers de monitoramento, da conexão com a internet e da disponibilidade do MVP.
- O intervalo de cinco segundos aumenta o número de requisições à aplicação pública e pode mantê-la ativa, afetando o consumo.
- O endpoint de métricas está publicamente acessível no ambiente demonstrado; seu conteúdo não deve conter dados pessoais, credenciais ou valores fornecidos livremente por usuários como labels.

## Dados, localização e LGPD

### Dados da aplicação

Os dados de negócio ficam no SQLite acessado pela aplicação.

- Localmente: volume Docker `dados`, montado em `/app/data`.
- Na Azure: arquivo no ambiente de execução da aplicação, sem volume persistente explicitamente configurado nos arquivos Terraform apresentados.
- Região dos recursos Azure declarados: East US, nos Estados Unidos.

A região declarada identifica a implantação dos recursos Azure. A localização de dados operacionais, backups e metadados também depende das condições dos serviços utilizados.

### Campos livres e exposição pública

Avaliações e solicitações aceitam texto livre. A orientação de uso exclusivamente fictício não impede tecnicamente que alguém envie dados pessoais.

As operações demonstradas não implementam autenticação de usuários na aplicação. Conteúdos enviados podem ser consultados pelas rotas públicas.

Não inserir nomes reais, telefones, endereços, documentos, e-mails ou outras informações pessoais.

Para uma evolução destinada a usuários reais, deverão ser definidos controles de autenticação, autorização, prevenção de abuso, retenção, exclusão e atendimento aos direitos dos titulares.

### Logs e métricas

Logs operacionais e registros de acesso podem conter metadados, como horários, caminhos e endereços IP, dependendo da configuração dos serviços.

O ambiente Container Apps está associado ao Log Analytics Workspace, cuja retenção declarada no Terraform é de 30 dias. As categorias efetivamente enviadas dependem da configuração de coleta dos serviços.

As métricas coletadas ficam no armazenamento temporário do Prometheus local. Não devem incorporar conteúdo pessoal dos campos livres.

### Evidências acadêmicas

Antes de inserir capturas no PDF:

- Ocultar credenciais e tokens.
- Remover dados pessoais que não sejam necessários à avaliação.
- Evitar exposição de telas de faturamento ou identificadores pessoais desnecessários.
- Manter somente o conteúdo suficiente para demonstrar o requisito.
- Entregar as evidências pelo portal da disciplina.

O uso de dados fictícios, a localização documentada e os cuidados com as capturas integram as medidas de redução de risco do MVP. Uma evolução para tratamento de dados pessoais reais exige avaliação específica dos requisitos aplicáveis da LGPD.

## Responsabilidade compartilhada

| Parte | Responsabilidades no contexto do projeto |
|---|---|
| Microsoft Azure | Infraestrutura física e camadas gerenciadas do serviço, conforme o modelo e os termos do Azure Container Apps |
| Equipe do projeto | Código, dependências, imagem, dados inseridos, configuração dos recursos, permissões, segredos, políticas de segurança e controle de custos |
| Equipe do projeto | Revisão dos achados de segurança, tratamento das vulnerabilidades e cumprimento do prazo da exceção de risco |
| Equipe do projeto | Disponibilidade do monitoramento local, preservação das exportações e análise dos alertas |
| GitHub e Docker Hub | Operação dos respectivos serviços hospedados, conforme seus termos |
| Equipe do projeto | Segurança das contas, permissões do workflow, credenciais de publicação e conteúdo dos repositórios e imagens |

O modelo de responsabilidade compartilhada mantém sob gestão da equipe o conteúdo da aplicação, os dados inseridos e as decisões de configuração, enquanto os provedores operam as camadas abrangidas pelos respectivos serviços.

## Custos e controle de consumo

### Recursos considerados

A estimativa da solução deve considerar:

- Azure Container Apps em perfil Consumption.
- CPU e memória das réplicas em execução.
- Requisições e regras de cobrança aplicáveis.
- Ingestão e retenção de logs no Log Analytics.
- Transferência de dados, quando aplicável.
- Outros recursos efetivamente presentes na assinatura.

A configuração declara 0,25 vCPU e 0,5 GiB por réplica, mínimo de zero e máximo de uma réplica por revisão.

O modo de revisões é `Multiple`. O dimensionamento total depende da quantidade de revisões ativas e das réplicas em execução em cada uma.

Prometheus e Grafana executam no computador local, sem recursos Azure dedicados a esses serviços na arquitetura apresentada.

### Estimativa de custos — cenário acadêmico

Estimativa de referência elaborada em 18/11/2026, em dólares americanos
(USD), para Azure Container Apps no plano Consumption, região East US.

#### Premissas

- Período simulado: 30 dias, equivalentes a 720 horas.
- Uma única réplica em execução no total, com 0,25 vCPU e 0,5 GiB de memória.
- Cenário conservador: réplica cobrada na tarifa ativa durante todo o período.
- A configuração permite escala a zero; disponibilidade da URL não significa necessariamente processamento e cobrança contínuos.
- Os valores são uma simulação, não uma medição do consumo nem uma previsão da fatura da assinatura.

#### Tarifas de referência

| Componente | Tarifa utilizada |
|---|---|
| CPU ativa | US$ 0,000024 por vCPU-segundo |
| Memória | US$ 0,000003 por GiB-segundo |
| Requisições excedentes à franquia | US$ 0,40 por milhão |

As tarifas unitárias foram consultadas no levantamento da DevZero para
East US, atualizado em 17/11/2026. Essa é uma fonte secundária que informa
utilizar a Azure Retail Prices API; não constitui cotação personalizada
da Microsoft.

#### Resultado da simulação de computação

| Item | Consumo em 30 dias | Custo sem franquias |
|---|---|---|
| CPU | 648.000 vCPU-segundos | US$ 15,55 |
| Memória | 1.296.000 GiB-segundos | US$ 3,89 |
| Total de computação | — | **US$ 19,44** |

A Microsoft informa franquias mensais por assinatura de 180.000
vCPU-segundos, 360.000 GiB-segundos e 2 milhões de requisições.

Descontando uma franquia mensal integral de CPU e memória, totalmente
disponível para este projeto, o total ilustrativo de computação seria
**US$ 14,04**.

A franquia é compartilhada pela assinatura. O período de avaliação pode
atravessar meses, portanto esse desconto simplificado não reproduz
exatamente o faturamento por mês-calendário.

#### Abrangência da estimativa

- Os totais acima incluem somente CPU e memória.
- Requisições dependem do volume efetivo e da franquia disponível.
- Ingestão e eventual retenção faturável de logs no Log Analytics, transferência de dados, impostos e outros recursos não estão quantificados nem incluídos nesses totais.
- A simulação utiliza tarifas de referência; o custo real depende do consumo registrado e das condições da assinatura.
- Prometheus e Grafana executam localmente, sem recursos Azure dedicados a esses serviços; custos do computador e da conexão não foram estimados.
- O modo `Multiple` permite várias revisões ativas. A simulação considera apenas uma réplica no total; mais réplicas podem elevar o custo.
- A coleta a cada cinco segundos pode manter a aplicação ativa.
- A interrupção do aplicativo reduz seu consumo de execução; eventuais custos de outros recursos devem ser acompanhados separadamente.

Assim, a referência para 30 dias de computação continuamente ativa é
**US$ 19,44 antes das franquias**, ou **US$ 14,04 no exemplo com uma
franquia integral disponível**, acrescida dos componentes não incluídos.
Com escala a zero e uso ocasional, o consumo de computação pode ser menor.

#### Fontes

- [Microsoft Azure — regras de cobrança e franquias do Container Apps](https://azure.microsoft.com/pt-br/pricing/details/container-apps/) — consultado em 18/11/2026.
- [DevZero — tarifas de referência para East US](https://www.devzero.io/blog/azure-container-apps-pricing) — consultado em 18/11/2026.

## Evidências e entrega

A entrega reúne o repositório público, o endereço da aplicação e um PDF único com as evidências.

Conteúdo previsto para o PDF:

- Arquitetura da solução.
- Funcionalidades do MVP com dados fictícios `[DEMO]`.
- Segurança do container.
- Pipeline com bloqueio e execução aprovada.
- Infraestrutura gerenciada pelo Terraform por importação.
- Dashboard de observabilidade e avaliação da condição de alerta em `Firing`.
- Estimativa de custos, premissas e fontes.
- Escopo acadêmico, cuidados com dados e links da entrega.

As capturas são mantidas localmente e não precisam ser publicadas no GitHub.

### Reprodução do monitoramento

O dashboard e a regra de alerta exportados referenciam a fonte Prometheus com UID `eg4en712jz8cge`. Em outro ambiente, é necessário configurar esse UID ou ajustar as referências dos arquivos para a fonte criada.

A regra referencia também o receiver `empty`. Para habilitar notificações externas em outro ambiente, é necessário configurar o destino e associá-lo à política de notificações; essa configuração não está incluída na exportação apresentada.

### Disponibilidade e validade da exceção

A disponibilidade da aplicação deve contemplar o período de entrega e correção acadêmica.

A exceção de risco abaixo possui prazo próprio, independente da consulta às evidências ou do acionamento do pipeline. Sua validade original é até 19/11/2026 às 23h55, horário de Brasília. A continuidade da operação após essa data requer revisão dos achados e decisão documentada do responsável, sem renovação automática.

### Política de vulnerabilidades da imagem

O pipeline utiliza Trivy para analisar vulnerabilidades dos pacotes
do sistema operacional e das dependências da imagem.

Critérios de bloqueio:

- Qualquer vulnerabilidade CRITICAL, com ou sem correção informada.
- Vulnerabilidades HIGH com versão corrigida informada pelo Trivy.

Vulnerabilidades HIGH sem correção informada não bloqueiam
automaticamente o pipeline durante a exceção temporária abaixo.
Elas permanecem visíveis no relatório de evidências.

#### Exceção temporária de risco — entrega acadêmica

- Responsável: mantenedor do projeto Quem Faz.
- Escopo: achados HIGH sem versão corrigida informada pelo Trivy.
- Referência inicial: imagem `quem-faz:979615869dc086f6ead2e227148511c66dd7fbe3`.
- Situação no relatório analisado: 47 ocorrências HIGH e nenhuma CRITICAL.
- Origem dos achados apresentados: pacotes do Debian da imagem.
- Justificativa: o relatório não informa versões corrigidas para esses achados; a atualização dos pacotes não eliminou as ocorrências.
- Decisão: aceitação temporária de risco para a demonstração acadêmica.
- Validade: até 19/11/2026 às 23h55, horário de Brasília, sem renovação automática da aceitação de risco.
- Revisão: a cada execução do pipeline e antes da entrega.
- Tratamento: aplicar atualizações quando disponíveis ou avaliar substituição da imagem-base, seguida de testes e nova análise.
- Restrição: utilizar somente dados fictícios identificados como `[DEMO]`, sem coleta de dados pessoais reais.

Referências dos achados no relatório inicial:

- util-linux e pacotes relacionados: CVE-2026-76642, CVE-2026-78408, CVE-2026-78409 e CVE-2026-78410.
- acl: CVE-2026-54369.
- ncurses: CVE-2025-69720.
- sqlite: CVE-2026-119373, CVE-2026-119374 e CVE-2026-119379.
- systemd e pacotes relacionados: CVE-2026-16742.
- perl: CVE-2026-9538.

A execução como usuário sem privilégios, UID `10001`, integra a defesa em profundidade. O tratamento dos achados permanece vinculado à política de vulnerabilidades, sem pressupor sua correção ou ausência de explorabilidade.

Os relatórios ficam no artefato `relatorios-devsecops`:

- `trivy.txt`: todos os achados HIGH e CRITICAL.
- `trivy-critical.txt`: resultado do controle de CRITICAL.
- `trivy-high-fixed.txt`: resultado do controle de HIGH com correção.

A aprovação do pipeline representa o atendimento aos critérios definidos nesta política.
