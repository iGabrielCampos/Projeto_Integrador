---
id: registro-decisoes
etapa: 0
autor: Main Agent (Orca)
data: 2026-11-06
status: ativo
---

# Registro de Decisões de Arquitetura e Governança (ADRs)

Este documento registra as decisões do projeto no padrão ADR (Architecture Decision Record): Contexto, Decisão e Consequências.

---

## ADR-001: Adoção do Modelo Modular de Dossiês por Etapa e Fonte Única da Verdade

- **Data:** 2026-11-06
- **Status:** Aprovado
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio, Main Agent (Orca)

### Contexto
O projeto integrador reúne sete etapas com dados empíricos e trabalho conjunto de quatro estudantes. Documentos dispersos poderiam gerar inconsistências em números e versões.

### Decisão
1. Cada etapa terá um documento-mestre principal (`dossie_<etapa>.md`).
2. As notas de trabalho dos subagentes em `subagentes/SA-X/` servem como rascunhos intermediários e não são entregáveis finais.
3. Os dados brutos ficam concentrados em arquivos-fonte específicos (como `vagas_brutas.csv` e `fontes.md`). Números e percentuais nos textos devem derivar dessas bases.
4. O relatório final da Etapa 7 unifica os dossiês das etapas anteriores.

### Consequências
- **Positivas:** Melhor rastreabilidade dos dados, redução de divergências numéricas e verificação automatizada via `verificar.py`.
- **Pontos de atenção:** Qualquer alteração em dados brutos exige reexecução dos scripts de verificação para atualizar os textos consolidados.

---

## ADR-002: Rodízio de Liderança e Separação entre Funções de Apoio (IA) e Autoria Humana

- **Data:** 2026-11-06
- **Status:** Aprovado
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio, Main Agent (Orca)

### Contexto
As diretrizes do projeto acadêmico orientam o uso de IA como ferramenta de apoio para estrutura e formatação, vedando a geração artificial de experiências pessoais, autoavaliações ou testes com usuários. A liderança das etapas também deve ser rotativa.

### Decisão
1. Os subagentes (`SA-1` a `SA-4`) representam papéis funcionais do sistema de IA para apoio técnico, enquanto os quatro estudantes respondem pela autoria, liderança e revisão do trabalho.
2. É vedada a geração artificial de relatos de aprendizagem ou de participantes de testes. O avanço do projeto requer as evidências práticas registradas pelos próprios estudantes.
3. Cada entrega passa por revisão de pelo menos dois colegas em `revisoes.md`.

### Consequências
- **Positivas:** Atendimento às normas de integridade acadêmica do UNIPÊ e garantia da autoria discente nas entregas e na defesa.
- **Pontos de atenção:** O avanço entre etapas depende da conclusão prévia das atividades e registros individuais.
