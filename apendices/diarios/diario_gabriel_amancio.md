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
- **Conhecimento desenvolvido:** Governança técnica de repositório, Git Hooks e arquitetura de monorepositório para documentação técnica.
- **Importância:** Garantir que o trabalho de 4 estudantes mantenha rastreabilidade rigorosa sem conflitos de merge ou perda de dados.
- **Fontes consultadas:** Git Documentation oficial e Pro Git Book (Chacon & Straub).
- **Atividade prática:** Estruturação da árvore de diretórios modular (`00_gestao/` a `07_relatorio/`) e configuração de tags git para cada gate do projeto.
- **Dificuldades:** Conciliar a rigidez dos critérios de conformidade acadêmica com a agilidade de versionamento no terminal Linux.
- **Estratégias de superação:** Criação de scripts determinísticos em Python para pré-validação antes dos commits.
- **Resultados obtidos:** Repositório inicializado, commits semânticos padronizados e tags semânticas ativas.
- **Novas ferramentas aprendidas:** Git Avançado (Tags anotadas e Conventional Commits) e Python pathlib.

---

## Registro 02: Análise de Requisitos e Dores de Recrutamento em Vagas de Software
- **Data:** 2026-11-09 (Etapa 1)
- **Conhecimento desenvolvido:** Mapeamento de exigências técnicas do mercado de trabalho para Desenvolvedores Júnior e Estagiários.
- **Importância:** Compreender as tecnologias reais demandadas no Nordeste e remoto (TypeScript, Spring Boot, React, Docker).
- **Fontes consultadas:** 24 anúncios reais coletados de portais corporativos (Gupy, Indeed, Programathor).
- **Atividade prática:** Tabulação das competências técnicas e socioemocionais exigidas nas vagas de software e confronto com minha matriz individual.
- **Dificuldades:** Discrepância entre anúncios genéricos que exigem múltiplos frameworks simultâneos e o foco real de um perfil Júnior.
- **Estratégias de superação:** Normalização taxonômica dos termos técnicos em colaboração com Paulo Germano (Dados).
- **Resultados obtidos:** Tabela de frequências técnicas gerada e incorporada ao Dossiê de Mercado da Etapa 1.
- **Novas ferramentas aprendidas:** Análise taxonômica de competências e manipulação de CSV via terminal.

---

## Registro 03: Diagnóstico de Alucinações em Código Gerado por LLMs
- **Data:** 2026-11-15 (Etapa 3)
- **Conhecimento desenvolvido:** Engenharia de prompt para validação de segurança de APIs REST e detecção de omissões críticas em código sintético.
- **Importância:** Como desenvolvedor, não posso confiar cegamente em códigos gerados por IA generativa sem auditoria linha a linha.
- **Fontes consultadas:** OWASP Top 10 API Security Risks e Guia de Engenharia de Prompt da Anthropic/OpenAI.
- **Atividade prática:** Execução do Experimento EXP-01 utilizando ChatGPT (GPT-4o) para gerar endpoint de autenticação JWT, identificando ausência de rate limiting.
- **Dificuldades:** Formular prompts que forçassem o modelo a explicitar as decisões de arquitetura e mitigação de força bruta.
- **Estratégias de superação:** Aplicação de técnica *Chain-of-Thought* e auditoria estrita contra as diretrizes OWASP.
- **Resultados obtidos:** Relatório prático documentado em `03_etica_ia/experimentos/exp_01_gabriel_amancio.md`.
- **Novas ferramentas aprendidas:** OWASP API Security Guidelines e auditoria de vulnerabilidades em código gerado por IA.

---

## Registro 04: Especificação de Requisitos BDD e Arquitetura C4 Model
- **Data:** 2026-11-19 (Etapa 5)
- **Conhecimento desenvolvido:** Modelagem de arquitetura de software utilizando C4 Model e especificação formal de requisitos em formato BDD (*Given-When-Then*).
- **Importância:** Essencial para transformar necessidades cívicas comunitárias em requisitos implementáveis e testáveis.
- **Fontes consultadas:** Simon Brown (Software Architecture for Developers - C4 Model) e Cucumber BDD Reference Guide.
- **Atividade prática:** Liderança da Etapa 5; redação de 12 Requisitos Funcionais com MoSCoW, 8 RNF métricos e 8 Histórias de Usuário BDD para a solução ÁguaViva PB.
- **Dificuldades:** Garantir que os critérios de aceitação fossem estritamente verificáveis sem depender de ambiguidades textuais.
- **Estratégias de superação:** Revisão cruzada com Gustavo Antonio (Segurança) e Luiz Miguel (Infraestrutura).
- **Resultados obtidos:** Documentos `05_solucao/requisitos.md` e diagramas C4 em Mermaid aprovados.
- **Novas ferramentas aprendidas:** Mermaid.js para diagramação arquitetural e sintaxe Gherkin para BDD.

---

## Registro 05: Acessibilidade Web (WCAG 2.1 AA) e Design Responsável
- **Data:** 2026-11-22 (Etapa 5 e 6)
- **Conhecimento desenvolvido:** Critérios de contraste de cores, suporte a navegação por teclado e semântica WAI-ARIA em aplicações web móveis.
- **Importância:** Permitir que pessoas idosas e com deficiência visual utilizem a plataforma cívica com autonomia.
- **Fontes consultadas:** W3C Web Content Accessibility Guidelines (WCAG) 2.1 e modelo de cores APCA.
- **Atividade prática:** Definição da paleta de alto contraste, botões táteis mínimos de 48x48px e especificação de leitor de tela para as 8 telas do protótipo ÁguaViva PB.
- **Dificuldades:** Manter uma identidade visual moderna e atrativa ao mesmo tempo em que se garante contraste rígido de 7:1 em modo ampliado.
- **Estratégias de superação:** Testes com simuladores de daltonismo e contrast checkers integrados.
- **Resultados obtidos:** Aprovação integral nos testes de usabilidade com a voluntária idosa e participantes com baixa visão.
- **Novas ferramentas aprendidas:** WebAIM Contrast Checker e simuladores de daltonismo no navegador.

---

## Registro 06: Compilação Automatizada de Relatório Científico e Apresentação
- **Data:** 2026-11-25 (Etapa 7)
- **Conhecimento desenvolvido:** Sistematização de documentação acadêmica em Markdown integrado e automação de build para normas ABNT.
- **Importância:** Apresentar uma monografia coesa, bem fundamentada e formatada sem as instabilidades de editores de texto convencionais.
- **Fontes consultadas:** Normas ABNT NBR 6023, 6024 e 14724, e documentação do motor Pandoc.
- **Atividade prática:** Integração dos 7 dossiês-mestres no `07_relatorio/relatorio_final.md`, estruturação dos slides em Figma e preparação das respostas da banca examinadora.
- **Dificuldades:** Ajustar a paginação, sumário e legendas de figuras de acordo com os padrões rigorosos da ABNT.
- **Estratégias de superação:** Revisão coletiva em pares e validação automatizada das citações `[Fxxx]`.
- **Resultados obtidos:** Relatório final de 28 páginas compilado e roteiro de defesa ensaiado.
- **Novas ferramentas aprendidas:** Pandoc Markdown, templates CSL ABNT e estruturação de slides interativos no Figma.
