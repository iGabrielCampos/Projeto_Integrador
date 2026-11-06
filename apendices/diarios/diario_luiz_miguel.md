---
id: diario-luiz-miguel
integrante: Luiz Miguel
funcao: Infraestrutura e Redes
curso: ADS - Unipê
periodo: 2026.2
---

# Diário Individual de Aprendizagem: Luiz Miguel

## Registro 01: Processamento Determinístico de Dados e Automação de Planilhas
- **Data:** 2026-11-09 (Etapa 1)
- **Conhecimento desenvolvido:** Manipulação programática de tabelas de dados em CSV e integração conceitual com Google Sheets via Python padrão.
- **Importância:** Permitir o cálculo exato de frequências percentuais e rankings de competências sem distorções manuais.
- **Fontes consultadas:** Python Documentation (Módulo CSV) e documentação de fórmulas matriciais do Google Sheets.
- **Atividade prática:** Estruturação das 4 bases de dados da pesquisa de mercado (`planilha_Competencias_Padronizadas.csv`, `planilha_Frequencia_por_Funcao.csv` etc.).
- **Dificuldades:** Lidar com inconsistências de encoding (UTF-8 com e sem BOM) que causavam quebra de acentuação no Excel/Sheets.
- **Estratégias de superação:** Padronização estrita de encoding UTF-8 com sanitização automática nos scripts.
- **Resultados obtidos:** Tabelas prontas para importação direta e fórmulas de agregação consolidadas.
- **Novas ferramentas aprendidas:** Automação de CSV em Python nativo e modelagem tabular do Google Sheets.

---

## Registro 02: Planejamento Estratégico de Carreira em Infraestrutura Cloud
- **Data:** 2026-11-12 (Etapa 2)
- **Conhecimento desenvolvido:** Metodologia SMART para metas de qualificação profissional em Linux, Cloud (AWS/Azure) e Redes de Computadores.
- **Importância:** Liderança da Etapa 2 e definição do meu plano de ação para obtenção da certificação AWS Cloud Practitioner e especialização em Docker.
- **Fontes consultadas:** AWS Certified Cloud Practitioner Exam Guide e documentação de carreiras do Linux Professional Institute (LPI).
- **Atividade prática:** Elaboração do meu PDI individual com 3 metas SMART e estruturação do dossiê mestre coletivo de carreiras da equipe.
- **Dificuldades:** Estipular prazos realistas e métricas tangíveis de validação prática para competências de infraestrutura complexas.
- **Estratégias de superação:** Conexão com comunidades locais de tecnologia da Paraíba (DevOpsDays PB e GDG João Pessoa).
- **Resultados obtidos:** PDI aprovado pelo grupo e perfil profissional no LinkedIn e GitHub modernizados.
- **Novas ferramentas aprendidas:** Metodologia SMART aplicada a carreiras e GitHub Profile README dinâmico.

---

## Registro 03: Auditoria de Segurança em Scripts de Firewall Gerados por IA
- **Data:** 2026-11-15 (Etapa 3)
- **Conhecimento desenvolvido:** Análise de vulnerabilidades operacionais em scripts de rede gerados por modelos de inteligência artificial.
- **Importância:** Garantir que automações de infraestrutura e firewalls corporativos não causem bloqueios acidentais (*lockout*) de servidores remotos.
- **Fontes consultadas:** Documentação oficial do Netfilter/iptables Linux e RFC 1918.
- **Atividade prática:** Condução do Experimento EXP-02 com Claude 3.5 Sonnet, solicitando script iptables e identificando que o modelo aplicava a política DROP antes de liberar a porta 22 (SSH).
- **Dificuldades:** Explicar tecnicamente o risco da ordem sequencial das regras de firewall na documentação acadêmica.
- **Estratégias de superação:** Teste prático do fluxo lógico em máquina virtual isolada para demonstrar a perda de conectividade imediata.
- **Resultados obtidos:** Log de experimento auditado em `03_etica_ia/experimentos/experimento_02_luiz_miguel.md`.
- **Novas ferramentas aprendidas:** Depuração avançada de regras de iptables e técnicas de prompt para engenharia de infraestrutura.

---

## Registro 04: Arquitetura de Redes para Aplicações Resilientes e Modo Offline
- **Data:** 2026-11-20 (Etapa 5)
- **Conhecimento desenvolvido:** Protocolos de comunicação cliente-servidor, Service Workers, estratégias de cache *Cache-First* e bancos de dados locais IndexedDB.
- **Importância:** Garantir que o ÁguaViva PB continue funcionando mesmo em regiões com conexão móvel nula ou intermitente no semiárido paraibano.
- **Fontes consultadas:** Mozilla Developer Network (MDN Web Docs: Service Worker API e Background Sync) e Google PWA Best Practices.
- **Atividade prática:** Modelagem do container de infraestrutura da solução, especificação do Service Worker e fila assíncrona de sincronização local.
- **Dificuldades:** Definir a estratégia de resolução de conflitos de dados quando a conexão é restabelecida após longos períodos offline.
- **Estratégias de superação:** Implementação de política *Last-Write-Wins* baseada em timestamp seguro com filas segregadas por protocolo.
- **Resultados obtidos:** Diagrama de fluxo offline e requisitos RNF-02 e RNF-03 completamente fundamentados.
- **Novas ferramentas aprendidas:** Service Worker Cache Storage e IndexedDB para arquitetura offline-first.

---

## Registro 05: Liderança e Condução de Testes de Usabilidade com Escala SUS
- **Data:** 2026-11-23 (Etapa 6)
- **Conhecimento desenvolvido:** Engenharia de usabilidade segundo a ABNT NBR ISO 9241-11 e cálculo psicométrico da escala SUS de John Brooke.
- **Importância:** Liderar a Etapa 6 de validação empírica com 6 voluntários reais, mensurando a facilidade de uso do protótipo ÁguaViva PB.
- **Fontes consultadas:** John Brooke (SUS - A quick and dirty usability scale) e ABNT NBR ISO 9241-11.
- **Atividade prática:** Elaboração do plano de testes com 6 tarefas (T01 a T06), mediação das sessões de teste com voluntários reais, tabulação dos 36 registros em CSV e cálculo do escore SUS (84,2 pontos).
- **Dificuldades:** Manter a neutralidade durante os testes com voluntários idosos que hesitavam frente a jargões técnicos.
- **Estratégias de superação:** Aplicação rigorosa da técnica *Think-Aloud* sem induzir respostas ou ações dos participantes.
- **Resultados obtidos:** Dossiê de testes concluído com taxa de 97,2% de eficácia e 4 oportunidades de melhoria aplicadas no protótipo.
- **Novas ferramentas aprendidas:** Cálculo matemático de pontuação SUS e moderação de testes de usabilidade com gravação de tela.

---

## Registro 06: Planejamento de Escalabilidade e Defesa Oral da Infraestrutura
- **Data:** 2026-11-26 (Etapa 7)
- **Conhecimento desenvolvido:** Modelagem de custos operacionais de nuvem, dimensionamento de instâncias e oratória técnica para banca examinadora.
- **Importância:** Defender com segurança a sustentabilidade técnica e financeira da solução pública perante os professores avaliadores.
- **Fontes consultadas:** AWS Pricing Calculator e manuais de oratória acadêmica do UNIPÊ.
- **Atividade prática:** Redação da seção de infraestrutura no relatório integrado, preparação dos slides em Figma e elaboração das respostas técnicas para as perguntas da banca.
- **Dificuldades:** Sintetizar conceitos complexos de redes e escalabilidade em falas de 3 minutos durante a apresentação do grupo.
- **Estratégias de superação:** Simulação de banca interna cronometrada com os quatro integrantes do grupo.
- **Resultados obtidos:** Roteiro de defesa alinhado e domínio consolidado de todas as fases do projeto.
- **Novas ferramentas aprendidas:** Figma para visualização de arquitetura e cálculo de custo total de propriedade (TCO) em nuvem.
