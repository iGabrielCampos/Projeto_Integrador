---
id: registro-decisoes
etapa: 0
autor: Main Agent (Orca)
data: 2026-11-06
status: ativo
---

# Registro de Decisões de Arquitetura e Governança (ADRs)

Este documento registra todas as decisões fundamentais do projeto no padrão ADR (Architecture Decision Record): Contexto, Decisão e Consequências.

---

## ADR-001: Adoção do Modelo Modular de Dossiês por Etapa e Fonte Única da Verdade

- **Data:** 2026-11-06
- **Status:** Aprovado
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio, Main Agent (Orca)

### Contexto
O projeto integrador do UNIPÊ exige rigor acadêmico, rastreabilidade de dados factuais, colaboração ativa entre 4 estudantes e integração de 7 etapas distintas. Notas soltas ou múltiplos arquivos dispersos geram inconsistências numéricas, duplicação de dados e descontrole de versões.

### Decisão
1. Cada etapa terá **exatamente um documento-mestre entregável** (`dossie_<etapa>.md`).
2. As notas de trabalho dos subagentes em `subagentes/SA-X/` são intermediárias e não constituem entregáveis finais.
3. Os dados brutos residirão exclusivamente em arquivos-fonte canônicos (ex.: `vagas_brutas.csv` e `fontes.md`). Nenhuma cifra ou percentual poderá ser inserido manualmente nos textos sem derivação direta dessas fontes.
4. O Relatório Final da Etapa 7 será montado programmaticamente pela unificação harmonizada dos dossiês-mestres via pipeline Pandoc/Markdown.

### Consequências
- **Positivas:** Rastreabilidade absoluta, eliminação de divergências numéricas, facilidade de auditoria via `verificar.py`.
- **Mitigações/Atenção:** Qualquer alteração em dados brutos exige reexecução dos scripts de verificação para atualizar os textos consolidados.

---

## ADR-002: Rodízio de Liderança e Separação entre Funções de Apoio (IA) e Autoria Humana

- **Data:** 2026-11-06
- **Status:** Aprovado
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio, Main Agent (Orca)

### Contexto
O DESAFIO_PRATICO estabelece que a IA deve atuar como catalisador de estrutura e rascunhos técnicos, mas jamais fabricar experiências vividas, diários individuais, autoavaliações, experimentos ou sessões de teste com usuários. Além disso, a liderança das etapas deve ser compartilhada e rotativa.

### Decisão
1. Subagentes (`SA-1` a `SA-4`) são papéis funcionais analíticos atribuídos ao sistema de IA para apoiar as etapas, enquanto os 4 estudantes são os autores, revisores e líderes rotativos.
2. É expressamente vedado ao orquestrador ou subagentes simular ou redigir experiências vividas de aprendizagem ou inventar participantes de testes. O orquestrador bloqueará a evolução do projeto caso evidências humanas não sejam inseridas pelos integrantes.
3. Cada entrega exige validação de no mínimo 2 pares em `revisoes.md`.

### Consequências
- **Positivas:** Conformidade com as normas acadêmicas e de integridade do UNIPÊ; garantia de autoria e defesa sólida perante a banca examinadora.
- **Mitigações/Atenção:** O avanço entre etapas dependerá estritamente do cumprimento dos checklists e das tarefas humanas.
