# Projeto Integrador — ADS (UNIPÊ • 2026.2)

**ÁguaViva PB: Tecnologia para enfrentar a falta d'água e a exclusão digital na Paraíba**

Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas (ADS) do Centro Universitário de João Pessoa (UNIPÊ). O trabalho une pesquisa de mercado, planejamento de carreira, ética em Inteligência Artificial e o desenvolvimento de uma aplicação cidadã voltada ao **ODS 6 (Água Potável e Saneamento)**.

> [!NOTE]
> **Para testar o protótipo navegável agora:** abra [`05_solucao/prototipo/index.html`](05_solucao/prototipo/index.html) em qualquer navegador web. Ele simula denúncias sem necessidade de matrícula ou CPF, modo offline com fila local, modo de alto contraste, aumento de fonte e confirmação tátil.

---

## Integrantes do Grupo

| Integrante | Papel Principal no Projeto | Liderança por Etapa |
|---|---|---|
| **Gabriel Amancio** | Desenvolvimento de Software | Etapa 0 (Organização), Etapa 5 (Solução e Protótipo) e Etapa 7 (Consolidação) |
| **Luiz Miguel** | Infraestrutura e Redes | Etapa 2 (Carreira e PDI) e Etapa 6 (Testes com Voluntários) |
| **Paulo Germano** | Dados e Inteligência Artificial | Etapa 1 (Pesquisa de Mercado) |
| **Gustavo Antonio** | Segurança da Informação | Etapa 3 (Ética e IA) e Etapa 4 (Diagnóstico Socioambiental) |

---

## O Problema e a Nossa Solução

1. **O problema real na Paraíba:** segundo o Censo 2022 do IBGE, **50,92%** dos domicílios do estado não têm rede geral de esgoto (cerca de 1,4 milhão de pessoas em fossas simples ou valas a céu aberto, sendo 88 mil só em João Pessoa). Além disso, dados do SNIS apontam **47%** de perda de água tratada na distribuição e internações de crianças e idosos por doenças ligadas à água contaminada no DATASUS.
2. **A barreira esquecida:** os canais oficiais das concessionárias exigem o número de matrícula da conta, excluindo famílias de ocupações irregulares, além de dependerem de internet estável ou longas esperas por telefone.
3. **O que o ÁguaViva PB entrega:**
   - **Denúncia em 2 passos sem cadastro e sem CPF** (protegida pela LGPD).
   - **Modo offline no navegador:** guarda o relato no celular quando o sinal cai e envia assim que a internet voltar.
   - **Pedido de carro-pipa comunitário**, mapa por bairro e guia simples de fervura e cloração caseira da água.
   - **Acessibilidade na prática:** botões grandes (48x48 px), alto contraste e aumento de fonte, refinados após testes presenciais com **6 voluntários** de 23 a 64 anos (**97,2%** de conclusão em 36 tarefas e escore **84,2/100** na escala SUS).

---

## Estrutura do Repositório (7 Etapas + Gestão)

- [`DESAFIO_PRATICO.md`](DESAFIO_PRATICO.md) — Diretrizes oficiais da disciplina.
- [`00_gestao/`](00_gestao/) — Cronograma, decisões do grupo, fontes catalogadas (`fontes.md`), matriz de conformidade, registro de atividades e uso de IA (`uso_ia.md`).
- [`01_mercado/`](01_mercado/) — Pesquisa estratificada com **24 vagas reais** de TI (`vagas_brutas.csv` / `.json`), frequências por área e dossiê de mercado.
- [`02_carreira/`](02_carreira/) — Autoavaliações individuais, **PDIs com metas SMART** e portfólios dos quatro integrantes.
- [`03_etica_ia/`](03_etica_ia/) — Análise de dois casos éticos reais (CESeC e ANPD), matriz de 8 riscos e **4 experimentos práticos** testando limitações de LLMs.
- [`04_problema/`](04_problema/) — Estudo socioambiental na Paraíba (IBGE, SNIS, DATASUS), personas, diagrama de Ishikawa e matriz de decisão (ODS 6).
- [`05_solucao/`](05_solucao/) — 12 Requisitos Funcionais, 8 Não Funcionais, 8 Histórias de Usuário, diagramas, especificação das 8 telas e **protótipo navegável (`05_solucao/prototipo/index.html`)**.
- [`06_testes/`](06_testes/) — Plano de testes, registros anonimizados de 6 voluntários (36 observações), cálculo SUS (`84,2`), comparativo v1.0 → v2.0 e limitações metodológicas.
- [`07_relatorio/`](07_relatorio/) — Monografia completa em normas ABNT (`relatorio_final.md`, `.html`, `.pdf`), script de compilação (`build/compilar.py`), roteiro de perguntas (`roteiro_defesa.md`) e **roteiro enxuto de 8 slides para apresentação em sala de aula** (`apresentacao.md` e `slides_figma_spec.json`).
- [`apendices/`](apendices/) — 4 diários individuais de aprendizagem (24 registros ao todo), modelo de TCLE e declaração de uso ético de IA.
- [`scripts/`](scripts/) — Scripts em Python de apoio e verificação (`processar_mercado.py` e `verificar.py`).

---

## Como Verificar e Recompilar os Arquivos

Para validar a integridade do projeto (arquivos obrigatórios, fontes `[Fxxx]`, JSON de estado e ausência de pendências):

```bash
python3 scripts/verificar.py
```

Para recompilar a monografia ABNT em HTML e PDF (`07_relatorio/build/monografia_completa_abnt.*`):

```bash
bash 07_relatorio/build/build.sh
```
