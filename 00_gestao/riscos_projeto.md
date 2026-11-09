---
id: riscos-projeto
etapa: 0
autor: Main Agent (Orca)
data: 2026-11-06
status: ativo
---

# Matriz de Riscos do Projeto

Este documento registra os riscos operacionais identificados durante o projeto, com probabilidade, impacto e ações de mitigação.

---

## 1. Mapeamento de Riscos e Planos de Contingência

| ID | Risco Identificado | Causa Potencial | Impacto | Prob. | Severidade | Ação Preventiva / Mitigação | Responsável |
|---|---|---|---|---|---|---|---|
| **RSK-01** | Bloqueio de coleta de dados no LinkedIn | Limitações de taxa (rate limit), antibot ou exigência de login restrito | Médio | Alta | **Alto** | Utilizar fontes públicas alternativas autorizadas (Gupy, Indeed, Vagas.com, InfoJobs, portais oficiais de carreiras de empresas), registrando sempre a URL e data. | SA-1 / Gabriel Amancio |
| **RSK-02** | Dificuldade no recrutamento de 6 voluntários para testes (Etapa 6) | Restrição de tempo ou indisponibilidade de público externo | Alto | Média | **Alto** | Iniciar o recrutamento prévio na Etapa 5; elaborar TCLE simplificado; caso necessário, recrutar colegas de outros períodos de ADS documentando a limitação amostral. | SA-4 / Luiz Miguel |
| **RSK-03** | Atraso nas entregas intermediárias por conflitos de agenda | Sobrecarga acadêmica/profissional dos 4 estudantes | Alto | Média | **Alto** | Folga de 15% embutida em cada ciclo do cronograma; acompanhamento semanal via `estado_projeto.json`; redistribuição rápida de subtarefas. | Gabriel Amancio (Coord.) |
| **RSK-04** | Divergência numérica entre relatórios e planilhas | Edição manual descompassada de valores estatísticos | Alto | Média | **Alto** | Aplicação estrita do Contrato de Dados (Fonte Única da Verdade) e execução do script determinístico `verificar.py` antes de qualquer gate. | SA-2 / Paulo Germano |
| **RSK-05** | Comprometimento da integridade acadêmica por geração excessiva de IA | Dependência de saídas automatizadas sem reflexão crítica | Crítico | Baixa | **Crítico** | Bloqueio orquestrado: diários, autoavaliações, experimentos e testes exigem execução e registro exclusivamente humano. Log em `uso_ia.md`. | Todos os Integrantes |
