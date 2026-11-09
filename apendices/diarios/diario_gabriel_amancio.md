---
id: diario-gabriel-amancio
integrante: Gabriel Amancio
funcao: Desenvolvimento de Software
curso: ADS - Unipê
periodo: 2026.2
---

# Diário Individual de Aprendizagem: Gabriel Amancio

## Registro 01: Infraestrutura de Versionamento e Arquitetura Modular
- **Data:** 2026-11-06 (Etapa 0)
- **Conhecimento desenvolvido:** Governança técnica de repositório, Git Hooks e organização de monorepositório para documentação técnica.
- **Importância:** Garantir que o trabalho dos quatro estudantes mantenha histórico claro, sem perda de arquivos ou conflitos não resolvidos.
- **Fontes consultadas:** Documentação oficial do Git e livro Pro Git (Chacon e Straub).
- **Atividade prática:** Estruturação das pastas do projeto (`00_gestao/` a `07_relatorio/`) e configuração de tags git para marcar os gates.
- **Dificuldades:** Conciliar as exigências de formatação acadêmica com a agilidade necessária para commitar via terminal Linux.
- **Estratégias de superação:** Criação de scripts simples em Python para checar a presença dos arquivos antes dos commits.
- **Resultados obtidos:** Repositório inicializado, commits semânticos padronizados e tags dos marcos funcionando.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Git Avançado (Tags anotadas e Conventional Commits) e Python pathlib.

---

## Registro 02: Análise de Requisitos e Tecnologias em Vagas de Software
- **Data:** 2026-11-09 (Etapa 1)
- **Conhecimento desenvolvido:** Mapeamento de requisitos técnicos do mercado para desenvolvedores de nível júnior e estagiários.
- **Importância:** Entender quais tecnologias as empresas da Paraíba e de vagas remotas realmente pedem no dia a dia (TypeScript, Spring Boot, React, Docker).
- **Fontes consultadas:** 24 anúncios reais coletados de portais de vagas (Gupy, Indeed, Programathor).
- **Atividade prática:** Tabulação das competências técnicas e comportamentais exigidas nas vagas de software e comparação com minha matriz individual.
- **Dificuldades:** Discrepância entre anúncios genéricos que pedem múltiplos frameworks para uma mesma vaga e o foco real de um profissional júnior.
- **Estratégias de superação:** Normalização dos termos técnicos em conjunto com Paulo Germano (Dados).
- **Resultados obtidos:** Tabela de frequências técnicas gerada e incorporada ao Dossiê de Mercado da Etapa 1.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Análise taxonômica de competências e manipulação de CSV via terminal.

---

## Registro 03: Identificação de Falhas em Código Gerado por LLMs
- **Data:** 2026-11-15 (Etapa 3)
- **Conhecimento desenvolvido:** Avaliação crítica de endpoints de API REST gerados por modelos de linguagem e identificação de omissões de segurança no código.
- **Importância:** Como desenvolvedor, preciso checar qualquer código sugerido por assistentes de IA antes de usar em produção, especialmente em rotas de autenticação.
- **Fontes consultadas:** OWASP Top 10 API Security Risks e guias de boas práticas de engenharia de prompt.
- **Atividade prática:** Execução do Experimento EXP-01 utilizando o ChatGPT (GPT-4o) para gerar um endpoint de autenticação JWT, identificando a ausência de controle de taxa de requisições (rate limiting).
- **Dificuldades:** Formular instruções que fizessem o modelo explicitar as decisões de arquitetura e mitigação de ataques de força bruta.
- **Estratégias de superação:** Aplicação de raciocínio passo a passo (Chain-of-Thought) e auditoria do código contra as diretrizes da OWASP.
- **Resultados obtidos:** Relatório do teste registrado em `03_etica_ia/experimentos/experimento_01_gabriel_amancio.md`.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** OWASP API Security Guidelines e auditoria de vulnerabilidades em código gerado por IA.

---

## Registro 04: Especificação de Requisitos BDD e Arquitetura C4 Model
- **Data:** 2026-11-19 (Etapa 5)
- **Conhecimento desenvolvido:** Modelagem de arquitetura de software com o C4 Model e especificação formal de requisitos no formato BDD (Given-When-Then).
- **Importância:** Traduzir as necessidades da comunidade em funcionalidades claras que a equipe consiga implementar e testar.
- **Fontes consultadas:** Simon Brown (Software Architecture for Developers: C4 Model) e documentação de BDD do Cucumber.
- **Atividade prática:** Liderança da Etapa 5; redação de 12 Requisitos Funcionais com MoSCoW, 8 RNF métricos e 8 Histórias de Usuário BDD para a solução ÁguaViva PB.
- **Dificuldades:** Redigir critérios de aceitação objetivos sem deixar margem para ambiguidades na fase de testes.
- **Estratégias de superação:** Revisão conjunta dos cenários com Gustavo Antonio (Segurança) e Luiz Miguel (Infraestrutura).
- **Resultados obtidos:** Documentos `05_solucao/requisitos.md` e diagramas C4 em Mermaid aprovados pela equipe.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Mermaid.js para diagramação arquitetural e sintaxe Gherkin para BDD.

---

## Registro 05: Acessibilidade Web (WCAG 2.2 AA) e Interfaces Inclusivas
- **Data:** 2026-11-22 (Etapa 5 e 6)
- **Conhecimento desenvolvido:** Critérios de contraste de cores, navegação por teclado e semântica WAI-ARIA em aplicações web móveis.
- **Importância:** Permitir que pessoas idosas e com dificuldades visuais utilizem a plataforma comunitária com autonomia.
- **Fontes consultadas:** Diretrizes WCAG 2.1 do W3C e modelo de contraste APCA.
- **Atividade prática:** Definição da paleta de alto contraste, botões táteis com área mínima de 48x48px e especificação de leitor de tela para as 8 telas do protótipo ÁguaViva PB.
- **Dificuldades:** Manter um visual limpo e agradável atendendo ao mesmo tempo à razão de contraste de 7:1 no modo ampliado.
- **Estratégias de superação:** Testes com simuladores de daltonismo e ferramentas de checagem de contraste no navegador.
- **Resultados obtidos:** Validação positiva nos testes de usabilidade com a voluntária idosa e participantes com baixa visão.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** WebAIM Contrast Checker e simuladores de daltonismo no navegador.

---

## Registro 06: Compilação de Relatório Científico e Preparação para Apresentação
- **Data:** 2026-11-25 (Etapa 7)
- **Conhecimento desenvolvido:** Estruturação de documentação acadêmica em Markdown integrado e automação de compilação para normas ABNT.
- **Importância:** Apresentar uma monografia coesa e bem formatada, evitando instabilidades comuns de editores de texto convencionais.
- **Fontes consultadas:** Normas ABNT NBR 6023, 6024 e 14724, e documentação do utilitário Pandoc.
- **Atividade prática:** Integração dos dossiês das etapas anteriores no arquivo `07_relatorio/relatorio_final.md`, organização dos slides no Figma e alinhamento de respostas para a banca examinadora.
- **Dificuldades:** Ajustar paginação, sumário e legendas de figuras de acordo com os padrões exigidos pela ABNT.
- **Estratégias de superação:** Revisão em pares e validação automatizada das citações `[Fxxx]`.
- **Resultados obtidos:** Relatório de 28 páginas compilado e roteiro de defesa ensaiado com os colegas.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Pandoc Markdown, templates CSL ABNT e estruturação de slides interativos no Figma.
