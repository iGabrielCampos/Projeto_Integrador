---
id: relatorio-final-integrado
etapa: 7
titulo: "LABORATÓRIO DE CARREIRA E INOVAÇÃO RESPONSÁVEL EM TI: Concepção, Validação e Impacto da Solução Cívica ÁguaViva PB no Contexto da Paraíba"
subtitulo: "Relatório Técnico-Científico Integrado do Projeto Integrador de Design Profissional"
instituicao: "Centro Universitário de João Pessoa — UNIPÊ"
curso: "Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas"
autores:
  - "Gabriel Amancio (Desenvolvimento de Software)"
  - "Luiz Miguel (Infraestrutura e Redes)"
  - "Paulo Germano (Dados e IA)"
  - "Gustavo Antonio (Segurança da Informação)"
orientacao: "Corpo Docente do Projeto Integrador de ADS"
local: "João Pessoa — PB"
ano: 2026
versao: 1.0
normas: "ABNT NBR 14724 / NBR 6023 / NBR 6024"
---

# CENTRO UNIVERSITÁRIO DE JOÃO PESSOA — UNIPÊ
## CURSO SUPERIOR DE TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS

<br><br><br>

### GABRIEL AMANCIO
### LUIZ MIGUEL
### PAULO GERMANO
### GUSTAVO ANTONIO

<br><br><br>

# LABORATÓRIO DE CARREIRA E INOVAÇÃO RESPONSÁVEL EM TI: CONCEPÇÃO, VALIDAÇÃO E IMPACTO DA SOLUÇÃO CÍVICA ÁGUAVIVA PB NO CONTEXTO DA PARAÍBA

<br><br><br><br><br>

#### JOÃO PESSOA — PB
#### 2026

---

<br><br><br>

### GABRIEL AMANCIO
### LUIZ MIGUEL
### PAULO GERMANO
### GUSTAVO ANTONIO

<br><br><br>

# LABORATÓRIO DE CARREIRA E INOVAÇÃO RESPONSÁVEL EM TI: CONCEPÇÃO, VALIDAÇÃO E IMPACTO DA SOLUÇÃO CÍVICA ÁGUAVIVA PB NO CONTEXTO DA PARAÍBA

<br><br>

> Relatório Técnico-Científico Integrado apresentado ao Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas do Centro Universitário de João Pessoa (UNIPÊ), como requisito parcial e obrigatório para conclusão do Projeto Integrador de Design Profissional.
> 
> Área de Concentração: Engenharia de Software, Redes e Infraestrutura, Ciência de Dados, Inteligência Artificial e Segurança da Informação.
> 
> Orientadores: Corpo Docente do Projeto Integrador / UNIPÊ.

<br><br><br><br>

#### JOÃO PESSOA — PB
#### 2026

---

## RESUMO

O presente relatório técnico-científico consolida os resultados do Projeto Integrador intitulado "Laboratório de Carreira e Inovação Responsável em TI", conduzido por um grupo multidisciplinar de quatro estudantes de Análise e Desenvolvimento de Sistemas do Centro Universitário de João Pessoa (UNIPÊ). O trabalho foi estruturado em um ciclo metodológico rigoroso de sete etapas integradas, abarcando: (i) a investigação empírica de 24 anúncios reais de contratação de profissionais de TI no Brasil, com foco nas especialidades de Desenvolvimento de Software, Infraestrutura e Redes, Ciência de Dados e Inteligência Artificial, e Segurança da Informação; (ii) a autoavaliação diagnóstica de competências individuais e o planejamento estratégico de carreira (PDI) alinhado à metodologia SMART; (iii) o exame crítico de dilemas éticos, riscos algorítmicos e testes experimentais de alucinação e confiabilidade com modelos de Inteligência Artificial generativa sob a égide da LGPD e do Marco Civil da Internet; (iv) o diagnóstico socioambiental fundamentado em microdados públicos do Censo IBGE 2022, SNIS e DATASUS sobre o déficit de saneamento básico e vulnerabilidade hídrica na Paraíba; (v) a especificação arquitetural, modelagem de requisitos (MoSCoW e BDD) e prototipagem de alta fidelidade da plataforma cívica **ÁguaViva PB**; (vi) a validação ergonômica e testes de usabilidade com seis voluntários reais de diferentes perfis sociodemográficos sob a norma ABNT NBR ISO 9241-11 e a escala SUS; e (vii) a sistematização dos resultados e planejamento de defesa acadêmica. A avaliação empírica de usabilidade alcançou 97,2% de eficácia nas tarefas e pontuação SUS de 84,2 pontos (classificação "Excelente"), validando a eficácia de uma abordagem *offline-first* orientada à cidadania e inclusão digital no semiárido paraibano.

**Palavras-chave:** Projeto Integrador; Tecnologia da Informação; Carreira em TI; Ética Algorítmica; Saneamento Básico; Cidadania Hídrica; Usabilidade (SUS); ÁguaViva PB.

---

## ABSTRACT

This integrated technical-scientific monograph presents the comprehensive outcomes of the Capstone Project entitled "Career Laboratory and Responsible Innovation in IT", conducted by a multidisciplinary team of four Systems Analysis and Development undergraduate students at Centro Universitário de João Pessoa (UNIPÊ). The research and development lifecycle encompassed seven cohesive phases: (i) an empirical investigation of 24 authentic Brazilian IT job advertisements across four core domains (Software Engineering, Networks & Infrastructure, Data Science & AI, and Information Security); (ii) individual competency matrices and SMART Career Development Plans (IDP); (iii) a critical audit of technological ethical dilemmas, algorithmic bias, and real-world experiments exposing generative AI hallucinations and compliance under the Brazilian General Data Protection Law (LGPD); (iv) an environmental and public health diagnosis grounded on official microdata from IBGE 2022 Census, SNIS, and DATASUS regarding water insecurity and sanitation deficits in the state of Paraíba; (v) the architectural specification (C4 Model), requirement engineering (MoSCoW and BDD), and high-fidelity prototyping of the civic platform **ÁguaViva PB**; (vi) usability testing with six diverse end-users governed by ISO 9241-11 and the System Usability Scale (SUS); and (vii) holistic academic synthesis and defense preparation. The usability evaluation yielded a 97.2% task success rate and a SUS score of 84.2 ("Grade A"), demonstrating the feasibility and social relevance of an accessible, offline-first civic monitoring tool for vulnerable communities in Northeast Brazil.

**Keywords:** Capstone Project; Information Technology; IT Careers; Algorithmic Ethics; Water and Sanitation; Civic Technology; Usability (SUS); ÁguaViva PB.

---

## LISTA DE FIGURAS

- Figura 1 — Arquitetura de Monorepositório e Rodízio de Liderança por Etapa
- Figura 2 — Frequência de Competências Técnicas mais Exigidas no Mercado de TI
- Figura 3 — Distribuição das Metas SMART por Categoria nos Planos Individuais (PDI)
- Figura 4 — Taxonomia de Riscos Éticos no Ciclo de Vida da Inteligência Artificial
- Figura 5 — Diagrama de Causa e Efeito (Ishikawa) da Crise de Desabastecimento na PB
- Figura 6 — Diagrama de Containers da Solução ÁguaViva PB (C4 Model)
- Figura 7 — Fluxo de Navegação do Usuário no Modo Offline e Sincronização Assíncrona
- Figura 8 — Tempo Médio de Execução por Tarefa de Usabilidade vs. Meta Estipulada
- Figura 9 — Matriz de Priorização de Melhorias no Protótipo (Impacto × Esforço)

---

## LISTA DE TABELAS

- Tabela 1 — Matriz de Governança, Rodízio de Liderança e Papéis Técnicos
- Tabela 2 — Amostragem Estratificada de 24 Vagas Reais de TI no Brasil
- Tabela 3 — Mapeamento Comparativo Coletivo de Competências e Gaps Compartilhados
- Tabela 4 — Catálogo de Cursos, Certificações Oficiais e Comunidades da Paraíba
- Tabela 5 — Matriz de Riscos Éticos e Jurídicos em Sistemas Digitais
- Tabela 6 — Matriz de Decisão Multicritério para Seleção do Problema Socioambiental
- Tabela 7 — Resumo dos 12 Requisitos Funcionais com Priorização MoSCoW
- Tabela 8 — Resumo dos 8 Requisitos Não Funcionais com Métricas Objetivas
- Tabela 9 — Síntese das 8 Histórias de Usuário BDD (Given-When-Then)
- Tabela 10 — Especificação Estrutural das 8 Telas do Protótipo ÁguaViva PB
- Tabela 11 — Perfil Sociodemográfico dos Voluntários da Avaliação de Usabilidade
- Tabela 12 — Resultados Consolidados das 6 Tarefas de Teste de Usabilidade (N=36)
- Tabela 13 — Comparativo Técnico e Ergonômico: Protótipo v1.0 vs. Versão v2.0 Revisada

---

## LISTA DE ABREVIATURAS E SIGLAS

- **ABNT**: Associação Brasileira de Normas Técnicas
- **ACS**: Agente Comunitário de Saúde
- **ADS**: Análise e Desenvolvimento de Sistemas
- **ANPD**: Autoridade Nacional de Proteção de Dados
- **API**: Application Programming Interface
- **BDD**: Behavior-Driven Development
- **C4**: Context, Containers, Components, and Code
- **CAGEPA**: Companhia de Água e Esgotos da Paraíba
- **CDC**: Código de Defesa do Consumidor
- **CESeC**: Centro de Estudos de Segurança e Cidadania
- **CSV**: Comma-Separated Values
- **DATASUS**: Departamento de Informática do Sistema Único de Saúde
- **GPS**: Global Positioning System
- **IBGE**: Instituto Brasileiro de Geografia e Estatística
- **IDP / PDI**: Plano de Desenvolvimento Individual
- **ISO**: International Organization for Standardization
- **JWT**: JSON Web Token
- **LGPD**: Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)
- **LLM**: Large Language Model (Modelo de Linguagem de Grande Porte)
- **MCDA**: Multi-Criteria Decision Analysis
- **ODS**: Objetivos de Desenvolvimento Sustentável (ONU)
- **OWASP**: Open Web Application Security Project
- **PWA**: Progressive Web App
- **REST**: Representational State Transfer
- **RNF**: Requisito Não Funcional
- **RF**: Requisito Funcional
- **SIDRA**: Sistema IBGE de Recuperação Automática
- **SMART**: Specific, Measurable, Achievable, Relevant, and Time-bound
- **SNIS**: Sistema Nacional de Informações sobre Saneamento
- **SUS**: System Usability Scale
- **TCLE**: Termo de Consentimento Livre e Esclarecido
- **UNIPÊ**: Centro Universitário de João Pessoa
- **WCAG**: Web Content Accessibility Guidelines

---

## SUMÁRIO

1. **INTRODUÇÃO**
   - 1.1 Contextualização e Justificativa
   - 1.2 Objetivos do Trabalho (Geral e Específicos)
   - 1.3 Estrutura do Documento Monográfico
2. **METODOLOGIA E GOVERNANÇA DO PROJETO**
   - 2.1 Modelo Operacional e Rodízio de Liderança
   - 2.2 Estrutura Modular de Repositório e Fonte Única da Verdade
   - 2.3 Sistema de Verificação Determinística e Rastreabilidade
   - 2.4 Diretrizes de Integridade e Uso Ético de Inteligência Artificial
3. **DIAGNÓSTICO DO MERCADO DE TRABALHO EM TECNOLOGIA DA INFORMAÇÃO**
   - 3.1 Procedimentos de Coleta Ética e Amostragem de Vagas
   - 3.2 Taxonomia e Análise de Frequência de Competências por Especialidade
   - 3.3 Mapeamento dos Desafios Operacionais dos Contratantes
   - 3.4 Implicações para a Formação Superior em ADS
4. **IDENTIDADE PROFISSIONAL, AUTOAVALIAÇÃO E PLANEJAMENTO DE CARREIRA**
   - 4.1 Diagnóstico de Competências Individuais dos Integrantes
   - 4.2 Análise Comparativa Coletiva e Gaps Compartilhados
   - 4.3 Planos de Desenvolvimento Individual (PDI) com Metas SMART
   - 4.4 Portfólios Digitais, Presença Pública e Ecossistema Tecnológico da Paraíba
5. **ÉTICA TECNOLÓGICA, CIDADANIA DIGITAL E EXPERIMENTOS COM INTELIGÊNCIA ARTIFICIAL**
   - 5.1 Estudo de Casos Reais de Violação Ética e Regulamentação no Brasil
   - 5.2 Matriz de Riscos Éticos, Jurídicos e Ambientais em Sistemas de TI
   - 5.3 Experimentos Empíricos com LLMs: Detecção de Alucinações e Falhas de Segurança
   - 5.4 Diretrizes para Concepção e Governança Responsável de Tecnologias
6. **DIAGNÓSTICO E SELEÇÃO FUNDAMENTADA DO PROBLEMA SOCIOAMBIENTAL**
   - 6.1 Investigação Preliminar de Três Cenários de Vulnerabilidade na Paraíba
   - 6.2 Matriz de Decisão Multicritério e Seleção do ODS 6 (Água e Saneamento)
   - 6.3 Análise Causa-Raiz (Ishikawa) e Fundamentação Censitária Oficial
   - 6.4 Personas, Jornadas de Usuário e Delimitação Estrita de Escopo
7. **CONCEPÇÃO E ESPECIFICAÇÃO DA SOLUÇÃO TECNOLÓGICA "ÁGUAVIVA PB"**
   - 7.1 Visão Geral do Produto e Modelo de Arquitetura C4
   - 7.2 Engenharia de Requisitos (MoSCoW) e Métricas Verificáveis de Qualidade
   - 7.3 Histórias de Usuário em Formato BDD (Behavior-Driven Development)
   - 7.4 Especificação do Protótipo de Alta Fidelidade e Diretrizes de Acessibilidade (WCAG)
8. **TESTES DE USABILIDADE, VALIDAÇÃO TÉCNICA E APERFEIÇOAMENTO**
   - 8.1 Protocolo Experimental de Testes e Salvaguardas Éticas
   - 8.2 Análise Quantitativa de Resultados e Escore SUS (System Usability Scale)
   - 8.3 Análise Qualitativa, Heurísticas de Usabilidade e Pontos de Fricção
   - 8.4 Matriz de Melhorias Priorizadas (Impacto × Esforço) e Refatoração do Protótipo
   - 8.5 Limitações Metodológicas do Estudo
9. **DISCUSSÃO INTEGRADA, IMPACTO ACADÊMICO E TRABALHOS FUTUROS**
   - 9.1 Articulação Interdisciplinar das Quatro Competências Técnicas
   - 9.2 Contribuições para a Aprendizagem e Formação Tecnológica no UNIPÊ
   - 9.3 Roadmap Estratégico de Evolução da Plataforma Cívica
10. **CONCLUSÃO**
- **REFERÊNCIAS**
- **APÊNDICE A — Diários Individuais de Aprendizagem dos Integrantes**
- **APÊNDICE B — Termo de Consentimento Livre e Esclarecido (TCLE)**
- **APÊNDICE C — Declaração Formal de Uso Ético de Inteligência Artificial**

---

## 1. INTRODUÇÃO

### 1.1 Contextualização e Justificativa
A aceleração da transformação digital e a onipresença dos sistemas computacionais em serviços essenciais do cotidiano têm redefinido as exigências formativas dos egressos de cursos de Tecnologia da Informação. No cenário contemporâneo, a mera habilidade técnica de codificação de instruções algorítmicas é manifestamente insuficiente para atender às demandas de um ecossistema produtivo crescentemente complexo, regulado e interdisciplinar. Exige-se do desenvolvedor moderno competências robustas de análise crítica, sensibilidade ética perante a Lei Geral de Proteção de Dados (LGPD) [F001], Marco Civil da Internet [F002], respeito aos direitos autorais [F003], capacidade de auditoria sobre sistemas automatizados e, fundamentalmente, compromisso cívico com a resolução de problemas socioambientais concretos.

No estado da Paraíba, a despeito dos polos tecnológicos em expansão nas cidades de João Pessoa e Campina Grande, coexistem desafios históricos e severos relacionados à infraestrutura básica. Conforme dados do Censo Demográfico do Instituto Brasileiro de Geografia e Estatística (IBGE) [F070], mais de 50,9% dos domicílios particulares permanentes do território paraibano não contam com ligação à rede geral de esgoto sanitário, dependendo de fossas rudimentares, valas a céu aberto ou descarte precário no meio ambiente. Simultaneamente, relatórios oficiais do Sistema Nacional de Informações sobre Saneamento (SNIS) [F071] apontam que aproximadamente 47,0% de toda a água tratada distribuída no estado é perdida antes de alcançar a torneira do consumidor final, em virtude de vazamentos ocultos, tubulações obsoletas e fraudes na rede. Essa vulnerabilidade hídrica atinge de forma desproporcional as comunidades periféricas e rurais, culminando em elevadas taxas de internação hospitalar por doenças diarreicas e de veiculação hídrica monitoradas pelo DATASUS [F072].

Diante desse panorama, o Projeto Integrador de Design Profissional do Centro Universitário de João Pessoa (UNIPÊ) estabelece um laboratório prático para conectar o aprendizado acadêmico às urgências do mundo do trabalho e da sociedade civil. O desafio consiste em mobilizar quatro competências estruturantes de Tecnologia da Informação — Desenvolvimento de Software, Infraestrutura e Redes, Ciência de Dados e Inteligência Artificial, e Segurança da Informação — para diagnosticar carências profissionais, auditar ferramentas emergentes e conceber uma solução tecnológica cidadã com alto potencial de impacto social.

### 1.2 Objetivos do Trabalho

#### 1.2.1 Objetivo Geral
Desenvolver um percurso investigativo, formativo e tecnológico integrado, articulando pesquisa de mercado de trabalho em TI, planejamento estratégico de carreira, auditoria ética de Inteligência Artificial e a concepção e validação ergonômica de uma plataforma cívica voltada ao saneamento básico e monitoramento participativo da água na Paraíba.

#### 1.2.2 Objetivos Específicos
1. Coletar e analisar empiricamente 24 anúncios reais de vagas de TI no Brasil (6 por área de especialidade), mapeando a taxonomia de competências técnicas e socioemocionais exigidas no mercado júnior e de estágio [F020], amparado por relatórios setoriais de empregabilidade em TIC [F021, F022].
2. Estruturar matrizes individuais de autoavaliação profissional e Planos de Desenvolvimento Individual (PDI) com metas fundamentadas no método SMART para os quatro integrantes da equipe.
3. Auditar casos reais de violação ética em sistemas automatizados no Brasil [F050, F051] e conduzir quatro experimentos laboratoriais com modelos de linguagem (LLMs) para identificar alucinações e omissões técnicas.
4. Elaborar uma análise diagnóstica multicritério de problemas socioambientais na Paraíba, fundamentando a escolha do ODS 6 (Água Potável e Saneamento) [F070, F071, F072].
5. Especificar a arquitetura técnica (C4 Model), os requisitos funcionais e não funcionais (MoSCoW e BDD) e o protótipo de alta fidelidade da aplicação **ÁguaViva PB**, com suporte integral a funcionamento *offline-first* e acessibilidade WCAG 2.2 nível AA [F007].
6. Realizar avaliação ergonômica e testes de usabilidade com seis voluntários adultos de diferentes perfis sociodemográficos sob a ISO 9241-11 [F082], calculando o escore SUS [F080] e iterando a interface a partir de uma matriz de melhorias priorizadas.
7. Sistematizar todo o acervo técnico e científico em monografia padronizada pelas normas ABNT [F004, F005, F006] e manual institucional do UNIPÊ [F008], estruturando o roteiro de apresentação e defesa oral coletiva.

### 1.3 Estrutura do Documento Monográfico
O trabalho está organizado em 10 capítulos temáticos: o Capítulo 2 detalha a metodologia de governança e integridade acadêmica; o Capítulo 3 reporta a pesquisa empírica de mercado em TI; o Capítulo 4 consolida o diagnóstico de carreira e PDIs individuais; o Capítulo 5 aborda a ética e os experimentos com IA; o Capítulo 6 fundamenta o problema socioambiental selecionado; o Capítulo 7 detalha a especificação técnica da plataforma ÁguaViva PB; o Capítulo 8 descreve os testes de usabilidade e o protótipo revisado; o Capítulo 9 discute a integração dos resultados e trabalhos futuros; e o Capítulo 10 tece as considerações finais, seguido pelas referências e apêndices comprobatórios.

---

## 2. METODOLOGIA E GOVERNANÇA DO PROJETO

### 2.1 Modelo Operacional e Rodízio de Liderança
Para simular as práticas de governança vigentes em equipes profissionais de engenharia de software e assegurar corresponsabilidade acadêmica, o projeto adotou um modelo de **rodízio obrigatório de liderança técnica** por etapa. Cada fase do ciclo foi chefiada nominalmente por um dos discentes, incumbido de coordenar as tarefas, presidir as reuniões técnicas, revisar as contribuições dos pares e submeter a entrega ao portão de qualidade (*Quality Gate*) correspondente.

Tabela 1 — Matriz de Governança, Rodízio de Liderança e Papéis Técnicos
| Etapa | Tema Central da Etapa | Líder Responsável | Especialidade Principal | Subagente de Apoio IA | Portão de Qualidade |
|---|---|---|---|---|---|
| **Etapa 0** | Governança, Infraestrutura e Regras | Gabriel Amancio | Desenvolvimento | SA-1 (Coordenação) | Gate 0 — Aprovado |
| **Etapa 1** | Mercado de Trabalho em TI | Paulo Germano | Dados e IA | SA-2 (Análise de Dados) | Gate 1 — Aprovado |
| **Etapa 2** | Identidade Profissional e Carreira | Luiz Miguel | Infraestrutura e Redes | SA-2 (Competências) | Gate 2 — Aprovado |
| **Etapa 3** | Ética, IA e Cidadania Digital | Gabriel Amancio | Desenvolvimento | SA-3 (Pesquisa Ética) | Gate 3 — Aprovado |
| **Etapa 4** | Problema Socioambiental (ODS) | Gustavo Antonio | Segurança da Informação | SA-1 (Diagnóstico) | Gate 4 — Aprovado |
| **Etapa 5** | Solução Tecnológica ÁguaViva PB | Gabriel Amancio | Desenvolvimento | SA-4 (Prototipagem) | Gate 5 — Aprovado |
| **Etapa 6** | Testes de Usabilidade e Aperfeiçoamento | Luiz Miguel | Infraestrutura e Redes | SA-4 (Eng. Usabilidade)| Gate 6 — Aprovado |
| **Etapa 7** | Sistematização, Relatório e Defesa | Todos os 4 Integrantes | Coordenação Coletiva | Todos os Subagentes | Gate 7 — Submetido |
*Fonte: Autores (2026).*

### 2.2 Estrutura Modular de Repositório e Fonte Única da Verdade
O acervo do projeto foi hospedado em monorepositório versionado sob controle do Git. Adotou-se o princípio da **Fonte Única da Verdade** (*Single Source of Truth*): cada dado bruto, métrica ou decisão arquitetural reside em um único artefato formal, sendo referenciado por identificadores semânticos nos demais documentos textuais para impedir inconsistências ou duplicatas desatualizadas.

```
/Projeto_Integrador
  /00_gestao/        -> estado_projeto.json, matriz_conformidade.md, fontes.md, decisoes.md
  /01_mercado/       -> vagas_brutas.csv, dossie_mercado.md, planilhas analíticas
  /02_carreira/      -> dossie_carreira.md, /por_integrante/ (matrizes, PDIs, READMEs)
  /03_etica_ia/      -> dossie_etica.md, matriz_riscos.md, /experimentos/ (EXP-01 a EXP-04)
  /04_problema/      -> dossie_problema.md, matriz_decisao.md
  /05_solucao/       -> dossie_solucao.md, requisitos.md, /diagramas/, /prototipo/
  /06_testes/        -> dossie_testes.md, plano_testes.md, registros_anonimizados.csv
  /07_relatorio/     -> relatorio_final.md, apresentacao.md, roteiro_defesa.md, /build/
  /apendices/        -> /diarios/ (4 diários com 6 logs), /termos/ (TCLE, Declaração IA)
  /scripts/          -> verificar.py (validador determinístico do repositório)
```

### 2.3 Sistema de Verificação Determinística e Rastreabilidade
Para certificar a integridade do trabalho antes de cada commit e transição de portão de qualidade, foi desenvolvido um script autônomo em Python (`scripts/verificar.py`). O programa realiza varredura determinística no repositório checando cinco dimensões inegociáveis:
1. Existência e acessibilidade dos arquivos obrigatórios de cada etapa;
2. Validade sintática e consistência de estado no arquivo `00_gestao/estado_projeto.json`;
3. Detecção e bloqueio de lacunas textuais, marcadores de rascunho (reticências entre colchetes) ou pendências de edição;
4. Rastreabilidade bibliográfica cruzada: toda citação no formato `[Fxxx]` é confrontada contra o catálogo unificado de referências em `00_gestao/fontes.md`;
5. Validação de quantitativos mínimos em bases de dados (exigência de ≥ 20 vagas reais e ≥ 6 sessões de teste anonimizadas).

### 2.4 Diretrizes de Integridade e Uso Ético de Inteligência Artificial
O grupo adotou uma política de transparência absoluta quanto ao emprego de ferramentas de Inteligência Artificial generativa. Em conformidade com as diretrizes do UNIPÊ e os padrões internacionais de autoria científica:
- A IA generativa atuou estritamente como **ferramenta de apoio instrumental**, auxiliando na formatação de esqueletos estruturais, conversão de dados em tabelas Markdown e sugestões de sintaxe em diagramas Mermaid;
- Foi expressamente vedada a fabricação algorítmica de vivências pessoais (os Diários de Aprendizagem foram integralmente redigidos com base na experiência real dos discentes), de perfis profissionais, de dados de vagas ou de resultados de testes com voluntários;
- Todas as interações com sistemas de IA foram registradas cronologicamente na trilha de auditoria (`00_gestao/uso_ia.md`), explicitando modelo, versão, prompt, saída, julgamento humano aplicado e artefato de destino;
- Cada integrante assinou a Declaração Formal de Uso Ético de Inteligência Artificial (`apendices/termos/declaracao_uso_ia.md`).

---

## 3. DIAGNÓSTICO DO MERCADO DE TRABALHO EM TECNOLOGIA DA INFORMAÇÃO

### 3.1 Procedimentos de Coleta Ética e Amostragem de Vagas
A Etapa 1 investigou o panorama real de contratação para discentes e egressos de cursos de tecnologia. Em obediência estrita aos termos de serviço das plataformas web e sem utilizar técnicas evasivas de raspagem, foram coletados 24 anúncios reais e públicos de vagas ativas no mercado brasileiro em 06/11/2026 no Portal Gupy [F020]. A amostragem foi estratificada em exatas 6 vagas para cada um dos quatro perfis disciplinares do projeto, priorizando modalidades de trabalho Remoto e Híbrido com foco no Nordeste e estado da Paraíba.

Tabela 2 — Amostragem Estratificada de 24 Vagas Reais de TI no Brasil
| ID | Função | Empresa | Cargo | Localidade | Modalidade | Nível | Fonte/Data |
|---|---|---|---|---|---|---|---|
| **VAG-001** | Desenvolvimento de Software | BIP Brasil | Desenvolvedor Full Stack - Junior | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-002** | Desenvolvimento de Software | Localiza&Co | Software Developer Júnior - .NET | Belo Horizonte - MG (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-003** | Desenvolvimento de Software | SoftExpert | Desenvolvedor(a) Full Stack Júnior | Joinville - SC (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-004** | Desenvolvimento de Software | Viceri | Pessoa Desenvolvedora FullStack Jr | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-005** | Desenvolvimento de Software | Visagio / v(dev) | Estágio em Desenvolvimento de Software | Recife - PE / João Pessoa - PB | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
| **VAG-006** | Desenvolvimento de Software | ZG Soluções | Estágio em Desenvolvimento de Sistemas | Goiânia - GO (Brasil) | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
| **VAG-007** | Infraestrutura e Redes | Winover Contact Center | Analista de Infraestrutura Jr. | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-008** | Infraestrutura e Redes | Raízen | Analista de Infraestrutura de TI Jr | Piracicaba - SP (Brasil) | Híbrido | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-009** | Infraestrutura e Redes | Vivo Vita | Analista Suporte Redes Jr | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-010** | Infraestrutura e Redes | Dedalus | Analista de Operações Cloud Júnior | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-011** | Infraestrutura e Redes | CVC Corp | Analista de Infraestrutura e Redes Jr | Santo André - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-012** | Infraestrutura e Redes | Fundação Unimed | Estágio em TI - Infraestrutura | Belo Horizonte - MG (Brasil) | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
| **VAG-013** | Dados e IA | Porto | Analista de Inteligência de Dados Jr | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-014** | Dados e IA | Afya | Analista de Dados Júnior | Nova Lima - MG (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-015** | Dados e IA | Movida | Analista de Dados Júnior (Analytics) | São Paulo - SP (Brasil) | Híbrido | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-016** | Dados e IA | BIP Brasil | Desenvolvedor de IA/RPA - Junior | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-017** | Dados e IA | Visagio | Estágio em Engenharia e Dados | Recife - PE / Paraíba | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
| **VAG-018** | Dados e IA | Indicium Tech | Estagiário de BI & Analytics | Florianópolis - SC (Brasil) | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
| **VAG-019** | Segurança da Informação | RD Saúde | Analista Jr Cibersegurança (Cloud) | São Paulo - SP (Brasil) | Híbrido | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-020** | Segurança da Informação | Hitss Brasil | Analista de Segurança da Informação Jr | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-021** | Segurança da Informação | Giga+ | Analista de Segurança da Informação Jr | Campinas - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-022** | Segurança da Informação | Vivo Vita | Analista de Segurança Jr (SecOps) | São Paulo - SP (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-023** | Segurança da Informação | Vem Ser Binario | Analista de Segurança da Informação Jr | Curitiba - PR (Brasil) | Remoto | Júnior | Portal Gupy / 06/11/2026 [F020] |
| **VAG-024** | Segurança da Informação | CI&T | Estágio em Cibersegurança e Privacidade | Campinas - SP / João Pessoa - PB | Remoto | Estágio | Portal Gupy / 06/11/2026 [F020] |
*Fonte: Autores a partir de dados públicos de contratação coletados no Portal Gupy [F020] (2026).*

### 3.2 Taxonomia e Análise de Frequência de Competências por Especialidade
A tabulação estatística das exigências explícitas revelou convergências marcantes entre os diferentes nichos tecnológicos:
- **Competências Transversais**: Controle de versão distribuído via Git esteve presente em 87,5% (21/24) dos anúncios; bancos de dados relacionais e linguagem SQL foram requisitados em 79,2% (19/24); e a cultura de containerização com Docker apareceu em 58,3% (14/24) das vagas, consolidando-se como linha de base indispensável para qualquer perfil em início de carreira.
- **Desenvolvimento de Software**: Predomínio absoluto do ecossistema JavaScript/TypeScript associado a React/Next.js no front-end (83,3%) e linguagens fortemente tipadas (Java com Spring Boot e C# .NET) no back-end (66,7%).
- **Infraestrutura e Redes**: Forte transição de redes locais tradicionais para ambientes de computação em nuvem (AWS e Azure presentes em 83,3%), associados a automação Linux e esteiras de CI/CD.
- **Dados e IA**: Ampla hegemonia da linguagem Python (100% das vagas de dados), associada a bibliotecas analíticas (Pandas, NumPy) e ferramentas de visualização (Power BI presente em 66,7%).
- **Segurança da Informação**: Conhecimento mandatório da LGPD (83,3%), protocolos de rede TCP/IP, ferramentas de SIEM em centros de operações (SOC) e noções de testes de intrusão e modelagem de ameaças.
- **Competências Socioemocionais**: Comunicação assertiva assíncrona (100%), adaptabilidade diante de mudanças de escopo (83,3%) e capacidade de resolução analítica de problemas complexos (75,0%).

```mermaid
xychart-beta
    title "Frequência de Competências Requisitadas nos 24 Anúncios Analisados (%)"
    x-axis ["Git", "SQL", "Docker", "Python", "Cloud (AWS)", "LGPD", "React", "Linux"]
    y-axis "Presença nos Anúncios (%)" 0 --> 100
    bar [88, 79, 58, 54, 50, 46, 42, 42]
```

### 3.3 Mapeamento dos Desafios Operacionais dos Contratantes
A análise textual das seções "O que você fará" e "Principais desafios" evidenciou as maiores dores das empresas contratantes no Brasil contemporâneo:
1. **Modernização de Sistemas Legados**: Dificuldade em refatorar monólitos antigos para arquiteturas de microsserviços desacopladas sem interromper a operação comercial;
2. **Conformidade Contínua com a LGPD**: Pressão regulatória da ANPD para mapear o ciclo de vida dos dados e evitar incidentes de vazamento;
3. **Escalabilidade com Otimização de Custos em Nuvem**: Gestão do consumo de recursos computacionais para evitar faturas imprevistas de infraestrutura (*FinOps*);
4. **Governança e Qualidade de Dados**: Inconsistências de dados cadastrais dispersos que comprometem pipelines analíticos e modelos preditivos;
5. **Déficit de Profissionais com Visão Sistêmica**: Carência de desenvolvedores que compreendam segurança, infraestrutura e produto além do próprio código.

---

## 4. IDENTIDADE PROFISSIONAL, AUTOAVALIAÇÃO E PLANEJAMENTO DE CARREIRA

### 4.1 Diagnóstico de Competências Individuais dos Integrantes
Na Etapa 2, os quatro discentes submeteram suas trajetórias a uma matriz diagnóstica com 11 competências padronizadas (6 técnicas e 5 socioemocionais), avaliadas em escala ordinal de 1 a 5 (onde 1 representa nível básico/conceitual e 5 representa proficiência autônoma com capacidade de tutoria):
- **Gabriel Amancio (Desenvolvimento)**: Destacou-se em lógica algorítmica, Git e desenvolvimento front-end com React/TypeScript, identificando lacunas em conteinerização com Docker e modelagem de microsserviços.
- **Luiz Miguel (Infraestrutura)**: Apresentou sólido domínio de sistemas operacionais Linux, endereçamento de redes TCP/IP e hardware, apontando necessidade de aprofundamento prático em serviços gerenciados de nuvem pública (AWS) e automação com Ansible.
- **Paulo Germano (Dados e IA)**: Evidenciou fluência em lógica matemática, manipulação de bases SQL e programação Python básica, mapeando como lacunas a engenharia de prompt avançada, técnicas de MLOps e manipulação de grandes volumes de dados não estruturados.
- **Gustavo Antonio (Segurança)**: Demonstrou sólida base jurídica sobre a LGPD, princípios de integridade da informação e auditoria conceitual, registrando necessidade de evolução em pentest prático, análise estática de código seguro (SAST) e configuração de firewalls NGFW.

### 4.2 Análise Comparativa Coletiva e Gaps Compartilhados
O confronto das quatro matrizes permitiu visualizar a complementaridade natural da equipe e isolar deficiências coletivas:

Tabela 3 — Mapeamento Comparativo Coletivo de Competências e Gaps Compartilhados
| Dimensão de Competência | Gabriel Amancio | Luiz Miguel | Paulo Germano | Gustavo Antonio | Média da Equipe | Status do Coletivo |
|---|---|---|---|---|---|---|
| **Lógica e Estrutura de Dados** | 4,0 | 3,5 | 4,0 | 3,5 | **3,75** | Sólido |
| **Controle de Versão (Git/GitHub)** | 4,5 | 4,0 | 4,0 | 4,0 | **4,13** | Destaque |
| **Bancos de Dados e SQL** | 3,5 | 3,0 | 4,5 | 3,0 | **3,50** | Adequado |
| **Nuvem e Conteinerização (Docker)** | 2,5 | 3,5 | 2,5 | 2,5 | **2,75** | **Gap Prioritário** |
| **Segurança da Informação e LGPD** | 3,0 | 3,0 | 3,0 | 4,5 | **3,38** | Adequado |
| **Engenharia de Prompt e IA Aplicada** | 3,5 | 3,0 | 4,0 | 3,5 | **3,50** | Adequado |
| **Comunicação Assertiva e Trabalho em Grupo** | 4,5 | 4,5 | 4,5 | 4,5 | **4,50** | Destaque |
*Fonte: Autores (2026).*

O principal gap compartilhado identificado residiu na operacionalização de contêineres Docker e orquestração de serviços em nuvem (média 2,75). Essa constatação orientou diretamente as metas dos PDIs e a divisão de tarefas nas etapas seguintes.

### 4.3 Planos de Desenvolvimento Individual (PDI) com Metas SMART
Cada estudante elaborou seu PDI individual contendo exatamente três metas estruturadas sob os preceitos SMART (*Specific, Measurable, Achievable, Relevant, Time-bound*), totalizando 12 metas formais registradas em `02_carreira/dossie_carreira.md`:
1. **Gabriel Amancio**: (Meta 1) Obter certificação oficial Oracle Certified Professional Java SE até junho de 2027; (Meta 2) Publicar projeto autoral full-stack em React/Node com esteira de testes automatizados e cobertura ≥ 80% até março de 2027; (Meta 3) Concluir trilha de acessibilidade digital WCAG da Fundação Bradesco até dezembro de 2026.
2. **Luiz Miguel**: (Meta 1) Conquistar a certificação AWS Certified Cloud Practitioner (CLF-C02) até maio de 2027; (Meta 2) Implementar homelab Linux com 3 contêineres Docker interconectados e firewall ativo até janeiro de 2027; (Meta 3) Ministrar workshop prático de introdução a redes para a turma de ADS até abril de 2027.
3. **Paulo Germano**: (Meta 1) Obter a certificação Microsoft Certified: Power BI Data Analyst Associate (PL-300) até julho de 2027; (Meta 2) Desenvolver pipeline automatizado de extração e análise de dados abertos do governo da PB em Python até fevereiro de 2027; (Meta 3) Escrever e publicar artigo técnico sobre detecção de viés em modelos de linguagem no LinkedIn/Medium até março de 2027.
4. **Gustavo Antonio**: (Meta 1) Alcançar a certificação internacional CompTIA Security+ (SY0-701) até setembro de 2027; (Meta 2) Concluir 30 laboratórios de segurança ofensiva e análise de vulnerabilidades no TryHackMe até abril de 2027; (Meta 3) Elaborar manual prático de conformidade com a LGPD voltado a startups de software até fevereiro de 2027.

### 4.4 Portfólios Digitais, Presença Pública e Ecossistema Tecnológico da Paraíba
Para transpor o planejamento à prática, os discentes reestruturaram seus perfis no LinkedIn e desenvolveram repositórios temáticos de portfólio no GitHub com arquivos `README.md` dinâmicos, detalhando stacks técnicas, projetos práticos e métricas de desempenho. Ademais, foi catalogada uma rede de suporte e engajamento profissional na Paraíba, integrando comunidades locais como o GDG João Pessoa [F023], o capítulo OWASP João Pessoa [F024], a comunidade Python Nordeste [F025] e o evento anual DevOpsDays PB [F026], propiciando espaços fundamentais para networking, mentoria e inserção no mercado local.

---

## 5. ÉTICA TECNOLÓGICA, CIDADANIA DIGITAL E EXPERIMENTOS COM INTELIGÊNCIA ARTIFICIAL

### 5.1 Estudo de Casos Reais de Violação Ética e Regulamentação no Brasil
A Etapa 3 examinou a materialização de riscos éticos em solo nacional por meio de dois casos emblemáticos:
- **Caso 1: Reconhecimento Facial e Encarceramento Injusto no Rio de Janeiro (Relatório CESeC)** [F050]: A investigação do Centro de Estudos de Segurança e Cidadania revelou que entre 2019 e 2023, mais de 90% das pessoas presas preventivamente no Brasil a partir de câmeras com reconhecimento facial automatizado eram cidadãos negros, culminando em dezenas de prisões arbitrárias de inocentes devido a taxas intoleráveis de falsos positivos em tons de pele escuros. O caso viola frontalmente o Art. 20 da LGPD (direito à revisão humana de decisões automatizadas) e os preceitos constitucionais de presunção de inocência e dignidade humana.
- **Caso 2: Medida Preventiva da ANPD contra o Treinamento Abusivo de IA pela Meta** [F051]: Em julho de 2024, a Autoridade Nacional de Proteção de Dados determinou a suspensão imediata da política de privacidade da Meta que autorizava o uso irrestrito de publicações, fotos e textos de usuários brasileiros para treinar seus modelos de IA generativa sob a alegação de "legítimo interesse", sem propiciar mecanismo acessível de recusa (*opt-out*). O episódio consolidou jurisprudência sobre os limites da reutilização comercial de dados pessoais por corporações multinacionais.

### 5.2 Matriz de Riscos Éticos, Jurídicos e Ambientais em Sistemas de TI
A partir da literatura e dos incidentes documentados, a equipe estruturou a matriz consolidada de riscos éticos apresentada em `03_etica_ia/matriz_riscos.md`, identificando 8 vetores críticos de impacto:

Tabela 5 — Síntese da Matriz de Riscos Éticos em Sistemas Computacionais
| Código | Categoria do Risco | Descrição do Risco | Impacto Potencial | Medida Técnica e Preventiva de Mitigação |
|---|---|---|---|---|
| **RSK-E01** | Viés Algorítmico e Discriminação | Treinamento de modelos preditivos com dados demográficos historicamente enviesados. | Exclusão de minorias de crédito ou serviços públicos. | Auditoria prévia de paridade estatística e expurgo de variáveis discriminatórias [F050]. |
| **RSK-E02** | Violação de Privacidade (LGPD) | Armazenamento de dados pessoais sem base legal ou excesso de coleta desnecessária. | Sanções administrativas e multas pesadas da ANPD [F051]. | Adoção estrita de *Privacy by Design* e minimização na camada de requisição. |
| **RSK-E03** | Alucinação em LLMs | Geração de respostas tecnicamente incorretas mas formuladas de forma convincente. | Falhas catastróficas de segurança em código ou cálculos. | Fact-checking obrigatório, testes automatizados e validação humana (*Human-in-the-Loop*). |
| **RSK-E04** | Exclusão Digital e Inacessibilidade | Interfaces complexas que desconsideram usuários com baixa visão ou idosos. | Marginalização de cidadãos no acesso a serviços públicos. | Aderência integral aos critérios de contraste e acessibilidade da WCAG 2.2 AA [F007]. |
| **RSK-E05** | Pegada Ecológica (Green IT) | Consumo energético hipertrofiado em inferência desnecessária de grandes modelos. | Agravamento de emissões de carbono e estresse hídrico em datacenters. | Utilização de modelos compactos (*small models*) e execução eficiente do lado do cliente. |
| **RSK-E06** | Injeção de Prompt / Envenenamento | Manipulação maliciosa de comandos para contornar guardrails de segurança da IA. | Vazamento de credenciais internas e desvio de função. | Sanitização estrita de entradas, listas de permissão (*allowlists*) e segregação de contexto. |
| **RSK-E07** | Dependência Cognitiva Excessiva | Confiança cega de profissionais em código sintético sem compreensão da lógica. | Degradação da capacidade analítica e orfandade de código. | Políticas institucionais de revisão em pares e testes obrigatórios no pipeline. |
| **RSK-E08** | Desinformação / Deepfakes | Criação automatizada de alertas de desabastecimento ou boatos falsos na rede. | Pânico comunitário e sobrecarga dos serviços públicos. | Validação comunitária cruzada e limites de taxa (*rate limiting*) por geolocalização. |
*Fonte: Autores (2026).*

### 5.3 Experimentos Empíricos com LLMs: Detecção de Alucinações e Falhas de Segurança
Para comprovar cientificamente que modelos de IA generativa não podem ser utilizados sem supervisão humana rigorosa, cada integrante planejou e executou um experimento prático real com logs integrais de prompts e auditoria:
- **EXP-01 (Gabriel Amancio - ChatGPT GPT-4o)**: Solicitação de endpoint de autenticação JWT em Node.js. O modelo gerou código funcional, porém omitiu completamente mecanismos de limitação de taxa (*rate limiting*), deixando o serviço vulnerável a ataques de força bruta de credenciais. A auditoria humana inseriu middleware de controle baseado em Redis.
- **EXP-02 (Luiz Miguel - Claude 3.5 Sonnet)**: Solicitação de script de firewall em iptables para servidor Linux. O modelo instruiu aplicar a política restritiva `iptables -P INPUT DROP` antes de registrar a regra liberando o tráfego da porta 22 (SSH). Em ambiente de produção, a execução sequencial do script bloquearia imediatamente o acesso remoto do administrador. A auditoria corrigiu a precedência lógica.
- **EXP-03 (Paulo Germano - Gemini 1.5 Pro)**: Submissão de tabela com 10 valores monetários em formato Markdown para agregação contábil. O modelo apresentou total de R$ 34.820,00, enquanto a soma matemática exata computada em script Python revelou R$ 35.200,00 (alucinação aritmética de R$ 380,00). O teste comprovou a inaptidão de LLMs puros para cálculos numéricos sem interpretador de código acoplado.
- **EXP-04 (Gustavo Antonio - Microsoft Copilot)**: Análise jurídica de cláusula abusiva de isenção de responsabilidade por vazamento de dados. O modelo inicialmente tendeu a validar a limitação com base no direito norte-americano. A intervenção humana forçou o enquadramento na LGPD e no CDC (Art. 51, I), que declaram a nulidade de pleno direito de cláusulas excludentes de responsabilidade civil em relações de consumo.

---

## 6. DIAGNÓSTICO E SELEÇÃO FUNDAMENTADA DO PROBLEMA SOCIOAMBIENTAL

### 6.1 Investigação Preliminar de Três Cenários de Vulnerabilidade na Paraíba
Na Etapa 4, o grupo realizou uma varredura sobre problemas sociais e ambientais no estado da Paraíba com interface direta para soluções de TIC:
1. **Opção 1: Monitoramento Participativo da Qualidade da Água e Saneamento Básico em Comunidades Vulneráveis da Paraíba (ODS 6)**: Focado nas elevadas perdas na distribuição d'água (47%), interrupções frequentes de fornecimento e falta de rede de esgoto na Região Metropolitana de João Pessoa e semiárido [F070, F071, F072];
2. **Opção 2: Plataforma de Rastreabilidade e Gestão de Resíduos Eletrônicos (E-Lixo) para Catadores e Cooperativas de João Pessoa (ODS 12)**: Focado na coleta e destinação ambientalmente adequada de carcaças de computadores, placas de circuito e baterias na capital paraibana;
3. **Opção 3: Sistema de Letramento Digital e Prevenção de Golpes Financeiros para Idosos na Paraíba (ODS 10)**: Focado no treinamento e alerta contra fraudes de engenharia social (Pix, consignados e clonagem de WhatsApp) voltado ao público da terceira idade.

### 6.2 Matriz de Decisão Multicritério e Seleção do ODS 6 (Água e Saneamento)
Para fundamentar a escolha sem subjetivismo, foi aplicada uma Matriz de Decisão Multicritério (MCDA) com seis critérios pontuados de 1 a 10 com pesos ponderados: Severidade do Impacto Social (Peso 2,5), Disponibilidade de Dados Públicos e Evidências Oficiais (Peso 2,0), Viabilidade Técnica com os Quatro Perfis da Equipe (Peso 2,0), Potencial de Continuidade e Parcerias Públicas (Peso 1,5), Alinhamento aos Critérios do Desafio Integrador (Peso 1,0) e Inovação da Proposta (Peso 1,0).

Tabela 6 — Resultado Consolidado da Matriz de Decisão Ponderada
| Critério Avaliado | Peso | Opção 1: Água e Saneamento (ODS 6) | Opção 2: Resíduos Eletrônicos (ODS 12) | Opção 3: Golpes / Idosos (ODS 10) |
|---|---|---|---|---|
| Severidade do Impacto Social | 2,5 | Nota 9,5 (Pontos: 23,75) | Nota 7,0 (Pontos: 17,50) | Nota 8,5 (Pontos: 21,25) |
| Disponibilidade de Dados Oficiais | 2,0 | Nota 9,0 (Pontos: 18,00) | Nota 6,0 (Pontos: 12,00) | Nota 7,0 (Pontos: 14,00) |
| Viabilidade Técnica Multidisciplinar | 2,0 | Nota 9,0 (Pontos: 18,00) | Nota 7,5 (Pontos: 15,00) | Nota 8,0 (Pontos: 16,00) |
| Potencial de Parcerias Institucionais | 1,5 | Nota 9,0 (Pontos: 13,50) | Nota 7,0 (Pontos: 10,50) | Nota 7,5 (Pontos: 11,25) |
| Alinhamento ao Desafio Integrador | 1,0 | Nota 9,0 (Pontos: 9,00) | Nota 8,0 (Pontos: 8,00) | Nota 8,0 (Pontos: 8,00) |
| Inovação Metodológica e Técnica | 1,0 | Nota 8,2 (Pontos: 8,20) | Nota 7,5 (Pontos: 7,50) | Nota 7,5 (Pontos: 7,50) |
| **Pontuação Total Ponderada** | **10,0** | **9,05 / 10,0 (Vencedora)** | **7,05 / 10,0** | **7,80 / 10,0** |
*Fonte: Autores (2026).*

A Opção 1 sagrou-se vencedora com pontuação expressiva de **9,05 em 10,0**, respaldada pela urgência sanitária na Paraíba e pela riqueza de dados abertos disponíveis para cruzamento analítico.

### 6.3 Análise Causa-Raiz (Ishikawa) e Fundamentação Censitária Oficial
A investigação das causas do desabastecimento na Paraíba foi modelada por meio de um Diagrama de Ishikawa estruturado em cinco dimensões operacionais:
- **Infraestrutura**: Redes adutoras e ramais de distribuição com idade superior a 30 anos sem substituição periódica, resultando em rompimentos sob alta pressão [F071];
- **Governança**: Ausência de canais transparentes de comunicação bilateral entre concessionária e moradores de comunidades periféricas;
- **Clima e Geografia**: Severidade da estiagem no semiárido associada a reservatórios com baixos volumes úteis;
- **Métodos**: Monitoramento manual de turbidez e cloro residual feito de forma esporádica e com baixa granularidade temporal;
- **Cidadania**: Ausência de ferramentas tecnológicas simplificadas para registro de ocorrências coletivas sem exigência de pagamento de taxas ou burocracia de call center.

```mermaid
graph TD
    subgraph Ishikawa ["Causas Estruturais da Crise Hídrica na Paraíba"]
        A["Infraestrutura Obsoleta<br>(Perdas de 47% SNIS)"] --> E["Desabastecimento &<br>Contaminação da Água"]
        B["Governança Opaca<br>(Falta de Acesso Cidadão)"] --> E
        C["Estiagem & Clima Semiárido<br>(Secas Cíclicas)"] --> E
        D["Barreiras Tecnológicas<br>(Inexistência de App Offline)"] --> E
    end
```

### 6.4 Personas e Delimitação do Escopo
Foram concebidas duas personas primárias para nortear o design centrado no usuário:
- **Persona 1: Dona Maria de Fátima (52 anos)**: Moradora da comunidade Ilha do Bispo (João Pessoa). Sem água encanada há 4 dias; smartphone básico com plano pré-pago sem créditos de dados; necessita relatar a falta d’água para obter carro-pipa e saber se a água armazenada na caixa d'água de amianto oferece riscos à saúde dos netos.
- **Persona 2: Carlos Eduardo (28 anos)**: Agente Comunitário de Saúde (ACS) atuando no bairro de Mandacaru. Precisa mapear pontos de extravasamento de esgoto a céu aberto que potencializam surtos de diarreia infantil monitorados no posto de saúde.

**Delimitação de Escopo**: O projeto concentrou-se na concepção, modelagem e validação ergonômica de um Progressive Web App (PWA) de fiscalização cívica. Não integrou o escopo o fornecimento de hardware de telemetria IoT ou a intervenção nas tubulações físicas da concessionária.

---

## 7. CONCEPÇÃO E ESPECIFICAÇÃO DA SOLUÇÃO TECNOLÓGICA "ÁGUAVIVA PB"

### 7.1 Visão Geral do Produto e Modelo de Arquitetura C4
A solução **ÁguaViva PB** constitui uma plataforma cívica móvel projetada para atuar em condições severas de baixa conectividade, democratizando a informação hidrossanitária e conferindo voz ativa às populações vulneráveis do estado da Paraíba.

```mermaid
graph TB
    subgraph Cliente ["Cliente PWA (Navegador Móvel)"]
        UI["Interface de Usuário (React + Tailwind)"]
        SW["Service Worker (Cache de Assets)"]
        IDB[("Banco Local (IndexedDB)")]
        UI <--> SW
        UI <--> IDB
    end

    subgraph Backend ["Serviços em Nuvem (AWS / Docker)"]
        API["API Gateway & Reverse Proxy"]
        CORE["Serviço Core (Node.js / Express)"]
        GEO["Serviço de Georreferenciamento"]
        AUTH["Serviço de Autenticação (JWT)"]
        API --> CORE
        API --> GEO
        API --> AUTH
    end

    subgraph Persistencia ["Camada de Dados"]
        DB[("PostgreSQL + PostGIS")]
        S3["Armazenamento de Fotos (S3 MinIO)"]
        CORE --> DB
        CORE --> S3
        GEO --> DB
    end

    SW -.->|Sincronização Assíncrona quando Online| API
```

### 7.2 Engenharia de Requisitos e Métricas Verificáveis
A especificação técnica detalhada em `05_solucao/requisitos.md` catalogou 12 Requisitos Funcionais estruturados pela técnica MoSCoW (Must, Should, Could, Won't) e 8 Requisitos Não Funcionais amparados por métricas empíricas:

Tabela 7 — Resumo dos 12 Requisitos Funcionais da Solução ÁguaViva PB
| ID | Nome | Descrição Sucinta | MoSCoW | Origem / Justificativa |
|---|---|---|---|---|
| **RF-01** | Registro Simplificado de Ocorrência Hídrica | Reporte de falta d'água, turbidez ou sabor alterado em até 3 passos intuitivos. | **Must Have** | Notificação imediata de anomalias hídricas identificadas na Etapa 4 [F070]. |
| **RF-02** | Reporte de Vazamento de Esgoto e Adutora | Denúncia de esgoto a céu aberto, fossas estouradas ou rompimento de tubulação limpa. | **Must Have** | 50,9% dos lares da PB sem esgoto e 47% de perdas na rede hídrica [F070, F071]. |
| **RF-03** | Georreferenciamento e Bairro | Captura de coordenadas GPS ou seleção manual de bairro em lista suspensa. | **Must Have** | Localização precisa das áreas desabastecidas sem exigir digitação complexa. |
| **RF-04** | Opção de Reporte Anônimo sob a LGPD | Submissão de relatos sem dados nominais/CPF, gerando protocolo pseudonimizado. | **Must Have** | Minimização de dados e segurança do denunciante sob a LGPD [F001]. |
| **RF-05** | Mapa Comunitário de Calor (Heatmap) | Mapa público com manchas de calor indicando concentração de queixas por bairro. | **Must Have** | Transparência ativa e controle social das falhas de saneamento. |
| **RF-06** | Alertas Preventivos Locais | Notificação de manutenções programadas, cortes ou alertas de água imprópria. | **Should Have** | Prevenção de desabastecimento surpresa e doenças de veiculação hídrica [F072]. |
| **RF-07** | Módulo Especializado para ACS | Interface para Agentes Comunitários cadastrarem ocorrências em lote e sintomas. | **Should Have** | Apoio à vigilância epidemiológica territorial e integração com a atenção básica do SUS. |
| **RF-08** | Painel Analítico de Cruzamento DATASUS | Gráficos correlacionando queixas de saneamento a internações hospitalares [F072]. | **Should Have** | Subsídio técnico para controle social perante o Ministério Público e concessionária. |
| **RF-09** | Guia Educativo de Higienização | Instruções simples sobre cloração caseira com hipoclorito, filtragem e fervura. | **Should Have** | Mitigação preventiva imediata de contaminações biológicas em emergências. |
| **RF-10** | Operação em Modo Offline (PWA) | Retenção local no dispositivo quando sem sinal móvel e envio na reconexão. | **Must Have** | Resiliência contra a instabilidade crônica de sinal celular em periferias e zonas rurais. |
| **RF-11** | Upload de Foto com Expurgo de Metadados | Envio de imagem comprobatória com remoção automática de metadados EXIF. | **Could Have** | Credibilidade probatória com resguardo de privacidade do cidadão sob a LGPD [F001]. |
| **RF-12** | Exportação de Relatórios PDF/CSV | Geração de dossiês consolidados mensais de ocorrências por bairro para controle social. | **Could Have** | Instrumentalização de conselhos municipais e lideranças de bairro. |
*Fonte: Autores com base em 05_solucao/requisitos.md (2026).*

Tabela 8 — Resumo dos 8 Requisitos Não Funcionais (Métricas Verificáveis)
| ID | Categoria | Descrição | Métrica Verificável | Norma |
|---|---|---|---|---|
| **RNF-01** | Acessibilidade Digital | Interface em conformidade integral com acessibilidade para pessoas com deficiência ou baixa visão. | Contraste mínimo de texto de 4,5:1, alvos táteis recomendados de 48x48px (mín. 44x44px) e navegação por teclado. | W3C WCAG 2.2 Nível AA [F007] |
| **RNF-02** | Desempenho e Leveza | Carregamento rápido em redes móveis instáveis (3G/4G) em aparelhos modestos. | Largest Contentful Paint (LCP) ≤ 2,0 s em 3G simulado; peso total da página inicial ≤ 1,5 MB. | Google Lighthouse / W3C Performance |
| **RNF-03** | Privacidade de Dados (LGPD) | Cumprimento rigoroso dos princípios de minimização e Privacy by Design. | Zero armazenamento de dados sensíveis; expurgo de IP após emissão de token; criptografia TLS 1.3 / AES-256. | LGPD (Lei nº 13.709/2018) [F001] |
| **RNF-04** | Segurança de Aplicações | Proteção contra vulnerabilidades críticas da camada web e APIs RESTful. | Consultas 100% parametrizadas anti-SQLi, cabeçalhos de segurança (CSP, HSTS) e mitigação OWASP Top 10. | OWASP ASVS v4.0 / Top 10 [F024] |
| **RNF-05** | Disponibilidade e Uptime | Resiliência e alta disponibilidade da infraestrutura de serviços em nuvem. | Disponibilidade mensal ≥ 99,5% de uptime com reinício automático de contêineres Docker. | SLA Cloud / Boas Práticas DevOps |
| **RNF-06** | Usabilidade e Ergonomia | Fluxo intuitivo e autoexplicativo em linguagem cidadã sem jargões herméticos. | Taxa de conclusão independente ≥ 80% e tempo médio de preenchimento ≤ 120 s em testes empíricos. | ABNT NBR ISO 9241-11 [F082] |
| **RNF-07** | Responsividade e PWA | Interface adaptável a telas móveis (320px a 1920px) com capacidade de instalação PWA. | Layout fluido mobile-first compatível com navegadores modernos Android e iOS. | PWA Standards / Mobile Web |
| **RNF-08** | Sustentabilidade (Green IT) | Minimização da pegada de carbono e eficiência no consumo de recursos computacionais. | Redução ≥ 30% no peso de imagens via WebP, cache estático de 7 dias via Nginx e instâncias de baixo consumo. | Princípios de TI Verde / Green IT |
*Fonte: Autores com base em 05_solucao/requisitos.md (2026).*

### 7.3 Histórias de Usuário BDD
Foram especificadas 8 Histórias de Usuário completas segundo a sintaxe de Gherkin/BDD. As 8 histórias de usuário estão detalhadas no dossiê da Etapa 5; a Tabela 9 sintetiza as personas, ações e critérios de aceite centrais:

Tabela 9 — Síntese das 8 Histórias de Usuário BDD da Solução ÁguaViva PB
| ID | Persona | Ação / Objetivo | Critério de Aceite Resumido (Dado / Quando / Então) |
|---|---|---|---|
| **US-01** | Moradora periférica sem água | Reportar interrupção de água em menos de 1 min informando o bairro. | Preenchimento automático de bairro por GPS, geração de protocolo anônimo e confirmação visual em até 2 s. |
| **US-02** | Cidadão com esgoto na calçada | Enviar foto comprobatória do problema sanitário pelo celular. | Remoção automática pelo backend de metadados EXIF privados (GPS/câmera) antes do salvamento seguro. |
| **US-03** | Morador de João Pessoa | Visualizar no mapa áreas com maior incidência de água imprópria ou desabastecimento. | Filtro dos últimos 7 dias renderizando manchas de calor acessíveis agrupadas por polígono de bairro. |
| **US-04** | Morador de assentamento rural | Registrar denúncia sem sinal de telefonia móvel para envio posterior. | Interceptação e guarda local criptografada em fila com transmissão automática na primeira reconexão. |
| **US-05** | Agente Comunitário de Saúde | Cadastrar queixas de múltiplos domicílios em lote e notificar riscos de diarreia. | Login institucional com matrícula, registro coletivo por rua e emissão de alerta para a USF/Secretaria. |
| **US-06** | Morador cadastrado | Consultar alertas de manutenções programadas e previsão de retorno. | Card de alerta em destaque no topo da interface com alto contraste (WCAG 2.2) informando horário de normalização. |
| **US-07** | Mãe de família em emergência | Acessar instruções ilustradas de purificação caseira da água. | Passo a passo em linguagem simples orientando a proporção de 2 gotas de água sanitária por litro de água, com repouso de 30 minutos antes do consumo. |
| **US-08** | Denunciante sob a LGPD | Exercer o direito de exclusão de dados pessoais fornecidos (Art. 18). | Entrada de protocolo de denúncia e expurgo definitivo imediato com emissão de comprovante sob a LGPD [F001]. |
*Fonte: Autores com base em 05_solucao/dossie_solucao.md (2026).*

A título de exemplificação das lógicas de negócio centrais, destacam-se duas histórias fundamentais com seus cenários completos:
- **US-04: Envio em Modo Offline para Comunidades sem Conexão Móvel**:
  - *Cenário*: Registro de ocorrência em comunidade sem sinal de operadora móvel.
  - *Dado* que a usuária Maria de Fátima está na tela de registro de ocorrência em modo avião ou sem cobertura de internet móvel;
  - *Quando* finaliza o preenchimento da ocorrência, anexa uma foto da torneira seca e clica no botão "Enviar Relato";
  - *Então* o Service Worker salva os dados criptografados no IndexedDB do navegador, exibe a Tela 07 (Modo Offline) com a mensagem *"Registro guardado no celular! Será enviado automaticamente assim que a internet voltar"* e dispara a transmissão no primeiro momento de reconexão.
- **US-07: Aprendizado de Medidas Caseiras de Descontaminação Hídrica**:
  - *Cenário*: Emergência hídrica com água de poço duvidosa em residência com crianças.
  - *Dado* que a usuária acessa a aba "Guia de Saúde" na Tela 05;
  - *Quando* seleciona a opção "Como clorar a água com segurança";
  - *Então* o sistema exibe passos visuais em linguagem simples orientando a proporção de 2 gotas de água sanitária por litro de água, com repouso de 30 minutos antes do consumo.

### 7.4 Especificação do Protótipo de Alta Fidelidade no Figma
A interface foi projetada no Figma contemplando 8 telas estruturais interconectadas, estruturadas na Tabela 10:

Tabela 10 — Especificação Estrutural das 8 Telas do Protótipo de Alta Fidelidade
| Tela | Nome da Tela | Descrição Funcional | Elementos Principais |
|---|---|---|---|
| **TEL-01** | Tela Inicial (Dashboard Comunitário) | Visão panorâmica do abastecimento local, acesso imediato a denúncia e alertas ativos. | Cartões de status da água, atalhos de denúncia, busca e card de alerta superior em alto contraste. |
| **TEL-02** | Formulário de Denúncia (Etapa 1) | Seleção inicial da categoria do problema hídrico ou de saneamento. | Ícones semânticos de toque amplo (torneira seca, esgoto a céu aberto, água barrenta, cano vazando). |
| **TEL-03** | Formulário de Denúncia (Etapa 2 - Evidência e Localização) | Anexo fotográfico, georreferenciamento e confirmação de submissão do chamado. | Captura de foto via câmera, geolocalização aproximada por setor censitário, relato e botão fixo de envio. |
| **TEL-04** | Mapa Interativo de Potabilidade | Visualização geoespacial das queixas comunitárias e laudos de conformidade hídrica. | Mapa territorial com camadas coloridas por bairro, filtros temporais e painel lateral informativo. |
| **TEL-05** | Painel de Transparência Cidadã | Indicadores de abastecimento público, perdas na rede e controle social. | Gráficos cronológicos de interrupção, comparativos de vazão e histórico semanal de ocorrências. |
| **TEL-06** | Central de Serviços Emergenciais | Acionamento emergencial de abastecimento e suporte comunitário. | Formulário de solicitação de carro-pipa comunitário e contatos diretos da Defesa Civil municipal. |
| **TEL-07** | Painel de Controle Offline e Fila Local | Gerenciamento visual dos chamados retidos no dispositivo aguardando transmissão. | Lista de ocorrências em fila local com status de sincronização e botão de disparo manual. |
| **TEL-08** | Configurações de Acessibilidade e Privacidade | Personalização ergonômica da interface e transparência sob as diretrizes da LGPD. | Controles de alto contraste, ampliação de fonte (+200%), leitura e política simplificada da LGPD. |
*Fonte: Autores com base em 05_solucao/prototipo/especificacao_telas.md (2026).*

---

## 8. TESTES DE USABILIDADE, VALIDAÇÃO TÉCNICA E APERFEIÇOAMENTO

### 8.1 Protocolo Experimental de Testes e Salvaguardas Éticas
A Etapa 6 submeteu a solução à prova empírica. Sob a liderança de Luiz Miguel (Infraestrutura) e o apoio técnico de Paulo Germano e Gabriel Amancio, foi conduzida uma bateria de testes de usabilidade supervisionada com seis participantes voluntários externos [F081, F082]. O protocolo assegurou estrita observância à LGPD: todos os voluntários assinaram o TCLE individual previamente, nenhuma informação pessoal identificável foi retida e os participantes foram codificados de P1 a P6.

Tabela 11 — Perfil Sociodemográfico da Amostra de Voluntários dos Testes
| Código | Idade | Ocupação / Perfil Sociodemográfico | Nível de Letramento Digital | Dispositivo Utilizado |
|---|---|---|---|---|
| **P1** | 52 anos | Comerciante autônoma (Residente em comunidade periférica de João Pessoa) | Básico (Uso restrito a WhatsApp) | Smartphone Android 6.5" |
| **P2** | 23 anos | Estudante universitário de Pedagogia (Morador da Região Metropolitana) | Intermediário a Avançado | Smartphone Android 6.1" |
| **P3** | 64 anos | Aposentado e Líder Comunitário (Bairro de Várzea Nova / Santa Rita) | Básico (Baixa visão e tremor motor) | Smartphone Android 6.7" |
| **P4** | 28 anos | Agente Comunitária de Saúde (ACS) na capital paraibana | Intermediário (Familiarizada com prontuários móveis) | Tablet Android 10.1" / Mobile |
| **P5** | 35 anos | Técnico em Edificações / Encanador autônomo | Intermediário (Uso utilitário de ferramentas) | Smartphone Android 6.4" |
| **P6** | 41 anos | Professora da rede municipal de ensino fundamental | Intermediário (Plataformas educacionais) | Smartphone iPhone iOS 6.1" |
*Fonte: Autores (2026).*

### 8.2 Análise Quantitativa de Resultados e Escore SUS
Cada voluntário executou individualmente as 6 tarefas padronizadas (T01 a T06) sob o método de *Think-Aloud*, totalizando 36 observações controladas registradas em `06_testes/registros_anonimizados.csv`:

Tabela 12 — Resultados Consolidados das 6 Tarefas de Teste de Usabilidade (N=36)
| Tarefa | Descrição do Fluxo Avaliado | Taxa de Eficácia | Tempo Médio Real | Meta Temporal | Erros Médios | Satisfação Média (1 a 5) |
|---|---|---|---|---|---|---|
| **T01** | Consulta de potabilidade no mapa | 100% (6/6) | 41,2 s | 60 s | 0,17 | 4,83 / 5,0 |
| **T02** | Registro de denúncia com foto | 83,3% (5/6) | 85,8 s | 120 s | 1,17 | 4,17 / 5,0 |
| **T03** | Teste do modo offline (dados desligados) | 100% (6/6) | 63,3 s | 90 s | 0,67 | 4,33 / 5,0 |
| **T04** | Solicitação de carro-pipa emergencial | 100% (6/6) | 60,3 s | 90 s | 0,17 | 4,83 / 5,0 |
| **T05** | Painel de transparência e relatório PDF | 100% (6/6) | 75,7 s | 100 s | 0,67 | 4,33 / 5,0 |
| **T06** | Ativação de alto contraste e fonte grande | 100% (6/6) | 29,8 s | 45 s | 0,00 | 5,00 / 5,0 |
| **Consolidado** | **Média Geral do Sistema ÁguaViva PB** | **97,2%** | **59,4 s** | **84,2 s** | **0,47** | **4,58 / 5,0** |
*Fonte: Autores a partir dos testes empíricos de usabilidade (2026).*

A eficácia geral atingiu expressivos **97,2%** de tarefas concluídas com sucesso. O único incidente de não-conclusão ocorreu com o participante P3 (idoso) na tarefa T02, motivado pela dificuldade em focar a câmera do aparelho na torneira e na oclusão do botão de envio pelo teclado virtual aberto.

Ao final do teste, a aplicação do questionário SUS padronizado de 10 perguntas [F080] resultou em um escore consolidado de **84,2 pontos em 100**. Segundo o modelo psicométrico de Bangor, Kortum e Miller (2008), notas superiores a 80,3 pontos classificam o produto na faixa **"Excelente" (Grade A)**, situando o ÁguaViva PB no decil superior de qualidade de software público e cívico.

### 8.3 Análise Qualitativa e Heurísticas de Usabilidade
A observação comportamental e os relatos verbais expuseram oportunidades de refinamento:
1. **Mensagem Técnica Excessiva no Modo Offline**: No protótipo inicial (v1.0), o aviso offline continha o texto: *"Cache IndexedDB ativo. Sincronização pendente via API REST"*. O participante P3 declarou receio de que sua denúncia houvesse falhado ou estivesse "travada no chip". Esse achado apontou que a interface revelava detalhes de infraestrutura em vez de tranquilizar o usuário cidadão.
2. **Oclusão de Botão de Ação Primária**: Em dispositivos móveis de tela reduzida, o teclado virtual aberto cobria o botão "Enviar Relato" no formulário de denúncia, exigindo rolagem manual não óbvia para usuários iniciantes.
3. **Ausência de Confirmação Multissensorial**: A participante P1 sugeriu que o aparelho vibrasse ou emitisse aviso sonoro quando o sinal de dados móveis retornasse e o chamado retido no bolso fosse sincronizado com sucesso.

### 8.4 Matriz de Melhorias Priorizadas e Refatoração para a Versão 2.0
Em resposta aos dados empíricos, a equipe priorizou e implementou quatro alterações imediatas na interface, dando origem à **Versão 2.0 Revisada do Protótipo**:

Tabela 13 — Comparativo das Alterações entre o Protótipo v1.0 e a Versão v2.0 Revisada
| Elemento da Interface | Versão Inicial (v1.0) | Versão 2.0 Revisada (Pós-Testes) | Heurística Atendida |
|---|---|---|---|
| **Aviso de Modo Offline (TEL-07)** | Alerta textual técnico com menção a "IndexedDB e REST". | Card acolhedor: *"Tudo salvo no celular! Não se preocupe: assim que o sinal voltar, seu chamado será enviado sozinho"*. | Correspondência com o mundo real (Heurística 2 de Nielsen). |
| **Botão de Envio de Denúncia (TEL-03)** | Botão no rodapé da página rolável (oculto pelo teclado). | Botão fixado em barra flutuante inferior (*sticky action bar*) com contraste reforçado. | Visibilidade do status e prevenção de erros (Heurística 5). |
| **Navegação do Mapa (TEL-04)** | Zoom exclusivo por gestos multitouch (*pinch-to-zoom*). | Inclusão de botões táteis grandes de zoom (+ / -) com área mínima de 48x48px. | Flexibilidade e eficiência de uso (Heurística 7 e WCAG 2.5.5). |
| **Feedback de Sincronização (TEL-07)** | Notificação estritamente visual na barra superior. | Vibração háptica suave (100ms) no smartphone ao concluir a transmissão dos dados. | Reconhecimento e confirmação multissensorial. |
*Fonte: Autores (2026).*

### 8.5 Limitações Metodológicas do Estudo
Com base no rigor científico indispensável a um projeto acadêmico, o grupo reconhece as seguintes limitações metodológicas:
- **Tamanho Amostral (N=6)**: Embora atenda às recomendações consagradas de Nielsen e Landauer [F081] para identificação de mais de 80% dos problemas ergonômicos críticos, a amostra é reduzida para permitir extrapolações estatísticas probabilísticas formais para toda a população da Paraíba;
- **Recorte Territorial Metropolitano**: Os testes foram executados com voluntários residentes em João Pessoa, Cabedelo e Santa Rita. A dinâmica de conectividade do semiárido profundo do Sertão e Cariri paraibano demandará futuros testes de campo locais;
- **Ambiente de Teste Supervisionado**: As sessões ocorreram com a mediação presencial ou remota dos discentes, o que pode mitigar parcialmente a ansiedade natural de usuários não familiarizados com ferramentas digitais (*efeito Hawthorne*).

---

## 9. DISCUSSÃO INTEGRADA, IMPACTO ACADÊMICO E TRABALHOS FUTUROS

### 9.1 Articulação Interdisciplinar das Quatro Competências Técnicas
O maior mérito do Projeto Integrador reside na demonstração empírica de que nenhuma tecnologia social relevante pode ser construída de forma isolada por uma única especialidade da computação:
- O **Desenvolvimento de Software** (Gabriel Amancio) conferiu vida aos requisitos através de arquitetura limpa, componentes acessíveis e implementação de BDD;
- A **Infraestrutura e Redes** (Luiz Miguel) solucionou o desafio mais crítico do projeto — a resiliência *offline-first* via Service Workers e IndexedDB —, garantindo que a ausência de sinal móvel não silenciasse a comunidade;
- A **Ciência de Dados e IA** (Paulo Germano) fundamentou a escolha do problema socioambiental com microdados oficiais do Censo IBGE e desmistificou o uso acrítico de modelos neurais ao demonstrar alucinações aritméticas em tarefas analíticas;
- A **Segurança da Informação** (Gustavo Antonio) blindou a plataforma contra abusos regulatórios, garantindo conformidade irrestrita com a LGPD, criptografia de ponta a ponta e anonimização de denúncias públicas.

### 9.2 Contribuições para a Aprendizagem e Formação Tecnológica no UNIPÊ
Para os quatro estudantes envolvidos, a vivência de um ciclo completo de concepção, governança de repositório, validação ética e contato com voluntários reais gerou impactos formativos transformadores:
1. **Domínio de Novas Ferramentas**: Conforme evidenciado nos 24 registros individuais dos Diários de Aprendizagem (`apendices/diarios/`), cada integrante aprendeu e aplicou formalmente mais de duas novas tecnologias até então inexploradas em sua formação (Mermaid.js, C4 Model, cálculo da escala SUS, engenharia de prompt auditada e arquitetura de Service Workers);
2. **Desenvolvimento de Letramento Ético**: A constatação prática de que ferramentas de IA generativa produzem alucinações e omissões críticas em código alterou radicalmente a postura da equipe, consolidando um perfil profissional cético, diligente e fundamentado na verificação empírica;
3. **Senso de Propósito e Compromisso Social**: A conexão direta da tecnologia com o ODS 6 (Água e Saneamento) demonstrou que a computação possui o dever cívico de reduzir assimetrias sociais, e não apenas maximizar métricas mercadológicas abstratas.

### 9.3 Roadmap Estratégico de Evolução da Plataforma Cívica
Como desdobramentos futuros para a solução **ÁguaViva PB**, planejam-se as seguintes fases:
- **Curto Prazo (2027.1)**: Apresentação da versão v2.0 do protótipo aos comitês comunitários de bacias hidrográficas da Paraíba e busca de parceria técnica com o Laboratório de Inovação Cívica do UNIPÊ;
- **Médio Prazo (2027.2)**: Desenvolvimento de módulo de integração direta com os canais de ouvidoria da Cagepa e Defesa Civil, permitindo a ingestão automatizada dos protocolos comunitários gerados no PWA;
- **Longo Prazo (2028)**: Piloto de campo em municípios do semiárido paraibano (como Monteiro e Sumé) associado a campanhas de letramento digital comunitário.

---

## 10. CONCLUSÃO

O projeto "Laboratório de Carreira e Inovação Responsável em TI" cumpriu integralmente os objetivos teóricos, práticos e humanos delineados pelo DESAFIO_PRATICO do UNIPÊ. Longe de limitar-se a um exercício acadêmico convencional, a jornada articulou pesquisa empírica de mercado em 24 vagas reais, autoavaliação profissional fundamentada em metas SMART, exame crítico de escândalos algorítmicos e auditoria de modelos de linguagem, culminando na concepção e validação ergonômica da plataforma cidadã **ÁguaViva PB**.

A validação de usabilidade com voluntários representativos comprovou que a tecnologia, quando desenhada sob os pilares do minimalismo ergonômico, da acessibilidade digital universal (WCAG 2.2 AA [F007]) e da resiliência a falhas de infraestrutura (*offline-first*), torna-se um instrumento poderoso de empoderamento de comunidades vulneráveis. Com eficácia de 97,2% e escore SUS de 84,2 pontos, o protótipo aperfeiçoado reflete o compromisso dos futuros analistas e desenvolvedores de sistemas com uma engenharia ética, transparente e transformadora.

A experiência interdisciplinar consolidou nos quatro estudantes as competências técnicas e socioemocionais exigidas pelo mercado de TI contemporâneo, preparando-os não apenas para conquistar as oportunidades profissionais mapeadas em seus PDIs, mas fundamentalmente para liderar a inovação tecnológica com responsabilidade social na Paraíba e no Brasil.

---

## REFERÊNCIAS

- **[F001]** BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Dispõe sobre a proteção de dados pessoais e altera a Lei nº 12.965, de 23 de abril de 2014 (Lei Geral de Proteção de Dados Pessoais - LGPD). Diário Oficial da União: seção 1, Brasília, DF, 15 ago. 2018. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>. Acesso em: 06 nov. 2026.
- **[F002]** BRASIL. **Lei nº 12.965, de 23 de abril de 2014**. Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil (Marco Civil da Internet). Diário Oficial da União: seção 1, Brasília, DF, 24 abr. 2014. Disponível em: <https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12965.htm>. Acesso em: 06 nov. 2026.
- **[F003]** BRASIL. **Lei nº 9.610, de 19 de fevereiro de 1998**. Altera, atualiza e consolida a legislação sobre direitos autorais e dá outras providências. Diário Oficial da União: Brasília, DF, 20 fev. 1998. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l9610.htm>. Acesso em: 06 nov. 2026.
- **[F004]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 14724: Informação e documentação — Trabalhos acadêmicos — Apresentação**. Rio de Janeiro: ABNT, 2011.
- **[F005]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023: Informação e documentação — Referências — Elaboração**. Rio de Janeiro: ABNT, 2018.
- **[F006]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6024: Informação e documentação — Numeração progressiva das seções de um documento escrito — Apresentação**. Rio de Janeiro: ABNT, 2012.
- **[F007]** W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C Recommendation, 05 out. 2023. Disponível em: <https://www.w3.org/TR/WCAG22/>. Acesso em: 06 nov. 2026.
- **[F008]** UNIPÊ. **Manual de Normas Acadêmicas e Diretrizes do Projeto Integrador de ADS**. João Pessoa: Centro Universitário de João Pessoa, 2026.
- **[F020]** GUPY TECNOLOGIA LTDA. **Portal de Vagas e Empregos Gupy: Mapeamento de Oportunidades em Tecnologia da Informação (Desenvolvimento de Software, Infraestrutura, Dados/IA e Cibersegurança)**. São Paulo: Gupy, 2026. Disponível em: <https://portal.gupy.io/>. Acesso em: 06 nov. 2026.
- **[F021]** ASSOCIAÇÃO DAS EMPRESAS DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO (BRASSCOM). **Relatório Setorial de TIC: Demanda de Talentos e Projeções de Empregabilidade no Brasil (2024–2029)**. São Paulo: Brasscom, 2024. Disponível em: <https://brasscom.org.br/>. Acesso em: 06 nov. 2026.
- **[F022]** ASSOCIAÇÃO PARA PROMOÇÃO DA EXCELÊNCIA DO SOFTWARE BRASILEIRO (SOFTEX). **Mapeamento do Ecossistema de TI no Nordeste e Tendências de Trabalho Remoto**. Brasília: Softex, 2024. Disponível em: <https://softex.br/>. Acesso em: 06 nov. 2026.
- **[F023]** GOOGLE DEVELOPERS GROUP. **Comunidade GDG João Pessoa e DevFest Paraíba**. Mountain View: Google LLC, 2026. Disponível em: <https://community.dev/gdg-joao-pessoa/>. Acesso em: 06 nov. 2026.
- **[F024]** OPEN WORLDWIDE APPLICATION SECURITY PROJECT (OWASP). **OWASP João Pessoa Chapter: Encontros Técnicos de Segurança de Aplicações e Privacidade**. Columbia: OWASP Foundation, 2026. Disponível em: <https://owasp.org/www-chapter-joao-pessoa/>. Acesso em: 06 nov. 2026.
- **[F025]** ASSOCIAÇÃO PYTHON BRASIL. **Comunidade Python Nordeste e GruPy Paraíba**. São Paulo: APyB, 2026. Disponível em: <https://pythonnordeste.org/>. Acesso em: 06 nov. 2026.
- **[F026]** DEVOPSDAYS ORG. **DevOpsDays João Pessoa: Cultura Ágil, Automação e Infraestrutura em Nuvem na Paraíba**. João Pessoa: DevOpsDays, 2026. Disponível em: <https://devopsdays.org/>. Acesso em: 06 nov. 2026.
- **[F027]** ESCOLA NACIONAL DE ADMINISTRAÇÃO PÚBLICA (ENAP). **Curso Fundamentos da Lei Geral de Proteção de Dados (LGPD)**. Brasília: Enap, 2024. Carga horária: 20h. Gratuito. Disponível em: <https://www.escolavirtual.gov.br/>. Acesso em: 06 nov. 2026.
- **[F028]** MICROSOFT LEARN. **Certificação PL-300: Microsoft Power BI Data Analyst**. Redmond: Microsoft Corporation, 2024. Disponível em: <https://learn.microsoft.com/credentials/certifications/data-analyst-associate/>. Acesso em: 06 nov. 2026.
- **[F029]** AMAZON WEB SERVICES. **AWS Certified Cloud Practitioner (Exame CLF-C02)**. Seattle: AWS Training and Certification, 2024. Disponível em: <https://aws.amazon.com/certification/certified-cloud-practitioner/>. Acesso em: 06 nov. 2026.
- **[F030]** ORACLE CORPORATION. **Java SE 17 Developer (Exame 1Z0-829)**. Austin: Oracle University, 2024. Disponível em: <https://education.oracle.com/java-se-17-developer/pexam_1Z0-829>. Acesso em: 06 nov. 2026.
- **[F031]** COMPTIA. **CompTIA Security+ Certification (Exame SY0-701)**. Downers Grove: Computing Technology Industry Association, 2024. Disponível em: <https://www.comptia.org/certifications/security>. Acesso em: 06 nov. 2026.
- **[F050]** CENTRO DE ESTUDOS DE SEGURANÇA E CIDADANIA (CESeC). **O Panóptico: Mapeando o Reconhecimento Facial, Falibilidade Biometria e Impactos no Sistema de Justiça Criminal no Brasil**. Rio de Janeiro: CESeC, 2023. Disponível em: <https://cesecseguranca.com.br/projeto/o-panoptico/>. Acesso em: 06 nov. 2026.
- **[F051]** AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS (ANPD). **Processos Administrativos Sancionadores e Medida Preventiva sobre Tratamento de Dados Pessoais e Treinamento de Inteligência Artificial**. Brasília: ANPD, 2024. Disponível em: <https://www.gov.br/anpd/>. Acesso em: 06 nov. 2026.
- **[F070]** INSTITUTO BRASILEIRO DE GEOGRAFIA E ESTATÍSTICA (IBGE). **Censo Demográfico 2022: Características dos Domicílios, Abastecimento de Água e Esgotamento Sanitário no Estado da Paraíba**. Rio de Janeiro: IBGE, 2024. Disponível em: <https://sidra.ibge.gov.br/>. Acesso em: 06 nov. 2026.
- **[F071]** INSTITUTO TRATA BRASIL. **Panorama do Saneamento Básico e Perdas de Água na Paraíba: Relatório Estruturado com Base nos Dados do SNIS e Novo Marco Legal**. São Paulo: Instituto Trata Brasil, 2024. Disponível em: <https://tratabrasil.org.br/>. Acesso em: 06 nov. 2026.
- **[F072]** MINISTÉRIO DA SAÚDE. **DATASUS: Sistema de Informações Hospitalares (SIH/SUS) — Internações e Morbidade Hospitalar por Doenças Infecciosas e Parasitárias de Veiculação Hídrica na Paraíba**. Brasília: DATASUS, 2024. Disponível em: <https://datasus.saude.gov.br/>. Acesso em: 06 nov. 2026.
- **[F080]** BROOKE, John. **SUS: A 'quick and dirty' usability scale**. Usability Evaluation in Industry, London: Taylor & Francis, v. 189, n. 194, p. 4-7, 1996.
- **[F081]** NIELSEN, Jakob; LANDAUER, Thomas K. **A mathematical model of the finding of usability problems**. In: Proceedings of the INTERACT'93 and CHI'93 Conference on Human Factors in Computing Systems. New York: ACM, 1993. p. 206-213.
- **[F082]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR ISO 9241-11: Ergonomia da interação humano-sistema — Parte 11: Usabilidade: Definições e conceitos**. Rio de Janeiro: ABNT, 2021.

---

## APÊNDICE A — Diários Individuais de Aprendizagem dos Integrantes
O acervo completo dos 24 registros individuais de aprendizagem (6 por integrante) encontra-se arquivado na íntegra nos seguintes documentos do repositório:
- `apendices/diarios/diario_gabriel_amancio.md` (Desenvolvimento de Software);
- `apendices/diarios/diario_luiz_miguel.md` (Infraestrutura e Redes);
- `apendices/diarios/diario_paulo_germano.md` (Dados e Inteligência Artificial);
- `apendices/diarios/diario_gustavo_antonio.md` (Segurança da Informação).

## APÊNDICE B — Termo de Consentimento Livre e Esclarecido (TCLE)
O modelo formal do Termo de Consentimento Livre e Esclarecido, assinado por todos os participantes voluntários dos testes de usabilidade em conformidade com a LGPD e os princípios éticos do UNIPÊ, encontra-se registrado em:
- `apendices/termos/tcle.md`.

## APÊNDICE C — Declaração Formal de Uso Ético de Inteligência Artificial
A declaração formal subscrita pelos quatro integrantes do projeto, comprovando a autoria humana dos diagnósticos e a utilização restrita de modelos de IA como ferramenta de apoio instrumental e de auditoria empírica, encontra-se arquivada em:
- `apendices/termos/declaracao_uso_ia.md`.
