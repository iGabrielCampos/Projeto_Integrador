---
id: registro-decisoes
etapa: 0
autor: Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio
data: 2026-11-06
status: ativo
---

# Registro de Decisões do Projeto

## Decisão 01: Organização Modular por Etapas e Dados Centralizados
- **Data:** 2026-11-06
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio
- **Motivo:** Como o projeto tem sete etapas integradas feitas por quatro pessoas, arquivos separados sem padrão poderiam gerar números diferentes entre as planilhas e o relatório final.
- **O que definimos:** Cada etapa tem sua pasta com um dossiê principal (`dossie_<etapa>.md`), os dados brutos ficam em arquivos CSV (`vagas_brutas.csv`, `registros_anonimizados.csv`) e o catálogo de referências fica centralizado em `00_gestao/fontes.md`.

## Decisão 02: Rodízio de Liderança e Autoria Coletiva
- **Data:** 2026-11-06
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio
- **Motivo:** Atender à exigência do projeto de alternar a coordenação entre os integrantes e garantir que todos participem das análises, do protótipo e da apresentação em sala.
- **O que definimos:** Cada etapa teve um líder responsável pela coordenação e revisão junto aos demais colegas. Os diários individuais, autoavaliações e registros de testes refletem exclusivamente as atividades reais conduzidas pela equipe.

## Decisão 03: Escopo Realista de Protótipo Web Leve (HTML/CSS/JS)
- **Data:** 2026-11-19
- **Decisores:** Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio
- **Motivo:** Para a realidade do curso e da apresentação em sala, o foco é demonstrar claramente o fluxo de denúncia acessível e o funcionamento offline simulado sem complicar o protótipo com infraestrutura pesada fora do escopo acadêmico.
- **O que definimos:** Entregar um protótipo navegável direto em navegador (`05_solucao/prototipo/index.html`) cobrindo as 8 telas especificadas, acompanhado de modelagem simplificada de como seria a versão em produção como Progressive Web App (PWA).
