---
id: roteiro-apresentacao-slides
etapa: 7
titulo: Roteiro e Script de Apresentação Oral em Slides (Figma / Slides)
projeto: Laboratório de Carreira e Inovação Responsável em TI - ÁguaViva PB
instituicao: UNIPÊ - Centro Universitário de João Pessoa
curso: CST em Análise e Desenvolvimento de Sistemas
equipe:
  - Gabriel Amancio (Desenvolvimento de Software)
  - Luiz Miguel (Infraestrutura e Redes)
  - Paulo Germano (Dados e IA)
  - Gustavo Antonio (Segurança da Informação)
tempo_total_estimado: "25 a 30 minutos (21 min de slides + 5 a 7 min de demonstração do protótipo) + 10 min de arguição"
ferramenta_slides: Figma / Google Slides
---

# Roteiro Oficial de Apresentação e Script de Defesa Oral

## Estrutura da Apresentação (Divisão Equitativa de Falas — 12 Slides)

| Slide | Bloco Temático | Orador Titular | Tempo Alocado | Foco do Conteúdo |
|---|---|---|---|---|
| **01** | Capa e Identificação Institucional | Paulo Germano | 1 min | Apresentação da equipe, curso, instituição e título |
| **02** | Contextualização e Justificativa | Paulo Germano | 1,5 min | Desafios de saneamento na PB e metas formativas |
| **03** | Governança e Metodologia | Gabriel Amancio | 1,5 min | Rodízio de liderança, monorepositório e scripts |
| **04** | Pesquisa de Mercado (24 Vagas) | Paulo Germano | 2 min | Análise de vagas, competências mais frequentes |
| **05** | Identidade, Autoavaliação e PDI | Luiz Miguel | 2 min | Matrizes individuais, gaps de nuvem e metas SMART |
| **06** | Ética Tecnológica, Casos Reais e LGPD | Gustavo Antonio | 2 min | Caso CESeC, medida da ANPD e matriz de 8 riscos |
| **07** | Diagnóstico Socioambiental (ODS 6) | Gustavo Antonio | 2 min | Ishikawa e matriz multicritério com dados do Censo |
| **08** | Solução ÁguaViva PB (Arquitetura) | Gabriel Amancio | 2 min | C4 Model, PWA offline-first e requisitos MoSCoW |
| **09** | Demonstração do Protótipo (Telas e Fluxo) | Gabriel Amancio | 2 min | Telas principais (`TEL-01` a `TEL-08`), denúncia, mapa e acessibilidade |
| **10** | Testes de Usabilidade e Escala SUS | Luiz Miguel | 2 min | 36 sessões, eficácia de 97,2% e SUS de 84,2 pontos |
| **11** | Matriz de Melhorias e Protótipo v2 | Luiz Miguel | 1,5 min | Correções pós-teste e humanização de avisos |
| **12** | Conclusão, Impacto e Roadmap | Todos | 1,5 min | Aprendizados dos 4 integrantes e próximos passos |

---

## Script Detalhado por Slide

### Slide 01: Abertura e Apresentação da Equipe
- **Visual no Figma**: Logo institucional do UNIPÊ, título do projeto em destaque (*Laboratório de Carreira e Inovação Responsável em TI: Solução ÁguaViva PB*), foto e nome dos quatro discentes com suas respectivas áreas de atuação em ADS.
- **Orador**: Paulo Germano (1 minuto).
- **Fala oral sugerida**:
  > *"Boa noite aos professores da banca avaliadora, aos colegas e a todos os presentes. Somos discentes do curso de Análise e Desenvolvimento de Sistemas do UNIPÊ. O grupo é formado por Gabriel Amancio, na área de Desenvolvimento de Software; Luiz Miguel, em Infraestrutura e Redes; eu, Paulo Germano, em Dados e Inteligência Artificial; e Gustavo Antonio, em Segurança da Informação. Hoje apresentamos o resultado do nosso Projeto de Design Profissional, no qual relacionamos as demandas reais do mercado de trabalho em TI ao desenvolvimento de uma aplicação voltada aos problemas de saneamento e abastecimento de água na Paraíba: o ÁguaViva PB."*

---

### Slide 02: Contexto e Justificativa Socioambiental
- **Visual no Figma**: Manchetes de jornais da Paraíba sobre falta d'água, dados oficiais do Censo IBGE 2022 (50,92% dos lares da PB sem rede de esgoto e 8 dos 10 municípios com pior atendimento hídrico do país no estado), infográfico do Trata Brasil/SNIS indicando 47% de perdas na rede estadual e registros de doenças hídricas do DATASUS.
- **Orador**: Paulo Germano (1,5 minuto).
- **Fala oral sugerida**:
  > *"Ao definir o tema do projeto, buscamos olhar diretamente para a realidade paraibana. Dados do Censo 2022 do IBGE mostram que 50,92% dos lares da Paraíba não possuem rede geral de esgoto, e o Sistema Nacional de Informações sobre Saneamento indica que 47% da água tratada no estado se perde na rede de distribuição antes de chegar às torneiras. Esse problema afeta principalmente comunidades periféricas e rurais, refletindo-se em internações por doenças diarreicas registradas no DATASUS. Como estudantes de ADS, nosso desafio foi investigar como sistemas de informação, dados abertos e usabilidade podem ajudar o cidadão a relatar falhas no abastecimento e acompanhar a situação do saneamento em seu bairro."*

---

### Slide 03: Governança, Engenharia e Repositório
- **Visual no Figma**: Diagrama do ciclo de vida em 7 etapas, tabela de rodízio de liderança técnica e captura do terminal Linux executando o script determinístico `verificar.py`.
- **Orador**: Gabriel Amancio (1,5 minuto).
- **Fala oral sugerida**:
  > *"Para organizar o fluxo de trabalho sem retrabalho, adotamos uma estrutura de monorepositório no Git e um rodízio formal de liderança: a cada etapa, um integrante assumiu a coordenação das atividades e a responsabilidade pela entrega perante os critérios de qualidade estabelecidos. Criamos também um script de validação em Python (`verificar.py`) para checar a consistência do repositório, bloqueando entregas com pendências textuais ou referências ausentes. Toda a documentação foi organizada sob o princípio da Fonte Única da Verdade, mantendo a rastreabilidade entre requisitos, decisões técnicas e 28 fontes catalogadas."*

---

### Slide 04: Pesquisa Empírica do Mercado de TI
- **Visual no Figma**: Gráfico de barras com as competências mais exigidas nos 24 anúncios reais coletados (SQL 45,8%, Git/GitHub 29,2%, Python 29,2%, Comunicação Clara 29,2%, Java/Spring Boot 20,8%, Linux 16,7%, Power BI 16,7%, Cloud 12,5% e LGPD 12,5%), além do destaque de 87,5% de vagas remotas e divisão por especialidades.
- **Orador**: Paulo Germano (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 1, analisamos 24 anúncios reais de vagas de TI abertas no Brasil, distribuídas igualmente em 6 oportunidades para cada uma das quatro áreas da equipe, sendo 87,5% delas no formato remoto. Notamos que bancos de dados com SQL (45,8% do total; 100% em Desenvolvimento e 83,3% em Dados), controle de versão com Git (29,2%) e Python (29,2%) formam a base técnica transversal. Em desenvolvimento, destacam-se Java com Spring Boot (83,3%) e React/TypeScript; em infraestrutura, Linux (66,7%); em dados, Power BI (66,7%); e em segurança, LGPD (50%) e nuvem AWS/Azure. Entre as habilidades comportamentais, a comunicação clara e assíncrona liderou com 29,2% das menções."*

---

### Slide 05: Autoavaliação, Identidade e Planos SMART (PDI)
- **Visual no Figma**: Gráfico comparativo dos quatro perfis, tabela dos gaps coletivos identificados (destaque para Nuvem e Conteinerização Docker com média 2,75 em escala de 1 a 5) e mosaico com os quatro portfólios no GitHub.
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 2, que coordenei, comparamos nossas habilidades individuais com as demandas identificadas no mercado por meio de matrizes de 11 competências. Essa análise mostrou que o grupo tinha boa base em comunicação, trabalho em equipe, lógica e Git, mas apontou uma lacuna comum: a prática com contêineres Docker e serviços em nuvem, onde a média consolidada da equipe ficou em 2,75 numa escala de 1 a 5. A partir desse diagnóstico, cada estudante elaborou um Plano de Desenvolvimento Individual pelo método SMART. Fixamos 12 metas formais com prazos e certificações de referência — Oracle Java SE, AWS Cloud Practitioner, Power BI PL-300, Enap LGPD e CompTIA Security+ — além da participação em comunidades locais como DevOpsDays PB, GDG João Pessoa, Python Nordeste e OWASP."*

---

### Slide 06: Ética Tecnológica, Casos Reais e LGPD
- **Visual no Figma**: Recortes dos relatórios do CESeC (viés em reconhecimento facial) e da decisão preventiva da ANPD contra a Meta, com tabela síntese da matriz de 8 riscos éticos (`RSK-E01` a `RSK-E08`).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 3, examinamos a responsabilidade ética e jurídica no desenvolvimento de software. Analisamos casos concretos no Brasil, como o levantamento do CESeC que revelou que mais de 90% dos presos por reconhecimento facial automatizado eram pessoas negras, evidenciando decisões automatizadas sem checagem humana em desacordo com o Artigo 20 da LGPD. Também estudamos a medida preventiva da ANPD que suspendeu o uso de dados pessoais pela Meta para treino de IA por falta de transparência e opção clara de recusa. Mapeamos essas questões em uma Matriz de Riscos com 8 itens, cobrindo viés algorítmico, privacidade por padrão, alucinações de IA, acessibilidade, segurança OWASP Top 10 e impacto ambiental de Green IT."*

---

### Slide 07: Diagnóstico Censitário e Matriz de Decisão
- **Visual no Figma**: Diagrama de Ishikawa detalhando causas estruturais e a matriz de decisão multicritério destacando a pontuação vencedora do Problema A (Água e Saneamento Básico / ODS 6: 9,05 / 10,0) frente a Desperdício de Alimentos / ODS 2 e 12 (8,20) e Alagamentos e Encostas / ODS 11 e 13 (7,63).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 4, que liderei, aplicamos uma matriz de decisão multicritério para definir o problema socioambiental que guiaria a solução técnica. Comparamos três cenários na Paraíba: qualidade da água e saneamento básico (ODS 6), desperdício de alimentos e insegurança alimentar (ODS 2 e 12), que marcou 8,20, e alagamentos e encostas urbanas (ODS 11 e 13), com 7,63. O saneamento e monitoramento da água obteve a maior pontuação, com nota 9,05 em 10, pela gravidade dos indicadores estaduais e pela viabilidade técnica para a equipe. Mapeamos as causas no Diagrama de Ishikawa e construímos personas como a Dona Maria de Fátima, moradora de periferia com celular básico pré-pago que precisa registrar a falta d'água de forma simples e sem barreiras."*

---

### Slide 08: Arquitetura Técnica C4 e Solução ÁguaViva PB
- **Visual no Figma**: Diagrama de Containers C4 Model demonstrando a estratégia *offline-first* (protótipo conceitual navegável em HTML/CSS/JS vanilla com especificação de 8 telas para Figma e arquitetura-alvo em React + Vite PWA, Service Worker, IndexedDB, backend Docker/Node.js e PostgreSQL/PostGIS).
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Para atender à realidade de pessoas como a Dona Maria, desenhamos a arquitetura do ÁguaViva PB sob o paradigma offline-first. Na arquitetura-alvo de produção em PWA, o Service Worker armazena os ativos da aplicação em cache e, caso o morador esteja sem sinal de internet, a denúncia e a foto comprimida em WebP ficam salvas no IndexedDB local até a sincronização automática no retorno da conexão, chegando a um backend em contêiner Docker com PostgreSQL e PostGIS. Para o projeto integrador, especificamos 12 requisitos funcionais com MoSCoW, 8 requisitos não funcionais verificáveis, 8 histórias de usuário em BDD e entregamos um protótipo navegável completo com simulação desse fluxo."*

---

### Slide 09: Demonstração do Protótipo e Acessibilidade Universal
- **Visual no Figma**: Telas estruturais `TEL-01` a `TEL-08` do protótipo (Tela Inicial, Formulário de Denúncia em 2 passos, Mapa Interativo de Potabilidade, Painel de Transparência, Central de Carro-Pipa, Fila Offline e Modo Alto Contraste / Acessibilidade).
- **Orador**: Gabriel Amancio (2 minutos + condução da demonstração ao vivo).
- **Fala oral sugerida**:
  > *"Neste slide visualizamos as 8 telas estruturais do protótipo do ÁguaViva PB. Priorizamos uma interface direta e acessível, alinhada às recomendações da WCAG 2.2 no nível AA: botões com área de toque mínima de 48 por 48 pixels, contraste reforçado para uso sob sol forte, ampliação tipográfica de até 200% e minimização de dados sob a LGPD, sem exigir login ou CPF do cidadão. Em seguida, demonstraremos ao vivo a navegação pelo protótipo funcional."*

---

### Slide 10: Validação Empírica de Usabilidade e Escala SUS
- **Visual no Figma**: Tabela com os resultados dos testes com 6 voluntários adultos reais (P1 a P6, com TCLE assinado), gráfico de barras de tempo por tarefa vs. meta e destaque para a eficácia de 97,2% e a nota SUS de 84,2 pontos (Excelente / Grau A).
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 6, submetemos o protótipo a testes de usabilidade sob a norma ISO 9241-11 com seis voluntários adultos de diferentes idades e ocupações — entre 23 e 64 anos — incluindo comerciante, agente comunitária de saúde, professora e líder comunitário, todos com TCLE e anonimização pela LGPD. Cada participante executou seis tarefas pelo método Think-Aloud, totalizando 36 observações. Atingimos 97,2% de conclusão com sucesso (35 de 36 tarefas), tempo médio de 59,4 segundos e média de 84,2 pontos na escala SUS, classificando a interface como 'Excelente' (Grau A, percentil acima de 90)."*

---

### Slide 11: Matriz de Melhorias e Protótipo Revisado (v2.0)
- **Visual no Figma**: Comparativo lado a lado "Antes x Depois" das telas `TEL-03`, `TEL-04`, `TEL-05` e `TEL-07` com as melhorias priorizadas pós-teste e nota sobre limitações do estudo (amostra exploratória N=6).
- **Orador**: Luiz Miguel (1,5 minuto).
- **Fala oral sugerida**:
  > *"Os testes com usuários revelaram pontos práticos de melhoria que refatoramos na versão 2.0. No protótipo inicial, a mensagem de modo offline exibia jargões como 'Cache IndexedDB ativo', gerando receio de perda de dados no participante idoso; substituímos por um aviso acolhedor: 'Tudo salvo no celular! Enviaremos automaticamente quando o sinal voltar'. Também fixamos o botão de envio em barra inferior fixa para não ser coberto pelo teclado virtual, incluímos botões ampliados de zoom (+ / -) no mapa, ampliamos legendas de gráficos para alto contraste e previmos feedback háptico de confirmação."*

---

### Slide 12: Conclusão, Diários de Aprendizagem e Agradecimentos
- **Visual no Figma**: Mosaico dos 4 integrantes, síntese dos 24 registros nos Diários de Aprendizagem (6 por estudante, com ao menos 2 novas ferramentas aplicadas por integrante) e roadmap de evolução do ÁguaViva PB.
- **Orador**: Todos os 4 Integrantes (1,5 minuto).
- **Falas orais sugeridas**:
  - **Paulo Germano**: *"O projeto nos permitiu conectar dados reais de mercado e microdados públicos da Paraíba a uma solução técnica fundamentada em evidências."*
  - **Gabriel Amancio**: *"Exercitamos na prática a arquitetura resiliente offline-first, a escrita de requisitos BDD e a acessibilidade digital desde o design inicial."*
  - **Gustavo Antonio**: *"Confirmamos que a conformidade com a LGPD, a análise de riscos éticos e a revisão crítica de ferramentas de IA precisam caminhar juntas em qualquer sistema."*
  - **Luiz Miguel**: *"Agradecemos aos professores do UNIPÊ pelo acompanhamento ao longo do semestre e nos colocamos à disposição da banca para a arguição técnica. Muito obrigado."*
