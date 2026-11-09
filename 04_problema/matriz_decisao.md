---
id: matriz-decisao-problema
etapa: 4
autor: Gustavo Antonio, Gabriel Amancio, Paulo Germano, Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F070
  - F071
  - F072
---

# Matriz Comparativa de Decisão para Seleção do Problema Socioambiental

Esta matriz avalia as três alternativas de problemas socioambientais investigadas pela equipe técnica, fundamentando a escolha prioritária com base em critérios técnicos, operacionais, regulatórios e de relevância pública no estado da Paraíba.

---

## 1. Problemas Socioambientais Investigados

1. **Problema A (ODS 6 - Água Potável e Saneamento Básico):** Ineficiência no monitoramento da qualidade da água potável, histórico crítico de interrupções no fornecimento e descarte inadequado de esgoto em comunidades periféricas e rurais da Paraíba `[F070]`, `[F071]`.
2. **Problema B (ODS 2 e ODS 12 - Fome Zero e Consumo Responsável):** Desperdício de alimentos na cadeia de hortifrúti e barreiras logísticas de intermediação entre produtores/varejistas e cozinhas comunitárias/bancos de alimentos em João Pessoa.
3. **Problema C (ODS 11 e ODS 13 - Cidades Sustentáveis e Ação Climática):** Vulnerabilidade a desastres hidrometeorológicos, alagamentos urbanos e deslizamento de encostas em comunidades ribeirinhas e encostas da capital paraibana.

---

## 2. Critérios de Avaliação e Pesos Atribuídos

| Critério de Decisão | Peso | Descrição do Critério |
|---|---|---|
| **C1. Relevância e Impacto Social** | 25% | Gravidade do problema na Paraíba, contingente populacional impactado e alinhamento com os ODS da ONU. |
| **C2. Viabilidade Técnica em ADS** | 25% | Aderência aos conhecimentos de software, APIs, bancos de dados e interfaces desenvolvidos pelo grupo no UNIPÊ. |
| **C3. Acessibilidade e Inclusão Digital** | 20% | Capacidade da solução tecnológica atender cidadãos de baixa renda, idosos e pessoas com deficiência sob diretrizes WCAG `[F007]`. |
| **C4. Sustentabilidade Operacional** | 15% | Viabilidade de manutenção com baixo custo de infraestrutura em nuvem (Green IT) e baixa dependência de hardware proprietário. |
| **C5. Riscos Regulatórios e LGPD** | 15% | Complexidade de governança de dados pessoais, consentimento e conformidade com a Lei nº 13.709/2018 `[F001]`. |

---

## 3. Matriz Ponderada de Pontuação (Escala de 1 a 10)

| Problema Socioambiental | C1: Relevância (25%) | C2: Viabilidade (25%) | C3: Acessibilidade (20%) | C4: Sustentabilidade (15%) | C5: Riscos LGPD (15%) | Nota Final Ponderada | Classificação |
|---|---|---|---|---|---|---|---|
| **Problema A: Qualidade da Água e Saneamento (ODS 6)** | **9,5** (2,375) | **9,0** (2,250) | **9,0** (1,800) | **8,5** (1,275) | **9,0** (1,350) | **9,05** | **1º Lugar (Selecionado)** |
| **Problema B: Desperdício de Alimentos (ODS 2/12)** | 8,5 (2,125) | 8,0 (2,000) | 8,0 (1,600) | 8,0 (1,200) | 8,5 (1,275) | 8,20 | 2º Lugar |
| **Problema C: Alagamentos e Encostas (ODS 11/13)** | 9,0 (2,250) | 6,5 (1,625) | 7,5 (1,500) | 7,0 (1,050) | 8,0 (1,200) | 7,625 | 3º Lugar |

---

## 4. Justificativa Técnica da Seleção

O **Problema A (Monitoramento da Qualidade da Água e Saneamento Básico)** obteve a pontuação ponderada de **9,05 pontos**, selecionado pelos seguintes fatores:
1. **Gravidade dos Indicadores Oficiais:** O Censo 2022 do IBGE `[F070]` registrou que 50,92% dos lares paraibanos não possuem rede geral de esgoto e 8 dos 10 municípios com abastecimento mais precário do Brasil situam-se na Paraíba. Além disso, as perdas físicas na distribuição alcançam 47% `[F071]`.
2. **Aderência ao Perfil Técnico da Equipe:** O tema possibilita integrar o desenvolvimento de interfaces acessíveis (Gabriel - Dev), consultas espaciais e correlação com o DATASUS `[F072]` (Paulo - Dados), infraestrutura de baixo consumo computacional (Luiz - Infra) e governança de dados anônimos sob a LGPD (Gustavo - Segurança).
3. **Viabilidade Operacional Frente às Alternativas:** O Problema C demandaria sensores físicos geotécnicos e pluviométricos de alto custo, enquanto o Problema B envolveria logística física de transporte refrigerado de perecíveis fora do escopo de software. O Problema A concentra-se em coleta comunitária de dados, georreferenciamento e inteligência analítica em saúde pública.
