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
tempo_total_estimado: "25 a 30 minutos (23 min de slides + 5 a 7 min de demonstração do protótipo) + 10 min de arguição"
ferramenta_slides: Figma / Google Slides
---

# Roteiro Oficial de Apresentação e Script de Defesa Oral

## Estrutura da Apresentação (Divisão Equitativa de Falas)

| Slide | Bloco Temático | Orador Titular | Tempo Alocado | Foco do Conteúdo |
|---|---|---|---|---|
| **01** | Capa e Identificação Institucional | Paulo Germano | 1 min | Apresentação da equipe, curso, instituição e título |
| **02** | Contextualização e Justificativa | Paulo Germano | 1,5 min | Desafios de saneamento na PB e metas formativas |
| **03** | Governança e Metodologia | Gabriel Amancio | 1,5 min | Rodízio de liderança, monorepositório e scripts |
| **04** | Pesquisa de Mercado (24 Vagas) | Paulo Germano | 2 min | Análise de vagas, competências mais frequentes |
| **05** | Identidade, Autoavaliação e PDI | Luiz Miguel | 2 min | Matrizes individuais, gaps de nuvem e metas SMART |
| **06** | Ética Tecnológica e Casos Reais | Gabriel Amancio | 2 min | Caso CESeC e medida preventiva da ANPD |
| **07** | Experimentos Práticos com IA | Gustavo Antonio | 2 min | Detecção empírica de alucinações e falhas em LLMs |
| **08** | Diagnóstico Socioambiental (ODS 6) | Gustavo Antonio | 2 min | Ishikawa e matriz multicritério com dados do Censo |
| **09** | Solução ÁguaViva PB (Arquitetura) | Gabriel Amancio | 2 min | C4 Model, PWA offline-first e requisitos MoSCoW |
| **10** | Demonstração do Protótipo (Figma) | Gabriel Amancio | 2 min | Telas principais, denúncia, mapa e acessibilidade |
| **11** | Testes de Usabilidade e Escala SUS | Luiz Miguel | 2 min | 36 sessões, eficácia de 97,2% e SUS de 84,2 pontos |
| **12** | Matriz de Melhorias e Protótipo v2 | Luiz Miguel | 1,5 min | Correções pós-teste e humanização de avisos |
| **13** | Conclusão, Impacto e Roadmap | Todos | 1,5 min | Aprendizados dos 4 integrantes e próximos passos |

---

## Script Detalhado por Slide

### Slide 01: Abertura e Apresentação da Equipe
- **Visual no Figma**: Logo institucional do UNIPÊ, título do projeto em destaque (*Laboratório de Carreira e Inovação Responsável em TI: Solução ÁguaViva PB*), foto e nome dos quatro discentes com suas respectivas áreas de atuação em ADS.
- **Orador**: Paulo Germano (1 minuto).
- **Fala oral sugerida**:
  > *"Boa noite aos professores da banca avaliadora, aos colegas e a todos os presentes. Somos discentes do curso de Análise e Desenvolvimento de Sistemas do UNIPÊ. O grupo é formado por Gabriel Amancio, na área de Desenvolvimento de Software; Luiz Miguel, em Infraestrutura e Redes; eu, Paulo Germano, em Dados e Inteligência Artificial; e Gustavo Antonio, em Segurança da Informação. Hoje apresentamos o resultado do nosso Projeto de Design Profissional, no qual relacionamos as demandas reais do mercado de trabalho em TI ao desenvolvimento de uma aplicação voltada aos problemas de saneamento e abastecimento de água na Paraíba: o ÁguaViva PB."*

---

### Slide 02: Contexto e Justificativa Socioambiental
- **Visual no Figma**: Manchetes de jornais da Paraíba sobre falta d'água, dados oficiais do Censo IBGE 2022 (50,9% dos lares da PB sem rede de esgoto) e infográfico do Trata Brasil indicando 47% de perdas na rede hídrica estadual.
- **Orador**: Paulo Germano (1,5 minuto).
- **Fala oral sugerida**:
  > *"Ao definir o tema do projeto, buscamos olhar diretamente para a realidade paraibana. Dados do Censo 2022 do IBGE mostram que 50,9% dos lares da Paraíba não possuem rede geral de esgoto, e o Sistema Nacional de Informações sobre Saneamento indica que 47% da água tratada no estado se perde na rede de distribuição antes de chegar às torneiras. Esse problema afeta principalmente comunidades periféricas e rurais. Como estudantes de ADS, nosso desafio foi investigar como sistemas de informação, dados abertos e usabilidade podem ajudar o cidadão a relatar falhas no abastecimento e acompanhar a situação do saneamento em seu bairro."*

---

### Slide 03: Governança, Engenharia e Repositório
- **Visual no Figma**: Diagrama do ciclo de vida em 7 etapas, tabela de rodízio de liderança técnica e captura do terminal Linux executando o script determinístico `verificar.py`.
- **Orador**: Gabriel Amancio (1,5 minuto).
- **Fala oral sugerida**:
  > *"Para organizar o fluxo de trabalho sem retrabalho, adotamos uma estrutura de monorepositório no Git e um rodízio formal de liderança: a cada etapa, um integrante assumiu a coordenação das atividades e a responsabilidade pela entrega perante os critérios de qualidade estabelecidos. Criamos também um script de validação em Python (verificar.py) para checar a consistência do repositório, bloqueando commits com pendências textuais ou referências ausentes. Toda a documentação foi organizada sob o princípio da Fonte Única da Verdade, mantendo a rastreabilidade entre requisitos, decisões técnicas e código."*

---

### Slide 04: Pesquisa Empírica do Mercado de TI
- **Visual no Figma**: Gráfico de barras com as competências mais exigidas nos 24 anúncios reais coletados (Git 88%, SQL 79%, Docker 58%, Cloud 50%) e divisão por especialidades.
- **Orador**: Paulo Germano (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 1, analisamos 24 anúncios reais de vagas de TI abertas no Brasil, distribuídas igualmente em 6 oportunidades para cada uma das quatro áreas da equipe. Notamos que bancos de dados relacionais com SQL, controle de versão com Git e o uso de contêineres com Docker aparecem como requisitos básicos em quase todas as funções. Em desenvolvimento de software, destacam-se React, TypeScript e Java com Spring Boot; em infraestrutura, sobressaem serviços em nuvem AWS e ambientes Linux; na área de dados, a linguagem Python e ferramentas de BI; e em segurança, conhecimentos de LGPD e segurança de aplicações. Entre as habilidades socioemocionais, a comunicação assíncrona e o trabalho colaborativo foram os requisitos mais citados pelos contratantes."*

---

### Slide 05: Autoavaliação, Identidade e Planos SMART (PDI)
- **Visual no Figma**: Gráfico de radar comparativo dos quatro perfis, tabela dos gaps coletivos identificados e mosaico com os quatro repositórios de portfólio no GitHub.
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 2, que coordenei, comparamos nossas habilidades individuais com as demandas identificadas no mercado por meio de matrizes de 11 competências. Essa análise mostrou que o grupo tinha boa base em lógica, Git e comunicação, mas apontou uma lacuna comum: a prática com contêineres Docker e serviços em nuvem, onde a média da equipe foi de 2,75 numa escala de 1 a 5. A partir desse diagnóstico, cada estudante elaborou um Plano de Desenvolvimento Individual pelo método SMART. Fixamos 12 metas formais com prazos e certificações de referência, como AWS, Oracle Java, Power BI e CompTIA Security+, além de prever nossa participação em comunidades técnicas locais, a exemplo do DevOpsDays PB, GDG João Pessoa e OWASP."*

---

### Slide 06: Ética Tecnológica, Casos Reais e LGPD
- **Visual no Figma**: Recortes dos relatórios do CESeC (viés em reconhecimento facial) e da decisão liminar da ANPD contra a Meta, com tabela síntese da matriz de riscos éticos.
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 3, examinamos a responsabilidade ética e jurídica no desenvolvimento de software. Analisamos casos concretos no Brasil, como o levantamento do CESeC que revelou que mais de 90% dos presos por reconhecimento facial automatizado eram pessoas negras. O caso evidenciou o perigo de decisões automatizadas sem checagem humana, em desacordo com o Artigo 20 da LGPD. Também estudamos a intervenção da ANPD sobre o uso de dados de usuários brasileiros para treino de IA sem opção clara de recusa. Mapeamos essas questões em uma Matriz de Riscos com 8 itens, cobrindo privacidade, discriminação algorítmica, segurança de aplicações e impacto ambiental do consumo energético em data centers."*

---

### Slide 07: Auditoria Prática de Alucinações em LLMs
- **Visual no Figma**: Capturas comparativas dos 4 experimentos laboratoriais (EXP-01 a EXP-04), com destaque para o código com falha de rate limiting e o erro de soma matemática de R$ 380,00 no Gemini.
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Para verificar na prática a confiabilidade de modelos de IA, realizamos quatro experimentos controlados. O Gabriel pediu ao ChatGPT um endpoint de autenticação JWT e identificou a falta de limitação de taxa de requisições, o que deixaria o serviço exposto a ataques de força bruta. O Luiz Miguel testou a criação de regras de firewall no Claude, e o modelo sugeriu aplicar a política restritiva DROP antes de liberar o SSH, o que travaria o acesso remoto ao servidor. O Paulo Germano submeteu um conjunto de dados ao Gemini para cálculos estatísticos e o modelo errou uma soma aritmética simples. E eu testei no Copilot a análise de uma cláusula contratual abusiva que feria o Código de Defesa do Consumidor e a LGPD. Os experimentos deixaram claro que a IA auxilia na produtividade, mas a revisão técnica humana continua indispensável."*

---

### Slide 08: Diagnóstico Censitário e Matriz de Decisão
- **Visual no Figma**: Diagrama de Ishikawa detalhando causas estruturais, e a matriz de decisão multicritério destacando a pontuação vencedora da Opção 1 (ÁguaViva PB: 9,05 / 10,0).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 4, que liderei, aplicamos uma matriz de decisão multicritério para definir o problema socioambiental que guiaria a solução técnica. Comparamos três propostas: descarte de lixo eletrônico, segurança contra golpes digitais em idosos e saneamento e monitoramento da água na Paraíba. A temática de saneamento e água obteve a pontuação mais alta, com nota 9,05 em 10, considerando a gravidade do cenário estadual e a viabilidade técnica para a equipe. Mapeamos as causas do problema no Diagrama de Ishikawa e construímos a persona da Dona Maria de Fátima: moradora da periferia de João Pessoa que enfrenta dias sem água, tem um celular básico sem franquia contínua de internet e precisa de um canal simples e acessível para registrar a falta d'água."*

---

### Slide 09: Arquitetura Técnica C4 e Solução ÁguaViva PB
- **Visual no Figma**: Diagrama de Containers C4 Model demonstrando a interface React PWA, Service Worker, banco local IndexedDB e serviços de backend em nuvem com PostgreSQL/PostGIS.
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Para atender à realidade de pessoas como a Dona Maria, desenhamos a arquitetura do ÁguaViva PB. Definimos a aplicação como um Progressive Web App (PWA) com operação voltada ao modo offline (offline-first). O navegador armazena a estrutura da página em cache logo no primeiro acesso. Se a pessoa estiver sem sinal de internet no bairro, o formulário, as coordenadas e a foto ficam gravados no banco local IndexedDB do aparelho. Assim que o dispositivo detecta a volta da conexão, os dados são enviados automaticamente ao backend em nuvem. Especificamos 12 requisitos funcionais com o método MoSCoW, 8 histórias de usuário em formato BDD e requisitos não funcionais com metas claras de desempenho, segurança e acessibilidade."*

---

### Slide 10: Demonstração Visual do Protótipo (Figma)
- **Visual no Figma**: Telas navegáveis conceituais do protótipo no Figma (Tela Inicial, Mapa de Potabilidade por Bairro, Formulário de Denúncia em 2 passos, Central Emergencial de Carro-Pipa e Modo Alto Contraste).
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Neste slide visualizamos as principais telas do protótipo no Figma. Priorizamos uma interface direta e acessível, alinhada às recomendações da WCAG 2.2 no nível AA. Os botões de ação contam com área de toque mínima de 48 por 48 pixels, o que facilita o uso em telas pequenas e reduz erros de clique. O mapa utiliza legendas e cores contrastantes para indicar a situação de cada localidade. Com poucos toques, a pessoa consegue selecionar o tipo de ocorrência, anexar uma foto e confirmar o chamado, gerando um protocolo que agrupa relatos da vizinhança para facilitar o acompanhamento com a concessionária ou o acionamento de apoio emergencial."*

---

### Slide 11: Validação Empírica de Usabilidade e Escala SUS
- **Visual no Figma**: Tabela com os resultados dos testes com 6 participantes reais (P1 a P6), gráfico de barras de tempo por tarefa e destaque para a nota SUS de 84,2 pontos (Excelente).
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 6, submetemos o protótipo a testes de usabilidade com seis voluntários de diferentes idades e ocupações, incluindo agentes de saúde, professores e líderes comunitários. Cada voluntário executou seis tarefas no sistema, totalizando 36 observações registradas. O índice geral de conclusão com sucesso foi de 97,2%, com tempo médio de 59,4 segundos por tarefa. Ao final, aplicamos o questionário da Escala de Usabilidade do Sistema (SUS), obtendo uma média de 84,2 pontos em 100. Na metodologia de Brooke, pontuações acima de 80 situam a interface na faixa 'Excelente', indicando que as escolhas de design atenderam bem ao público-alvo."*

---

### Slide 12: Matriz de Melhorias e Protótipo Revisado (v2.0)
- **Visual no Figma**: Comparativo lado a lado 'Antes x Depois' das telas TEL-03 e TEL-07 com a substituição de termos técnicos por frases acolhedoras e a fixação do botão de envio.
- **Orador**: Luiz Miguel (1,5 minuto).
- **Fala oral sugerida**:
  > *"Os testes com usuários trouxeram melhorias práticas que não havíamos notado internamente. No protótipo inicial, a mensagem de tela ao entrar em modo offline exibia termos técnicos como 'Cache IndexedDB ativo. Sincronização pendente via API REST'. Um voluntário de 64 anos relatou receio de que o celular tivesse travado. Ajustamos o texto para uma comunicação clara e acolhedora: 'Tudo salvo no seu celular! Não se preocupe: assim que o sinal voltar, enviamos seu relato sozinho'. Também fixamos o botão de envio na parte inferior da tela para não sumir sob o teclado virtual e adicionamos botões táteis de zoom no mapa. Essas mudanças tornaram a navegação mais simples e segura para o usuário."*

---

### Slide 13: Conclusão, Impacto e Agradecimentos
- **Visual no Figma**: Mosaico dos 4 integrantes, resumo dos ganhos de aprendizagem (mais de 2 novas ferramentas dominadas por estudante) e roadmap futuro para a Paraíba.
- **Orador**: Todos os 4 Integrantes (1,5 minuto).
- **Falas orais sugeridas**:
  - **Paulo Germano**: *"O projeto nos permitiu conectar teoria e prática, mostrando como a tecnologia pode responder a problemas sociais urgentes da nossa região."*
  - **Gabriel Amancio**: *"Exercitamos na prática a arquitetura de software resiliente, a escrita de requisitos claros e os cuidados com acessibilidade."*
  - **Gustavo Antonio**: *"Compreendemos que a conformidade com a LGPD, os controles de segurança e a checagem crítica de ferramentas de IA precisam ser tratados desde o primeiro dia de trabalho."*
  - **Luiz Miguel**: *"Agradecemos aos professores do UNIPÊ pelo suporte ao longo do semestre e nos colocamos à disposição da banca para a arguição técnica. Muito obrigado."*
