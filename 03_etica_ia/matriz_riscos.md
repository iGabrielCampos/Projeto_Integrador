---
id: matriz-riscos-eticos-ia
etapa: 3
autor: Gabriel Amancio, Gustavo Antonio, Paulo Germano, Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F002
  - F007
  - F050
  - F051
---

# Matriz de Riscos Éticos, Regulatórios e de Inteligência Artificial

Esta matriz cataloga os riscos tecnológicos, éticos, regulatórios e socioambientais no ciclo de vida de soluções digitais e no uso de Inteligência Artificial, detalhando causas-raiz, potenciais consequências e medidas preventivas de mitigação.

---

## 1. Tabela Geral de Riscos Mapeados (Mínimo de 8 Riscos)

| ID | Risco Identificado | Descrição do Risco | Causa Potencial | Consequência Provável | Prob. | Impacto | Nível | Medida de Mitigação | Responsável |
|---|---|---|---|---|---|---|---|---|---|
| **RSK-E01** | **Viés Algorítmico e Discriminação Indireta** | O sistema de software ou modelo de IA reproduz ou amplia disparidades históricas contra grupos vulneráveis `[F050]`. | Dados de treino históricos desbalanceados, ausência de testes de equidade e métricas enviesadas. | Exclusão de usuários, decisões automatizadas discriminatórias e danos morais coletivos. | Média | **Crítico** | **Crítico** | Auditoria de paridade estatística, uso de datasets representativos e supervisão humana obrigatória (*Human-in-the-Loop*). | Paulo Germano (Dados/IA) |
| **RSK-E02** | **Vazamento de Dados Pessoais e Não Conformidade com a LGPD** | Exposição indevida ou acesso não autorizado a dados pessoais ou sensíveis de cidadãos sob custódia da aplicação `[F001]`. | Falhas em controles de acesso e endpoints desprotegidos. | Sanções administrativas e multas da ANPD `[F051]`, perda de credibilidade e danos aos titulares. | Média | **Alto** | **Alto** | Adoção de *Privacy by Design*, princípio da minimização de dados, conexão segura HTTPS e segregação de privilégios. | Gustavo Antonio (Segurança) |
| **RSK-E03** | **Alucinação Factual e Dependência Acrítica de IA Generativa** | Geração e publicação de informações inverídicas, códigos vulneráveis ou referências inexistentes produzidas por LLMs. | Limitações probabilísticas intrínsecas dos modelos de linguagem e falta de checagem humana. | Falhas de segurança no código em produção, decisões baseadas em premissas falsas e plágio involuntário. | Alta | **Alto** | **Alto** | Política institucional de checagem factual obrigatória (*fact-checking*), testes em compilador e log de transparência de prompts em `uso_ia.md`. | Gabriel Amancio (Dev) |
| **RSK-E04** | **Opacidade Algorítmica e Falta de Explicabilidade (Black Box)** | Impossibilidade técnica de explicar a um usuário ou auditor o porquê de uma resposta ou decisão gerada pelo sistema. | Adoção de modelos de aprendizado profundo excessivamente complexos sem camada interpretável. | Violação do dever de transparência do Marco Civil `[F002]` e da LGPD `[F001]`, gerando insegurança jurídica. | Média | **Médio** | **Médio** | Utilização de modelos interpretáveis, geração de justificativas em linguagem simples e direito à revisão humana de decisões automatizadas. | Paulo Germano (Dados/IA) |
| **RSK-E05** | **Barreiras de Acessibilidade Digital e Exclusão de Usuários** | Interface gráfica inacessível para pessoas com deficiência visual, auditiva, motora ou neurodivergentes `[F007]`. | Não observância das diretrizes WCAG 2.2, contraste inadequado de cores e navegação dependente de mouse. | Impossibilidade de uso por parcelas vulneráveis da população e infração à Lei Brasileira de Inclusão. | Média | **Alto** | **Alto** | Implementação das diretrizes WCAG 2.2 nível AA `[F007]`, compatibilidade com leitores de tela e validação em testes de usabilidade (Etapa 6). | Gabriel Amancio (Dev) |
| **RSK-E06** | **Injeção de Código e Vulnerabilidades Críticas em APIs (OWASP Top 10)** | Invasão do backend por exploração de falhas clássicas de injeção SQL, Cross-Site Scripting (XSS) ou Broken Access Control. | Falta de sanitização de dados recebidos via requisições HTTP e uso de bibliotecas desatualizadas. | Comprometimento total da base de dados, roubo de credenciais e indisponibilidade do serviço. | Baixa | **Crítico** | **Alto** | Validação estrita de tipos e entradas, uso de Object-Relational Mapping (ORM) parametrizado e esteiras de análise estática (SAST). | Gustavo Antonio (Segurança) |
| **RSK-E07** | **Falhas de Disponibilidade e Perda de Integridade de Backups** | Indisponibilidade do serviço e perda permanente de dados durante picos de acesso ou falhas de hardware/servidores. | Infraestrutura monolítica sem redundância, ausência de testes periódicos de restauração de backup. | Interrupção prolongada da solução tecnológica e prejuízo aos serviços prestados à comunidade. | Baixa | **Alto** | **Médio** | Estratégia de backup automatizado 3-2-1 (3 cópias, 2 mídias, 1 fora do local), monitoramento de uptime via Zabbix e redundância de servidores. | Luiz Miguel (Infra) |
| **RSK-E08** | **Pegada Hídrica e Energética de Sistemas Computacionais (Green IT)** | Consumo desproporcional de eletricidade e emissões de carbono decorrentes de computação em nuvem ineficiente. | Arquitetura de microsserviços superdimensionada e reprocessamento redundante de pipelines de dados. | Impacto socioambiental negativo contrário aos Objetivos de Desenvolvimento Sustentável (ODS) da ONU. | Média | **Médio** | **Médio** | Princípios de computação sustentável (Green IT): otimização de consultas em banco, desligamento de ambientes ociosos e cache eficiente. | Luiz Miguel (Infra) |
