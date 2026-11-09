# Gráficos Analíticos da Pesquisa de Mercado de TIC

Este diretório armazena e cataloga as especificações visuais dos quatro gráficos analíticos exigidos pelo Edital do Projeto Integrador (Etapa 1), derivados diretamente de `01_mercado/vagas_brutas.csv` e `planilha_Frequencia_por_Funcao.csv`.

---

## 1. Catálogo dos Quatro Gráficos

1. **Gráfico 01 — Frequência Geral das Competências Técnicas Mais Exigidas (Top 10)**
   - *Tipo:* Gráfico de barras verticais (`xychart-beta`).
   - *Fonte:* `planilha_Frequencia_por_Funcao.csv`.
   - *Destaques:* SQL (45,8%), Git (29,2%), Docker (25,0%), Python (20,8%), Linux (20,8%).

2. **Gráfico 02 — Distribuição das Modalidades de Contratação por Função**
   - *Tipo:* Gráfico comparativo de categorias (`xychart-beta`).
   - *Fonte:* `vagas_brutas.csv`.
   - *Destaques:* Remoto (54,2%), Híbrido (29,2%), Presencial (16,7%).

3. **Gráfico 03 — Frequência Relativa de Soft Skills nas Descrições de Vagas**
   - *Tipo:* Gráfico de distribuição percentual (`xychart-beta`).
   - *Fonte:* `planilha_Competencias_Padronizadas.csv`.
   - *Destaques:* Comunicação (62,5%), Trabalho em Equipe (54,2%), Resolução de Problemas (41,7%), Proatividade (37,5%).

4. **Gráfico 04 — Taxonomia Hierárquica de Especialidades em TIC no Brasil**
   - *Tipo:* Grafo direcionado conceitual (`graph TD`).
   - *Fonte:* `dossie_mercado.md`.
   - *Destaques:* Relações entre Desenvolvimento de Software, Infraestrutura/Redes, Dados/IA e Segurança da Informação.
