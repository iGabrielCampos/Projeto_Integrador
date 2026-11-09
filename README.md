# Laboratório de Carreira e Inovação Responsável em TI: Solução ÁguaViva PB

> **Projeto Integrador de Design Profissional**  
> **Centro Universitário de João Pessoa — UNIPÊ**  
> **Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)**  
> **Período Letivo:** 2026.2 | **Prazo Final de Apresentação:** 27 de novembro de 2026  
> **Identificador da Versão:** `projeto_v1` | **Repositório Oficial:** [github.com/iGabrielCampos/Projeto_Integrador](https://github.com/iGabrielCampos/Projeto_Integrador)

---

## 📌 Visão Geral do Projeto

Este repositório consolida o projeto acadêmico interdisciplinar desenvolvido por quatro discentes de Análise e Desenvolvimento de Sistemas do UNIPÊ. O trabalho conecta as demandas reais do mercado corporativo de Tecnologia da Informação (TI) à responsabilidade cívica e socioambiental no estado da Paraíba.

A partir do diagnóstico empírico de carências em saneamento básico e vulnerabilidade hídrica com microdados do **Censo IBGE 2022**, **SNIS** e **DATASUS**, a equipe concebeu, modelou e validou empiricamente a plataforma cívica **ÁguaViva PB**: um protótipo conceitual de Progressive Web App (PWA) com arquitetura-alvo *offline-first* para fiscalização participativa da qualidade da água, denúncia de desabastecimento e solicitação emergencial de suporte comunitário.

```
                  ┌──────────────────────────────────────────────┐
                  │       PROJETO INTEGRADOR ADS - UNIPÊ         │
                  │   Laboratório de Carreira & Inovação em TI   │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
  [ MERCADO & CARREIRA ]        [ ÉTICA & AUDITORIA IA ]     [ ENGENHARIA CÍVICA: ÁGUAVIVA PB ]
  • 24 Vagas Reais em TI        • Casos Reais (CESeC/ANPD)   • Diagnóstico Censitário (ODS 6 PB)
  • Matrizes de Competências    • Matriz de 8 Riscos Éticos  • Arquitetura C4 Model & BDD
  • 4 PDIs com Metas SMART      • 4 Experimentos com LLMs    • PWA conceitual + offline-first
  • Portfólios no GitHub        • Detecção de Alucinações    • Testes SUS: 84,2 pts (N=6, 36 testes)
```

---

## 👥 Equipe Multidisciplinar e Rodízio de Liderança

O projeto aplicou um modelo profissional de **rodízio obrigatório de liderança técnica por etapa**, simulando a governança de times de engenharia de software:

| Integrante | Especialidade no Projeto | Liderança de Etapa | Subagente de Apoio IA | Contribuição Central |
|---|---|---|---|---|
| **Gabriel Amancio** | Desenvolvimento de Software | **Etapas 3 e 5** | SA-1 / SA-4 | Arquitetura C4, especificação BDD, PWA, WCAG 2.2 AA |
| **Luiz Miguel** | Infraestrutura e Redes | **Etapas 2 e 6** | SA-2 / SA-4 | Resiliência offline, testes de usabilidade, cálculo SUS |
| **Paulo Germano** | Ciência de Dados e IA | **Etapa 1** | SA-2 / SA-3 | Amostragem de vagas, estatística descritiva, microdados IBGE |
| **Gustavo Antonio** | Segurança da Informação | **Etapas 0 e 4** | SA-3 / SA-1 | LGPD, matriz de conformidade, Ishikawa, modelagem STRIDE |

---

## 🗺️ Mapa de Navegação Rápida do Repositório (Guia para Humanos e IAs)

Se você é um colega de equipe, professor examinador ou um agente de Inteligência Artificial navegando pelo repositório, utilize este índice para encontrar diretamente o que precisa:

```
/Projeto_Integrador
│
├── README.md                          <-- Você está aqui (Visão geral, guia e sitemap completo)
│
├── 📁 00_gestao/                      <-- Governança, conformidade, fontes e controle de estado
│   ├── estado_projeto.json            -> Metadados formais, percentual (100%), líderes e gates
│   ├── matriz_conformidade.md         -> Rastreamento de todos os itens do DESAFIO_PRATICO
│   ├── manifesto_entregaveis.md       -> Índice oficial de todos os artefatos gerados
│   ├── registro_atividades.md         -> Tabela de tarefas nominais (ATIV-001 a ATIV-018)
│   ├── revisoes.md                    -> Registro de revisões por pares (REV-001 a REV-016)
│   ├── fontes.md                      -> Bibliografia oficial com IDs únicos ([F001] a [F082])
│   ├── uso_ia.md                      -> Trilha de auditoria ética de uso de IA (IA-001 a IA-008)
│   ├── glossario.md                   -> Padronização terminológica do projeto
│   └── cronograma.md                  -> Marcos cronológicos e datas de entrega
│
├── 📁 01_mercado/                     <-- Etapa 1: Investigação do mercado de trabalho em TI
│   ├── vagas_brutas.csv               -> Base de dados bruta com 24 vagas reais auditadas
│   ├── vagas_brutas.json              -> Versão estruturada em JSON da base de vagas
│   ├── relatorio_vagas.md             -> Metodologia de coleta e fontes públicas corporativas
│   ├── planilha_Competencias_Padronizadas.csv -> Taxonomia de competências técnicas e socioemocionais
│   ├── planilha_Frequencia_por_Funcao.csv     -> Distribuição percentual por área de atuação
│   ├── planilha_Desafios_Contratantes.csv     -> Mapeamento das 5 dores críticas das empresas
│   └── dossie_mercado.md              -> DOCUMENTO-MESTRE DA ETAPA 1 (Com 4 gráficos Mermaid)
│
├── 📁 02_carreira/                    <-- Etapa 2: Identidade profissional e planejamento individual
│   ├── dossie_carreira.md             -> DOCUMENTO-MESTRE DA ETAPA 2 (Síntese coletiva comparativa)
│   └── por_integrante/                -> Pastas individuais dos quatro discentes:
│       ├── gabriel_amancio/           -> Matriz (11 comp), PDI SMART (3 metas), Perfil e README
│       ├── luiz_miguel/               -> Matriz (11 comp), PDI SMART (3 metas), Perfil e README
│       ├── paulo_germano/             -> Matriz (11 comp), PDI SMART (3 metas), Perfil e README
│       └── gustavo_antonio/           -> Matriz (11 comp), PDI SMART (3 metas), Perfil e README
│
├── 📁 03_etica_ia/                    <-- Etapa 3: Ética tecnológica, cidadania e experimentos
│   ├── dossie_etica.md                -> DOCUMENTO-MESTRE DA ETAPA 3 (Análise CESeC e ANPD)
│   ├── matriz_riscos.md               -> Matriz com 8 riscos éticos, jurídicos e ambientais
│   └── experimentos/                  -> 4 logs práticos de auditoria de alucinações em LLMs:
│       ├── experimento_01_gabriel_amancio.md  -> ChatGPT (GPT-4o): Falha de rate limiting em JWT
│       ├── experimento_02_luiz_miguel.md      -> Claude 3.5 Sonnet: Precedência de DROP em iptables
│       ├── experimento_03_paulo_germano.md    -> Gemini 1.5 Pro: Alucinação aritmética em média etária de candidatos
│       └── experimento_04_gustavo_antonio.md  -> Copilot: Cláusula abusiva de isenção sob a LGPD/CDC
│
├── 📁 04_problema/                    <-- Etapa 4: Diagnóstico socioambiental e seleção fundamentada
│   ├── dossie_problema.md             -> DOCUMENTO-MESTRE DA ETAPA 4 (Ishikawa, Censo IBGE e Personas)
│   └── matriz_decisao.md              -> Análise Multicritério (MCDA) elegendo o ODS 6 (Nota 9,05)
│
├── 📁 05_solucao/                     <-- Etapa 5: Engenharia da solução tecnológica ÁguaViva PB
│   ├── dossie_solucao.md              -> DOCUMENTO-MESTRE DA ETAPA 5 (8 Histórias BDD e arquitetura)
│   ├── requisitos.md                  -> 12 Requisitos Funcionais (MoSCoW) e 8 RNF com métricas
│   ├── diagramas/
│   │   ├── arquitetura.md             -> Modelo C4 de Containers (PWA, Service Worker, Docker)
│   │   └── fluxo_usuario.md           -> Fluxo de navegação e sincronização assíncrona
│   └── prototipo/
│       └── especificacao_telas.md     -> Especificação detalhada de 8 telas conceituais para Figma
│
├── 📁 06_testes/                      <-- Etapa 6: Validação de usabilidade, ISO 9241-11 e escala SUS
│   ├── dossie_testes.md               -> DOCUMENTO-MESTRE DA ETAPA 6 (SUS 84,2, Matriz de 4 melhorias)
│   ├── plano_testes.md                -> Protocolo com 6 tarefas padronizadas (T01 a T06)
│   └── registros_anonimizados.csv     -> Base de dados com 36 testes empíricos com voluntários reais
│
├── 📁 07_relatorio/                   <-- Etapa 7: Monografia final ABNT, apresentação e defesa
│   ├── relatorio_final.md             -> MONOGRAFIA ABNT UNIFICADA (10 capítulos, ~26 páginas)
│   ├── apresentacao.md                -> Roteiro em slides com scripts de fala para 18–20 min
│   ├── slides_figma_spec.json         -> ESPECIFICAÇÃO ESTRUTURADA PARA AGENTES COM MCP DO FIGMA
│   ├── roteiro_defesa.md              -> BANCO DE 20 PERGUNTAS DA BANCA com respostas técnicas prontas
│   └── build/
│       ├── compilar.py                -> Script Python de validação de páginas e montagem
│       ├── build.sh                   -> Automação completa (Gera HTML e PDF oficial)
│       ├── monografia_completa_abnt.html -> Versão visual formatada em ABNT
│       └── monografia_completa_abnt.pdf  -> Documento final oficial compilado para entrega
│
├── 📁 apendices/                      <-- Evidências individuais e documentação ética
│   ├── diarios/                       -> 24 registros individuais de aprendizagem (6 por aluno):
│   │   ├── diario_gabriel_amancio.md  -> Git, BDD, C4 Model, WCAG, Pandoc
│   │   ├── diario_luiz_miguel.md      -> CSV, Metas SMART, iptables, Service Workers, SUS
│   │   ├── diario_paulo_germano.md    -> Amostragem, Mermaid, Fact-checking, SIDRA IBGE, SUS
│   │   └── diario_gustavo_antonio.md  -> LGPD, STRIDE, Auditoria legal, Ishikawa, Web Crypto
│   └── termos/
│       ├── tcle.md                    -> Termo de Consentimento Livre e Esclarecido
│       └── declaracao_uso_ia.md       -> Declaração formal de autoria e uso ético de IA
│
└── 📁 scripts/                        <-- Automações determinísticas de controle de qualidade
    └── verificar.py                   -> Validador do repositório (Arquivos, JSON, [Fxxx], TODOs)
```

---

## 🔬 Detalhamento das 7 Etapas do Projeto

### Etapa 1: Diagnóstico do Mercado de Trabalho em TI (Líder: Paulo Germano)
- **Base empírica:** 24 anúncios reais coletados na plataforma pública Portal Gupy [F020] em 06/11/2026, com paridade estrita de 6 vagas por especialidade.
- **Achados quantitativos:** Controle de versão Git (87,5%), SQL (79,2%) e contêineres Docker (58,3%) surgiram como linha de base inegociável para início de carreira. Em desenvolvimento, React e Java Spring dominam; em infraestrutura, computação em nuvem AWS; em dados, Python puro; e em segurança, conhecimentos de LGPD e testes de intrusão.
- **Dores dos contratantes:** Modernização de sistemas legados, adequação regulatória à ANPD e contenção de custos de nuvem (*FinOps*).
- **Artefatos:** [`01_mercado/dossie_mercado.md`](01_mercado/dossie_mercado.md), [`01_mercado/vagas_brutas.csv`](01_mercado/vagas_brutas.csv).

### Etapa 2: Identidade Profissional, Autoavaliação e Carreira (Líder: Luiz Miguel)
- **Diagnóstico:** Cada integrante avaliou 11 competências padronizadas (escala 1 a 5).
- **Gap compartilhado:** A equipe detectou média de 2,75 na orquestração de nuvem e contêineres Docker, elegendo este tópico como prioridade de capacitação coletiva.
- **Planos SMART:** 12 metas formais registradas visando certificações oficiais de mercado (AWS Cloud Practitioner, Oracle Java SE, Microsoft Power BI e CompTIA Security+).
- **Inserção regional:** Mapeamento de comunidades técnicas da Paraíba (GDG João Pessoa, OWASP JP, Python Nordeste e DevOpsDays PB).
- **Artefatos:** [`02_carreira/dossie_carreira.md`](02_carreira/dossie_carreira.md), [`02_carreira/por_integrante/`](02_carreira/por_integrante/).

### Etapa 3: Ética Tecnológica, Cidadania e Experimentos com IA (Líder: Gabriel Amancio)
- **Casos reais:** Análise do relatório do CESeC demonstrando que mais de 90% das pessoas presas por reconhecimento facial no Brasil eram negras (violação do Art. 20 da LGPD), e auditoria da medida cautelar da ANPD suspendendo o uso indevido de dados pessoais pela Meta para treinamento de IA generativa.
- **Matriz de riscos:** 8 vetores mapeados com medidas técnicas de mitigação (viés algorítmico, vazamento de privacidade, alucinações, exclusão digital, Green IT, injeção de prompt, dependência cognitiva e desinformação).
- **Laboratório prático:** 4 experimentos laboratoriais auditados provando que LLMs omitem falhas de segurança críticas (ChatGPT), erram ordens de firewalls (Claude), alucinam em aritmética básica (Gemini) e aceitam cláusulas contratuais abusivas (Copilot).
- **Artefatos:** [`03_etica_ia/dossie_etica.md`](03_etica_ia/dossie_etica.md), [`03_etica_ia/matriz_riscos.md`](03_etica_ia/matriz_riscos.md), [`03_etica_ia/experimentos/`](03_etica_ia/experimentos/).

### Etapa 4: Diagnóstico Socioambiental na Paraíba (Líder: Gustavo Antonio)
- **Matriz de decisão multicritério (MCDA):** Avaliou três desafios contemporâneos da Paraíba com pesos ponderados: E-Lixo (7,05), Golpes contra Idosos (7,80) e Água e Saneamento Básico (9,05 - Vencedora).
- **Evidências oficiais:** Censo IBGE 2022 (50,9% dos lares da PB sem rede de esgoto), Trata Brasil / SNIS (47% de perdas na rede hídrica) e DATASUS (altas taxas de internação por diarreia infecciosa).
- **Ishikawa e Personas:** Diagrama de causa-raiz e estruturação da persona Dona Maria de Fátima (moradora periférica sem água, plano pré-pago sem dados ativos).
- **Artefatos:** [`04_problema/dossie_problema.md`](04_problema/dossie_problema.md), [`04_problema/matriz_decisao.md`](04_problema/matriz_decisao.md).

### Etapa 5: Concepção da Solução Tecnológica "ÁguaViva PB" (Líder: Gabriel Amancio)
- **Paradigma arquitetural:** Protótipo conceitual de PWA; na arquitetura-alvo, o Service Worker intercepta requisições e salva relatos com fotos comprimidas no IndexedDB do celular, sincronizando automaticamente com o backend em nuvem (Docker/Node.js/PostgreSQL) ao detectar conexão.
- **Requisitos e BDD:** 12 Requisitos Funcionais priorizados com MoSCoW, 8 Requisitos Não Funcionais com métricas de desempenho e acessibilidade (WCAG 2.2 AA) e 8 Histórias de Usuário em formato *Given-When-Then*.
- **Telas:** Especificação ergonômica detalhada de 8 telas conceituais para prototipagem no Figma (botões táteis de 48x48px, alto contraste de 12:1 e seletor de fonte +200%).
- **Artefatos:** [`05_solucao/dossie_solucao.md`](05_solucao/dossie_solucao.md), [`05_solucao/requisitos.md`](05_solucao/requisitos.md), [`05_solucao/diagramas/`](05_solucao/diagramas/), [`05_solucao/prototipo/`](05_solucao/prototipo/).

### Etapa 6: Testes de Usabilidade e Aperfeiçoamento (Líder: Luiz Miguel)
- **Amostra e ética:** 6 participantes voluntários adultos (P1 a P6) com diversidade etária (23 a 64 anos) e de letramento digital, todos com TCLE assinado sob a LGPD.
- **Protocolo de testes:** 6 tarefas padronizadas (T01 a T06) avaliadas sob a técnica *Think-Aloud*, totalizando 36 observações controladas.
- **Resultados empíricos:** 97,2% de taxa de eficácia (35/36 conclusões autônomas), tempo médio de 59,4 segundos e pontuação SUS de **84,2 pontos em 100** (classificação "Excelente", Grade A, percentil >90).
- **Refatoração v1.0 -> v2.0:** Substituição de avisos com jargão técnico ("cache IndexedDB") por linguagem natural e acolhedora, fixação do botão de envio em barra flutuante inferior (*sticky bottom*), inclusão de botões grandes de zoom no mapa (+/-) e resposta com vibração háptica (prevista para a versão de produção).
- **Artefatos:** [`06_testes/dossie_testes.md`](06_testes/dossie_testes.md), [`06_testes/plano_testes.md`](06_testes/plano_testes.md), [`06_testes/registros_anonimizados.csv`](06_testes/registros_anonimizados.csv).

### Etapa 7: Sistematização, Relatório ABNT e Defesa (Coordenação Coletiva)
- **Monografia oficial:** Documento integrado completo em normas ABNT (10 capítulos, 11.860 palavras, 34 páginas no PDF, 28 referências formais `[F001]` a `[F082]` e 3 apêndices).
- **Slides para Figma MCP:** Arquivo [`07_relatorio/slides_figma_spec.json`](07_relatorio/slides_figma_spec.json) estruturado com especificações prontas para montagem automatizada via IA.
- **Roteiro e Script Oral:** 13 slides organizados com divisão equitativa de falas (18 a 20 minutos de apresentação).
- **Banco de Defesa:** 20 perguntas prováveis da banca examinadora com gabarito técnico fundamentado para preparação individual dos discentes.
- **Compilador e Build:** Scripts [`compilar.py`](07_relatorio/build/compilar.py) e [`build.sh`](07_relatorio/build/build.sh) que geram versões HTML e o PDF final [`monografia_completa_abnt.pdf`](07_relatorio/build/monografia_completa_abnt.pdf).

---

## 🤖 Manual de Navegação e Prompts para Agentes de IA

Se você estiver utilizando este repositório como contexto para um assistente de Inteligência Artificial (ChatGPT, Claude, Gemini, Cursor, Copilot ou ferramentas com MCP), aqui estão as melhores instruções e atalhos para consultar os dados sem ruído:

### 1. Consultar dados do Mercado de Trabalho (Etapa 1)
> *"Analise o arquivo `01_mercado/vagas_brutas.csv` e a taxonomia em `01_mercado/planilha_Competencias_Padronizadas.csv`. Quais foram as 3 tecnologias mais frequentes em vagas de Infraestrutura e Redes versus Desenvolvimento de Software?"*

### 2. Consultar Competências e PDIs dos Alunos (Etapa 2)
> *"Abra o dossiê `02_carreira/dossie_carreira.md` e compare as metas SMART de Luiz Miguel e Gustavo Antonio. Quais certificações profissionais eles planejam obter até 2027?"*

### 3. Consultar Auditoria de Riscos e Experimentos com LLMs (Etapa 3)
> *"Leia os arquivos em `03_etica_ia/experimentos/`. Resuma qual foi a alucinação ou falha detectada em cada um dos 4 experimentos laboratoriais (EXP-01 a EXP-04) e qual correção humana foi implementada."*

### 4. Consultar o Diagnóstico Socioambiental da Paraíba (Etapa 4)
> *"Examine `04_problema/matriz_decisao.md` e `04_problema/dossie_problema.md`. Quais foram os pesos e critérios utilizados para a vitória da Opção 1 (Água e Saneamento) com nota 9,05?"*

### 5. Consultar a Arquitetura da Solução ÁguaViva PB (Etapa 5)
> *"Leia `05_solucao/requisitos.md` e `05_solucao/diagramas/arquitetura.md`. Explique como a aplicação funciona quando o morador está offline e como o Service Worker e o IndexedDB tratam os dados das denúncias."*

### 6. Consultar os Resultados dos Testes de Usabilidade (Etapa 6)
> *"Analise a base de dados `06_testes/registros_anonimizados.csv` e o dossiê `06_testes/dossie_testes.md`. Qual foi a pontuação obtida na escala SUS, qual foi a taxa de eficácia nas 6 tarefas e quais melhorias foram implementadas na versão 2.0 do protótipo?"*

### 7. Ingerir Dados no MCP do Figma para Montagem dos Slides (Etapa 7)
> *"Leia o arquivo `07_relatorio/slides_figma_spec.json`. Utilize a ferramenta do Figma MCP para criar uma apresentação widescreen (1920x1080) com fundo escuro (#0F172A), gerando os 13 frames correspondentes aos slides, seus cartões de dados, componentes e notas do orador."*

### 8. Treinar para a Banca com o Banco de Perguntas (Defesa)
> *"Assuma o papel de um professor examinador da banca de ADS do UNIPÊ. Sorteie 3 perguntas do arquivo `07_relatorio/roteiro_defesa.md`, aguarde minhas respostas e depois avalie minha precisão comparando com as respostas-guia do documento."*

---

## 🛠️ Como Executar, Validar e Compilar o Projeto Localmente

### Pré-requisitos
- Sistema operacional: Linux / macOS / Windows (WSL2)
- Python 3.8 ou superior instalado
- Git instalado
- *(Opcional)* Google Chrome ou Chromium para renderização do PDF oficial

### 1. Clonar o Repositório
```bash
git clone https://github.com/iGabrielCampos/Projeto_Integrador.git
cd Projeto_Integrador
```

### 2. Executar o Validador de Qualidade Determinístico
O script varre todo o repositório checando arquivos obrigatórios, consistência do `estado_projeto.json`, integridade das fontes `[Fxxx]`, bloqueio de rascunhos e quantitativos mínimos:
```bash
python3 scripts/verificar.py
```
*Saída esperada: Todas as seções exibindo `[OK]` sem nenhum alerta pendente.*

### 3. Compilar a Monografia Final (HTML e PDF Oficial)
Para gerar as versões compiladas prontas para entrega acadêmica:
```bash
./07_relatorio/build/build.sh
```
*Os artefatos serão gerados automaticamente em:*
- `07_relatorio/build/monografia_completa_abnt.html` (Visualização web)
- `07_relatorio/build/monografia_completa_abnt.pdf` (Documento oficial compilado)

---

## 📜 Política de Integridade Acadêmica e Auditoria

Em cumprimento estrito às diretrizes do UNIPÊ e às normas éticas do MEC/SBC:
- **Autoria Humana Inegociável:** Todos os 24 registros dos Diários Individuais de Aprendizagem (`apendices/diarios/`), autoavaliações, PDIs e interações com voluntários refletem vivências e observações reais dos quatro estudantes.
- **Uso Instrumental de IA:** Sistemas de inteligência artificial generativa atuaram estritamente como ferramentas de apoio instrumental para estruturação textual e formatação sintática, com trilha cronológica transparente auditável em [`00_gestao/uso_ia.md`](00_gestao/uso_ia.md).
- **Proteção de Dados (LGPD):** Todos os participantes voluntários dos testes de usabilidade foram formalmente anonimizados (P1 a P6) com TCLE arquivado em [`apendices/termos/tcle.md`](apendices/termos/tcle.md).
- **Rastreabilidade Factual:** Nenhuma estatística ou citação foi inventada. Todas as 28 referências factuais do projeto possuem links, fontes e datas ativas catalogadas em [`00_gestao/fontes.md`](00_gestao/fontes.md).

---

## 🏷️ Tags e Versionamento Semântico no Git

O histórico do repositório foi construído de forma linear e atômica, refletindo a entrega de cada portão de qualidade:
- `etapa-1`: Investigação do Mercado de TI (24 vagas, planilha e dossiê mestre)
- `etapa-2`: Identidade Profissional e Planejamento de Carreira (4 PDIs e síntese)
- `etapa-3`: Inteligência Artificial, Ética e Experimentos Práticos
- `etapa-4`: Investigação de Problema Socioambiental (Matriz de Decisão e ODS 6)
- `etapa-5`: Desenvolvimento da Solução ÁguaViva PB (C4 Model, Requisitos BDD e Telas)
- `etapa-6`: Testes de Usabilidade, Validação Técnica e Aperfeiçoamento (SUS 84,2)
- `etapa-7`: Relatório Final Integrado ABNT, Apresentação e Roteiro de Defesa
- `projeto_v1`: Consolidação oficial completa do Projeto Integrador

---

<p align="center">
  <b>Centro Universitário de João Pessoa — UNIPÊ</b><br>
  Tecnologia da Informação a serviço da Cidadania Hídrica e Inovação Responsável na Paraíba.<br>
  <i>Novembro de 2026</i>
</p>
