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
- Referência inicial: imagem quem-faz:979615869dc086f6ead2e227148511c66dd7fbe3.
- Situação no relatório analisado: 47 ocorrências HIGH e nenhuma CRITICAL.
- Origem dos achados apresentados: pacotes do Debian da imagem.
- Justificativa: o relatório não informa versões corrigidas para
  esses achados; a atualização dos pacotes não eliminou as ocorrências.
- Decisão: aceitação temporária de risco para a demonstração acadêmica.
- Validade: até 19/11/2026 às 23:55, horário de Brasília, sem
  renovação automática da aceitação de risco.
- Revisão: a cada execução do pipeline e antes da entrega.
- Tratamento: aplicar atualizações quando disponíveis ou avaliar
  substituição da imagem-base, seguida de testes e nova análise.
- Restrição: utilizar somente dados fictícios identificados como [DEMO],
  sem coleta de dados pessoais reais.

Referências dos achados no relatório inicial:
- util-linux e pacotes relacionados: CVE-2026-76642,
  CVE-2026-78408, CVE-2026-78409 e CVE-2026-78410.
- acl: CVE-2026-54369.
- ncurses: CVE-2025-69720.
- sqlite: CVE-2026-119373, CVE-2026-119374 e CVE-2026-119379.
- systemd e pacotes relacionados: CVE-2026-16742.
- perl: CVE-2026-9538.

A execução como usuário sem privilégios (UID 10001) é uma medida
de defesa em profundidade, não uma correção dessas vulnerabilidades.
Não foi comprovada a ausência de explorabilidade dos achados.

Os relatórios ficam no artefato relatorios-devsecops:
- trivy.txt: todos os achados HIGH e CRITICAL.
- trivy-critical.txt: resultado do controle de CRITICAL.
- trivy-high-fixed.txt: resultado do controle de HIGH com correção.

Pipeline aprovado significa conformidade com esta política,
não ausência de vulnerabilidades.
