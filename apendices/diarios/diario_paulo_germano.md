---
id: diario-paulo-germano
integrante: Paulo Germano
funcao: Dados e IA
curso: ADS - Unipê
periodo: 2026.2
---

# Diário Individual de Aprendizagem: Paulo Germano

## Registro 01: Amostragem Estatística e Curadoria de Vagas de TI
- **Data:** 2026-11-08 (Etapa 1)
- **Conhecimento desenvolvido:** Metodologia de amostragem estratificada para mercado de trabalho e técnicas de web scraping ético sem violação de termos de uso.
- **Importância:** Liderança da Etapa 1; assegurar que a base de 24 anúncios reais de TI fosse representativa, balanceada e auditável.
- **Fontes consultadas:** Diretrizes de raspagem de dados ética e documentação do portal Gupy e InfoJobs.
- **Atividade prática:** Coleta manual/supervisionada de 24 vagas reais de TI (6 por área: Dev, Infra, Dados e Sec) e montagem dos arquivos `vagas_brutas.json` e `vagas_brutas.csv`.
- **Dificuldades:** Evitar anúncios que exigiam login ou páginas dinâmicas que bloqueavam a visualização pública.
- **Estratégias de superação:** Filtragem estrita de páginas públicas corporativas com registro imediato de URLs, datas de acesso e cópias textuais.
- **Resultados obtidos:** Base de 24 vagas aprovada com 100% de fontes ativas e rastreáveis.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Curadoria de datasets públicos e validação de schema JSON estruturado.

---

## Registro 02: Visualização de Dados e Diagramação Declarativa com Mermaid
- **Data:** 2026-11-10 (Etapa 1 e 2)
- **Conhecimento desenvolvido:** Geração de gráficos estatísticos e fluxogramas diretamente em código Markdown utilizando Mermaid.js.
- **Importância:** Permitir que toda a documentação gráfica do projeto seja versionada no Git como texto simples, eliminando a dependência de imagens binárias opacas.
- **Fontes consultadas:** Documentação oficial do Mermaid.js (Diagramas de Barras `xychart-beta`, Grafos e Quadrantes).
- **Atividade prática:** Construção dos 4 gráficos do Dossiê de Mercado da Etapa 1 e dos diagramas de carreira da Etapa 2.
- **Dificuldades:** Limitações de formatação de rótulos com caracteres especiais no motor do Mermaid.
- **Estratégias de superação:** Ajuste de sintaxe e uso de strings delimitadas por aspas duplas nos nós do grafo.
- **Resultados obtidos:** Gráficos interativos perfeitamente renderizados no repositório.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Mermaid.js para visualização declarativa de dados estatísticos.

---

## Registro 03: Auditoria de Alucinações Aritméticas em LLMs
- **Data:** 2026-11-16 (Etapa 3)
- **Conhecimento desenvolvido:** Avaliação empírica da confiabilidade matemática de modelos de linguagem de grande porte (LLMs) em análises tabulares.
- **Importância:** Como especialista em Dados e IA, comprovar a vulnerabilidade dos modelos neurais para cálculos exatos e a necessidade de fact-checking computacional.
- **Fontes consultadas:** Artigos acadêmicos sobre *hallucinations* em LLMs (Ji et al., 2023) e documentação do Google Gemini 1.5 Pro.
- **Atividade prática:** Realização do Experimento EXP-03 submetendo tabela com 10 observações numéricas ao Gemini e descobrindo erro de soma aritmética (erro de R$ 380,00 na agregação).
- **Dificuldades:** Isolar o mecanismo de alucinação do modelo sem introduzir vieses nas instruções do prompt.
- **Estratégias de superação:** Criação de scripts comparativos em Python (`sum()` nativo) para auditar a resposta da IA com precisão matemática absoluta.
- **Resultados obtidos:** Log completo de auditoria registrado em `03_etica_ia/experimentos/experimento_03_paulo_germano.md`.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Métodos de fact-checking automatizado para saídas de IA generativa.

---

## Registro 04: Análise Censitária e Modelagem Estatística do Problema Socioambiental
- **Data:** 2026-11-18 (Etapa 4)
- **Conhecimento desenvolvido:** Extração e cruzamento de microdados demográficos e de saneamento de fontes públicas oficiais (IBGE Censo 2022, SNIS e DATASUS).
- **Importância:** Fornecer a fundamentação quantitativa incontestável para a seleção do tema de saneamento básico e qualidade da água na Paraíba (ODS 6).
- **Fontes consultadas:** API SIDRA do IBGE (Censo 2022), Painel Saneamento Brasil (Instituto Trata Brasil) e DATASUS.
- **Atividade prática:** Tabulação das taxas de ausência de rede de esgoto na Paraíba (50,9%) e índice de perda hídrica na distribuição (47,0%), subsidiando a matriz de decisão da Etapa 4.
- **Dificuldades:** Normalizar nomenclaturas entre as bases do IBGE e os relatórios operacionais do SNIS.
- **Estratégias de superação:** Criação de dicionário de correspondência de variáveis territoriais.
- **Resultados obtidos:** Matriz de decisão com pontuação ponderada comprovando a prioridade do saneamento com nota 9,05.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Consulta ao SIDRA IBGE e análise de indicadores de saúde pública no DATASUS.

---

## Registro 05: Análise Psicométrica e Tratamento dos Dados de Usabilidade
- **Data:** 2026-11-23 (Etapa 6)
- **Conhecimento desenvolvido:** Aplicação de estatística descritiva e cálculo do escore SUS (*System Usability Scale*) sobre a base de dados dos testes de interface.
- **Importância:** Transformar 36 observações empíricas em indicadores claros de eficiência e satisfação para respaldar as decisões de produto.
- **Fontes consultadas:** Sauro & Lewis (Quantifying the User Experience: Practical Statistics for User Research).
- **Atividade prática:** Processamento do arquivo `06_testes/registros_anonimizados.csv`, cálculo da média temporal (59,4s), taxa de sucesso (97,2%) e consolidação do escore SUS de 84,2 pontos.
- **Dificuldades:** Tratamento do caso de não-conclusão da tarefa T02 pelo participante P3 para não distorcer as médias ponderadas.
- **Estratégias de superação:** Segregação entre análise de intenção de uso (*Intention-to-Treat*) e tempo das tarefas concluídas com sucesso.
- **Resultados obtidos:** Tabelas e gráficos consolidados no Dossiê de Testes da Etapa 6.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Cálculo psicométrico da escala SUS e análise estatística de usabilidade.

---

## Registro 06: Integração de Dados do Relatório Monográfico e Preparação para a Defesa
- **Data:** 2026-11-26 (Etapa 7)
- **Conhecimento desenvolvido:** Redação acadêmica integrada de metodologia quantitativa e formulação de argumentos técnicos para banca avaliadora.
- **Importância:** Garantir que todos os números, tabelas e gráficos do relatório final de 28 páginas mantenham consistência cruzada absoluta.
- **Fontes consultadas:** Normas de apresentação de tabelas e gráficos do IBGE e ABNT NBR 14724.
- **Atividade prática:** Revisão final de todos os dados quantitativos inseridos no `relatorio_final.md`, redação do roteiro de apresentação em Figma e preparação das respostas para a banca.
- **Dificuldades:** Garantir que o texto acadêmico integrasse as 4 disciplinas sem soar fragmentado ou redundante.
- **Estratégias de superação:** Alinhamento contínuo em sessões diárias com os quatro integrantes.
- **Resultados obtidos:** Monografia completa aprovada sem nenhuma inconsistência factual ou numérica.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Auditoria cruzada de monografias acadêmicas e técnicas de defesa oral de dados.
