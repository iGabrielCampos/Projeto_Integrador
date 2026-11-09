# Laboratório de Carreira e Inovação Responsável em TI: Solução ÁguaViva PB

> **Projeto Integrador de Design Profissional**  
> **Centro Universitário de João Pessoa (UNIPÊ)**  
> **Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)**  
> **Período Letivo:** 2026.2 | **Prazo Final de Apresentação:** 27 de novembro de 2026  
> **Identificador da Versão:** `projeto_v1` | **Repositório Oficial:** [github.com/iGabrielCampos/Projeto_Integrador](https://github.com/iGabrielCampos/Projeto_Integrador)

---

## Visão Geral do Projeto

Este repositório reúne o projeto acadêmico interdisciplinar desenvolvido por quatro estudantes de Análise e Desenvolvimento de Sistemas do UNIPÊ. O trabalho analisa demandas do mercado de Tecnologia da Informação (TI) e propõe uma intervenção voltada à realidade socioambiental da Paraíba.

A partir do levantamento sobre saneamento básico e vulnerabilidade hídrica com dados do Censo IBGE 2022, SNIS e DATASUS, a equipe modelou a plataforma cívica **ÁguaViva PB**: um protótipo conceitual de Progressive Web App (PWA) com arquitetura *offline-first* para registro de desabastecimento, fiscalização da qualidade da água e solicitação de apoio comunitário.

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

## Equipe e Rodízio de Liderança

O projeto adotou um modelo de rodízio de liderança técnica por etapa, acompanhando práticas comuns de times de engenharia de software:

| Integrante | Especialidade no Projeto | Liderança de Etapa | Subagente de Apoio IA | Contribuição Central |
|---|---|---|---|---|
| **Gabriel Amancio** | Desenvolvimento de Software | Etapas 3 e 5 | SA-1 / SA-4 | Arquitetura C4, especificação BDD, PWA, WCAG 2.2 AA |
| **Luiz Miguel** | Infraestrutura e Redes | Etapas 2 e 6 | SA-2 / SA-4 | Resiliência offline, testes de usabilidade, cálculo SUS |
| **Paulo Germano** | Ciência de Dados e IA | Etapa 1 | SA-2 / SA-3 | Amostragem de vagas, estatística descritiva, microdados IBGE |
| **Gustavo Antonio** | Segurança da Informação | Etapas 0 e 4 | SA-3 / SA-1 | LGPD, matriz de conformidade, Ishikawa, modelagem STRIDE |

---

## Mapa de Navegação do Repositório

O índice abaixo orienta a localização direta de cada artefato e documento do projeto:

```
/Projeto_Integrador
│
├── README.md                          <-- Visão geral, guia e estrutura completa
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
│   ├── apresentacao.md                -> Roteiro em slides com scripts de fala para 18 a 20 min
│   ├── slides_figma_spec.json         -> ESPECIFICAÇÃO ESTRUTURADA PARA FIGMA
│   ├── roteiro_defesa.md              -> BANCO DE 20 PERGUNTAS DA BANCA com respostas técnicas
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

## Detalhamento das 7 Etapas do Projeto

### Etapa 1: Diagnóstico do Mercado de Trabalho em TI (Líder: Paulo Germano)
- **Base empírica:** 24 anúncios reais coletados na plataforma pública Portal Gupy [F020] em 06/11/2026, com divisão de 6 vagas por especialidade.
- **Achados quantitativos:** Controle de versão Git (87,5%), SQL (79,2%) e contêineres Docker (58,3%) formam a base técnica comum para início de carreira. Em desenvolvimento, aparecem com frequência React e Java Spring; em infraestrutura, nuvem AWS; em ciência de dados, Python; e em segurança da informação, conhecimentos de LGPD e testes de intrusão.
- **Demandas dos contratantes:** Modernização de sistemas legados, adequação regulatória à ANPD e gestão de custos em nuvem (FinOps).
- **Artefatos:** [`01_mercado/dossie_mercado.md`](01_mercado/dossie_mercado.md), [`01_mercado/vagas_brutas.csv`](01_mercado/vagas_brutas.csv).

### Etapa 2: Identidade Profissional, Autoavaliação e Carreira (Líder: Luiz Miguel)
- **Diagnóstico:** Cada integrante avaliou 11 competências padronizadas em escala de 1 a 5.
- **Ponto de melhoria coletivo:** A equipe registrou média de 2,75 em orquestração de nuvem e contêineres Docker, definindo o tópico como prioridade de capacitação conjunta.
- **Planos SMART:** 12 metas formais registradas voltadas a certificações de mercado (AWS Cloud Practitioner, Oracle Java SE, Microsoft Power BI e CompTIA Security+).
- **Inserção regional:** Mapeamento de comunidades técnicas da Paraíba (GDG João Pessoa, OWASP JP, Python Nordeste e DevOpsDays PB).
- **Artefatos:** [`02_carreira/dossie_carreira.md`](02_carreira/dossie_carreira.md), [`02_carreira/por_integrante/`](02_carreira/por_integrante/).

### Etapa 3: Ética Tecnológica, Cidadania e Experimentos com IA (Líder: Gabriel Amancio)
- **Casos reais:** Análise do relatório do CESeC sobre prisões por reconhecimento facial no Brasil (violação do Art. 20 da LGPD) e da medida cautelar da ANPD que suspendeu o uso de dados pessoais pela Meta para treinamento de IA generativa.
- **Matriz de riscos:** 8 vetores mapeados com medidas técnicas de mitigação (viés algorítmico, vazamento de privacidade, alucinações, exclusão digital, Green IT, injeção de prompt, dependência cognitiva e desinformação).
- **Laboratório prático:** 4 experimentos auditados mostrando que LLMs omitem falhas de segurança em autenticação (ChatGPT), erram ordens de firewalls (Claude), alucinam em cálculos de média (Gemini) e aceitam cláusulas contratuais abusivas (Copilot).
- **Artefatos:** [`03_etica_ia/dossie_etica.md`](03_etica_ia/dossie_etica.md), [`03_etica_ia/matriz_riscos.md`](03_etica_ia/matriz_riscos.md), [`03_etica_ia/experimentos/`](03_etica_ia/experimentos/).

### Etapa 4: Diagnóstico Socioambiental na Paraíba (Líder: Gustavo Antonio)
- **Matriz de decisão multicritério (MCDA):** Avaliou três desafios da Paraíba com critérios ponderados: E-Lixo (7,05), Golpes contra Idosos (7,80) e Água e Saneamento Básico (9,05, opção selecionada).
- **Evidências oficiais:** Censo IBGE 2022 (50,9% dos lares da PB sem rede de esgoto), Trata Brasil e SNIS (47% de perdas na rede hídrica) e DATASUS (taxas de internação por diarreia infecciosa).
- **Ishikawa e Personas:** Diagrama de causa e efeito e caracterização da persona Dona Maria de Fátima (moradora de área periférica com desabastecimento frequente e acesso restrito a dados móveis).
- **Artefatos:** [`04_problema/dossie_problema.md`](04_problema/dossie_problema.md), [`04_problema/matriz_decisao.md`](04_problema/matriz_decisao.md).

### Etapa 5: Concepção da Solução Tecnológica "ÁguaViva PB" (Líder: Gabriel Amancio)
- **Paradigma arquitetural:** Protótipo conceitual de PWA. Na arquitetura-alvo, o Service Worker intercepta requisições e salva relatos com fotos comprimidas no IndexedDB do dispositivo, sincronizando com o backend (Docker, Node.js e PostgreSQL) quando houver conexão.
- **Requisitos e BDD:** 12 Requisitos Funcionais priorizados com MoSCoW, 8 Requisitos Não Funcionais com métricas de desempenho e acessibilidade (WCAG 2.2 AA) e 8 Histórias de Usuário no formato *Given-When-Then*.
- **Telas:** Especificação detalhada de 8 telas conceituais para prototipagem (alvos de toque de 48x48px, contraste de 12:1 e suporte a escala de fonte até 200%).
- **Artefatos:** [`05_solucao/dossie_solucao.md`](05_solucao/dossie_solucao.md), [`05_solucao/requisitos.md`](05_solucao/requisitos.md), [`05_solucao/diagramas/`](05_solucao/diagramas/), [`05_solucao/prototipo/`](05_solucao/prototipo/).

### Etapa 6: Testes de Usabilidade e Aperfeiçoamento (Líder: Luiz Miguel)
- **Amostra e ética:** 6 participantes voluntários adultos (P1 a P6) com idades entre 23 e 64 anos e diferentes níveis de familiaridade com tecnologia, todos com TCLE assinado sob os termos da LGPD.
- **Protocolo de testes:** 6 tarefas padronizadas (T01 a T06) acompanhadas com a técnica *Think-Aloud*, totalizando 36 observações.
- **Resultados empíricos:** 97,2% de eficácia (35 de 36 tarefas concluídas de forma autônoma), tempo médio de 59,4 segundos e pontuação SUS de **84,2 pontos em 100** (classificação "Excelente", grau A, percentil >90).
- **Ajustes v1.0 para v2.0:** Substituição de mensagens com jargão técnico ("cache IndexedDB") por avisos claros ao usuário, fixação do botão de envio em barra inferior fixa (*sticky bottom*), adição de botões ampliados de zoom no mapa (+/-) e previsão de resposta háptica na versão final.
- **Artefatos:** [`06_testes/dossie_testes.md`](06_testes/dossie_testes.md), [`06_testes/plano_testes.md`](06_testes/plano_testes.md), [`06_testes/registros_anonimizados.csv`](06_testes/registros_anonimizados.csv).

### Etapa 7: Sistematização, Relatório ABNT e Defesa (Coordenação Coletiva)
- **Monografia oficial:** Documento integrado completo em normas ABNT (10 capítulos, 11.860 palavras, 34 páginas no PDF, 28 referências formais `[F001]` a `[F082]` e 3 apêndices).
- **Slides para Figma:** Arquivo [`07_relatorio/slides_figma_spec.json`](07_relatorio/slides_figma_spec.json) com especificações estruturadas para montagem visual dos slides.
- **Roteiro de apresentação:** 13 slides organizados com divisão planejada de falas para 18 a 20 minutos de apresentação.
- **Banco de Defesa:** 20 questões potenciais da banca examinadora com respostas técnicas de apoio para os discentes.
- **Scripts de montagem:** Scripts [`compilar.py`](07_relatorio/build/compilar.py) e [`build.sh`](07_relatorio/build/build.sh) que geram as versões HTML e o PDF final [`monografia_completa_abnt.pdf`](07_relatorio/build/monografia_completa_abnt.pdf).

---

## Roteiro de Consultas ao Acervo

Para localizar informações específicas dentro do repositório, os pontos de consulta abaixo indicam os arquivos de referência de cada tema:

### 1. Dados do Mercado de Trabalho (Etapa 1)
- Consultar `01_mercado/vagas_brutas.csv` e `01_mercado/planilha_Competencias_Padronizadas.csv` para verificar frequências e tecnologias exigidas por área de atuação.

### 2. Competências e PDIs dos Alunos (Etapa 2)
- Consultar `02_carreira/dossie_carreira.md` para comparar planos individuais, notas de autoavaliação e metas de certificação.

### 3. Auditoria de Riscos e Experimentos com LLMs (Etapa 3)
- Consultar a pasta `03_etica_ia/experimentos/` para analisar falhas detectadas em cada teste de laboratório (EXP-01 a EXP-04) e correções aplicadas.

### 4. Diagnóstico Socioambiental da Paraíba (Etapa 4)
- Consultar `04_problema/matriz_decisao.md` e `04_problema/dossie_problema.md` para conferir pesos, critérios e fontes censitárias da escolha do ODS 6.

### 5. Arquitetura da Solução ÁguaViva PB (Etapa 5)
- Consultar `05_solucao/requisitos.md` e `05_solucao/diagramas/arquitetura.md` para detalhes sobre armazenamento local com IndexedDB e sincronização via Service Worker.

### 6. Resultados dos Testes de Usabilidade (Etapa 6)
- Consultar `06_testes/registros_anonimizados.csv` e `06_testes/dossie_testes.md` para verificar tempos de tarefa, pontuação SUS e melhorias aplicadas no protótipo.

### 7. Estrutura dos Slides (Etapa 7)
- Consultar `07_relatorio/slides_figma_spec.json` para acessar a especificação dos 13 frames, cartões de métricas e notas de apresentação.

### 8. Preparação para a Defesa Oral
- Consultar `07_relatorio/roteiro_defesa.md` para revisar as 20 perguntas técnicas organizadas por etapa do projeto.

---

## Como Executar, Validar e Compilar o Projeto Localmente

### Pré-requisitos
- Sistema operacional: Linux, macOS ou Windows (WSL2)
- Python 3.8 ou superior
- Git
- *(Opcional)* Google Chrome ou Chromium para geração do PDF via headless browser

### 1. Clonar o Repositório
```bash
git clone https://github.com/iGabrielCampos/Projeto_Integrador.git
cd Projeto_Integrador
```

### 2. Executar o Validador de Qualidade
O script verifica a presença dos arquivos obrigatórios, o arquivo `estado_projeto.json`, a integridade das referências `[Fxxx]` e a ausência de marcadores de rascunho:
```bash
python3 scripts/verificar.py
```

### 3. Compilar a Monografia Final (HTML e PDF)
Para gerar as versões compiladas prontas para entrega:
```bash
./07_relatorio/build/build.sh
```
Os arquivos gerados ficam disponíveis em:
- `07_relatorio/build/monografia_completa_abnt.html` (versão HTML)
- `07_relatorio/build/monografia_completa_abnt.pdf` (documento compilado)

---

## Política de Integridade Acadêmica e Auditoria

Em conformidade com as diretrizes do UNIPÊ e as normas do MEC e da SBC:
- **Autoria dos Trabalhos:** Os 24 registros dos diários individuais (`apendices/diarios/`), as autoavaliações, os PDIs e os testes com voluntários refletem atividades desenvolvidas pelos quatro discentes.
- **Uso Instrumental de Ferramentas:** Ferramentas de apoio computacional foram empregadas para suporte à revisão e estruturação, com histórico documentado em [`00_gestao/uso_ia.md`](00_gestao/uso_ia.md).
- **Proteção de Dados (LGPD):** Os participantes dos testes de usabilidade foram identificados por códigos (P1 a P6), com TCLE arquivado em [`apendices/termos/tcle.md`](apendices/termos/tcle.md).
- **Rastreabilidade:** Os dados e citações apoiam-se em fontes documentadas, listadas em [`00_gestao/fontes.md`](00_gestao/fontes.md).

---

## Versionamento no Git

O histórico do repositório registra os marcos de entrega de cada etapa:
- `etapa-1`: Investigação do mercado de TI (24 vagas, planilha e dossiê mestre)
- `etapa-2`: Identidade profissional e planejamento de carreira (4 PDIs e síntese)
- `etapa-3`: Ética na inteligência artificial e experimentos práticos
- `etapa-4`: Diagnóstico de problema socioambiental (Matriz de Decisão e ODS 6)
- `etapa-5`: Concepção da solução ÁguaViva PB (C4 Model, Requisitos BDD e Telas)
- `etapa-6`: Testes de usabilidade e refinamento técnico (SUS 84,2)
- `etapa-7`: Monografia ABNT, apresentação e roteiro de defesa
- `projeto_v1`: Versão final consolidada do Projeto Integrador

---

<p align="center">
  <b>Centro Universitário de João Pessoa (UNIPÊ)</b><br>
  Tecnologia da Informação a serviço da Cidadania Hídrica e Inovação Responsável na Paraíba.<br>
  <i>Novembro de 2026</i>
</p>
