---
id: diario-luiz-miguel
integrante: Luiz Miguel
funcao: Infraestrutura e Redes
curso: ADS - Unipê
periodo: 2026.2
---

# Diário Individual de Aprendizagem: Luiz Miguel

## Registro 01: Processamento de Dados Tabulares e Automação de Planilhas
- **Data:** 2026-11-09 (Etapa 1)
- **Conhecimento desenvolvido:** Manipulação de tabelas de dados em formato CSV e integração com planilhas eletrônicas via Python.
- **Importância:** Permitir o cálculo exato de frequências percentuais e rankings de competências sem distorções manuais.
- **Fontes consultadas:** Documentação oficial do módulo csv do Python e fórmulas matriciais de planilhas eletrônicas.
- **Atividade prática:** Estruturação das 4 bases de dados da pesquisa de mercado (`planilha_Competencias_Padronizadas.csv`, `planilha_Frequencia_por_Funcao.csv` etc.).
- **Dificuldades:** Lidar com inconsistências de codificação de caracteres (UTF-8 com e sem BOM), que causavam quebra de acentos no Excel.
- **Estratégias de superação:** Padronização rigorosa do encoding UTF-8 com rotinas automáticas de sanitização nos scripts.
- **Resultados obtidos:** Tabelas prontas para importação direta e fórmulas de agregação consolidadas.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Automação de CSV em Python nativo e modelagem tabular do Google Sheets.

---

## Registro 02: Planejamento de Carreira em Infraestrutura e Cloud
- **Data:** 2026-11-12 (Etapa 2)
- **Conhecimento desenvolvido:** Metodologia SMART para metas de qualificação profissional em Linux, Cloud (AWS/Azure) e Redes de Computadores.
- **Importância:** Liderança da Etapa 2 e definição do meu plano de ação para obtenção da certificação AWS Cloud Practitioner e especialização em Linux e redes.
- **Fontes consultadas:** Guia do exame AWS Certified Cloud Practitioner e documentação de carreiras do Linux Professional Institute (LPI).
- **Atividade prática:** Elaboração do meu PDI individual com 3 metas SMART e estruturação do dossiê mestre coletivo de carreiras da equipe.
- **Dificuldades:** Estipular prazos realistas e métricas tangíveis de validação prática para competências de infraestrutura complexas.
- **Estratégias de superação:** Troca de experiências em comunidades técnicas da Paraíba (DevOpsDays PB e GDG João Pessoa).
- **Resultados obtidos:** PDI aprovado pelo grupo e perfis profissionais no LinkedIn e GitHub atualizados.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Metodologia SMART aplicada a carreiras e GitHub Profile README dinâmico.

---

## Registro 03: Identificação de Falhas em Scripts de Firewall Gerados por IA
- **Data:** 2026-11-15 (Etapa 3)
- **Conhecimento desenvolvido:** Análise de vulnerabilidades operacionais em scripts de rede gerados por modelos de inteligência artificial.
- **Importância:** Garantir que automações de infraestrutura e firewalls corporativos não causem bloqueios acidentais (lockout) de servidores remotos.
- **Fontes consultadas:** Documentação oficial do Netfilter/iptables Linux e RFC 1918.
- **Atividade prática:** Condução do Experimento EXP-02 com o Claude 3.5 Sonnet, solicitando um script iptables e identificando que o modelo aplicava a política DROP antes de liberar a porta 22 (SSH).
- **Dificuldades:** Demonstrar tecnicamente o risco da ordem sequencial das regras de firewall para os colegas do grupo.
- **Estratégias de superação:** Teste prático do fluxo lógico em máquina virtual isolada para comprovar a perda de conectividade imediata.
- **Resultados obtidos:** Registro de experimento documentado em `03_etica_ia/experimentos/experimento_02_luiz_miguel.md`.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Depuração avançada de regras de iptables e técnicas de prompt para engenharia de infraestrutura.

---

## Registro 04: Arquitetura de Redes para Aplicações Resilientes e Modo Offline
- **Data:** 2026-11-20 (Etapa 5)
- **Conhecimento desenvolvido:** Protocolos de comunicação cliente-servidor, Service Workers, estratégias de cache (Cache-First) e bancos de dados locais IndexedDB.
- **Importância:** Garantir que o ÁguaViva PB continue funcionando mesmo em regiões com conexão móvel instável ou inexistente no semiárido paraibano.
- **Fontes consultadas:** Mozilla Developer Network (MDN Web Docs: Service Worker API) e guias de boas práticas para PWAs do Google.
- **Atividade prática:** Modelagem dos componentes de rede da solução, especificação do Service Worker e fila assíncrona de sincronização local.
- **Dificuldades:** Definir a estratégia de tratamento de conflitos quando a conexão é restabelecida após longos períodos offline.
- **Estratégias de superação:** Adoção de timestamps precisos com ordenação cronológica e filas segregadas por tipo de registro.
- **Resultados obtidos:** Diagrama de fluxo offline e requisitos RNF-02 e RNF-03 completamente fundamentados.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Service Worker Cache Storage e IndexedDB para arquitetura offline-first.

---

## Registro 05: Condução de Testes de Usabilidade com a Escala SUS
- **Data:** 2026-11-23 (Etapa 6)
- **Conhecimento desenvolvido:** Engenharia de usabilidade segundo a ABNT NBR ISO 9241-11 e cálculo psicométrico da escala SUS de John Brooke.
- **Importância:** Liderar a Etapa 6 de validação com 6 voluntários reais, mensurando a facilidade de uso do protótipo ÁguaViva PB.
- **Fontes consultadas:** John Brooke (SUS: A quick and dirty usability scale) e norma ABNT NBR ISO 9241-11.
- **Atividade prática:** Elaboração do plano de testes com 6 tarefas (T01 a T06), mediação das sessões de teste com voluntários, tabulação dos 36 registros em CSV e cálculo do escore SUS (84,2 pontos).
- **Dificuldades:** Manter a neutralidade durante os testes com voluntários idosos que hesitavam frente a termos técnicos.
- **Estratégias de superação:** Aplicação cuidadosa da técnica Think-Aloud, ouvindo as impressões sem induzir ações dos participantes.
- **Resultados obtidos:** Dossiê de testes concluído com taxa de 97,2% de eficácia e 4 oportunidades de melhoria aplicadas no protótipo.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Cálculo matemático de pontuação SUS e moderação de testes de usabilidade com gravação de tela.

---

## Registro 06: Planejamento de Custos e Apresentação da Infraestrutura
- **Data:** 2026-11-26 (Etapa 7)
- **Conhecimento desenvolvido:** Estimativa de custos operacionais de nuvem, dimensionamento de instâncias e oratória técnica para banca examinadora.
- **Importância:** Defender com clareza a sustentabilidade técnica e financeira da solução pública perante os professores avaliadores.
- **Fontes consultadas:** AWS Pricing Calculator e roteiros de apresentação acadêmica do UNIPÊ.
- **Atividade prática:** Redação da seção de infraestrutura no relatório integrado, preparação dos slides em Figma e alinhamento das respostas técnicas para as perguntas da banca.
- **Dificuldades:** Sintetizar conceitos complexos de redes e escalabilidade em falas curtas durante a apresentação da equipe.
- **Estratégias de superação:** Simulação de banca interna cronometrada com os quatro integrantes do grupo.
- **Resultados obtidos:** Roteiro de defesa alinhado e domínio consolidado de todas as fases do projeto.
- **Evidências que demonstram a aprendizagem (novas ferramentas):** Figma para visualização de arquitetura e cálculo de custo total de propriedade (TCO) em nuvem.
