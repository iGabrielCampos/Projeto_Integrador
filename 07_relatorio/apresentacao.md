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
tempo_total_estimado: "18 a 20 minutos"
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
  > *"Boa noite, nobres professores da banca avaliadora, colegas e presentes. Somos estudantes do Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas do UNIPÊ. Nosso grupo é composto por Gabriel Amancio, focado em Desenvolvimento de Software; Luiz Miguel, em Infraestrutura e Redes; eu, Paulo Germano, na área de Dados e Inteligência Artificial; e Gustavo Antonio, em Segurança da Informação. Hoje temos a satisfação de apresentar o resultado integrado do nosso Projeto de Design Profissional, no qual aliamos o diagnóstico rigoroso das exigências do mercado de trabalho de TI à concepção de uma tecnologia cívica de alto impacto social para o nosso estado: a plataforma ÁguaViva PB."*

---

### Slide 02: Contexto e Justificativa Socioambiental
- **Visual no Figma**: Manchetes de jornais da Paraíba sobre falta d'água, dados oficiais do Censo IBGE 2022 (50,9% dos lares da PB sem rede de esgoto) e infográfico do Trata Brasil indicando 47% de perdas na rede hídrica estadual.
- **Orador**: Paulo Germano (1,5 minuto).
- **Fala oral sugerida**:
  > *"Ao iniciarmos este projeto, nos recusamos a construir uma solução hipotética desconectada da realidade paraibana. Os dados oficiais do Censo Demográfico do IBGE revelam que mais de metade dos domicílios da Paraíba ainda sofrem com a ausência de rede geral de esgoto sanitário, e o Sistema Nacional de Informações sobre Saneamento aponta que quase metade da água tratada no estado se perde em tubulações obsoletas antes de chegar às casas. Esse cenário atinge brutalmente as comunidades periféricas e rurais. Nosso desafio como futuros analistas de sistemas foi responder à pergunta: como a tecnologia da informação, a governança de dados e a responsabilidade social podem empoderar o cidadão para fiscalizar e combater essa crise hídrica?"*

---

### Slide 03: Governança, Engenharia e Repositório
- **Visual no Figma**: Diagrama do ciclo de vida em 7 etapas, tabela de rodízio de liderança técnica e captura do terminal Linux executando o script determinístico `verificar.py`.
- **Orador**: Gabriel Amancio (1,5 minuto).
- **Fala oral sugerida**:
  > *"Para operacionalizar um projeto dessa envergadura sem retrabalho ou sobreposição, estabelecemos uma governança técnica de padrão industrial. Adotamos o modelo de monorepositório versionado em Git, com rodízio estrito de liderança técnica: cada etapa teve um líder nominal que assinou e respondeu pela entrega perante os portões de qualidade. Desenvolvemos ainda um validador automatizado em Python que barrava qualquer commit com lacunas textuais ou fontes não registradas em nosso arquivo mestre. Toda a documentação e dados operam sob o princípio da Fonte Única da Verdade, garantindo rastreabilidade absoluta de ponta a ponta."*

---

### Slide 04: Pesquisa Empírica do Mercado de TI
- **Visual no Figma**: Gráfico de barras com as competências mais exigidas nos 24 anúncios reais coletados (Git 88%, SQL 79%, Docker 58%, Cloud 50%) e divisão por especialidades.
- **Orador**: Paulo Germano (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 1, investigamos o mundo real do trabalho coletando e auditando 24 anúncios reais de vagas públicas de TI no Brasil, com equilíbrio rigoroso de 6 vagas para cada uma das nossas quatro especialidades. Constatamos que o domínio de Git, bancos de dados SQL e cultura de contêineres com Docker formam o piso mínimo inegociável em todos os nichos. No desenvolvimento de software, React, TypeScript e Java Spring dominam o mercado; em infraestrutura, há uma migração massiva para nuvem pública AWS; em dados, a linguagem Python é unânime; e em segurança, a conformidade com a LGPD e testes de intrusão são mandatórios. Além disso, a capacidade de comunicação assíncrona clara surgiu como a competência socioemocional mais valorizada pelos recrutadores."*

---

### Slide 05: Autoavaliação, Identidade e Planos SMART (PDI)
- **Visual no Figma**: Gráfico de radar comparativo dos quatro perfis, tabela dos gaps coletivos identificados e mosaico com os quatro repositórios de portfólio no GitHub.
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 2, liderada por mim, confrontamos nossas habilidades individuais com as demandas apuradas no mercado através de matrizes com 11 competências. A análise comparativa revelou uma equipe com excelente base em lógica, versionamento e comunicação, mas expôs um gap coletivo evidente: a orquestração prática de serviços em nuvem e contêineres Docker, cuja média da equipe era de apenas 2,75. Em resposta direta a esse diagnóstico, cada discente elaborou um Plano de Desenvolvimento Individual estruturado no método SMART. Estabelecemos 12 metas formais, cobrindo certificações da AWS, Oracle Java, Power BI e CompTIA Security+, integrando nossas trajetórias a comunidades ativas da Paraíba como o DevOpsDays PB, GDG João Pessoa e OWASP."*

---

### Slide 06: Ética Tecnológica, Casos Reais e LGPD
- **Visual no Figma**: Recortes dos relatórios do CESeC (viés em reconhecimento facial) e da decisão liminar da ANPD contra a Meta, com tabela síntese da matriz de riscos éticos.
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"A Etapa 3 nos colocou diante da responsabilidade cívica e jurídica do desenvolvedor. Analisamos casos reais no Brasil, como o estudo do CESeC que comprovou que mais de 90% dos presos por reconhecimento facial automatizado no país eram pessoas negras, ilustrando o perigo de decisões algorítmicas enviesadas sem revisão humana, ferindo o Art. 20 da LGPD. Também examinamos a medida da ANPD que impediu o treinamento indiscriminado de IAs generativas com dados pessoais dos brasileiros sem consentimento prévio. Sistematizamos esses aprendizados em uma Matriz de Riscos com 8 vetores críticos, cobrindo desde discriminação e vazamentos de privacidade até a pegada ecológica de datacenters e riscos de injeção de prompt."*

---

### Slide 07: Auditoria Prática de Alucinações em LLMs
- **Visual no Figma**: Capturas comparativas dos 4 experimentos laboratoriais (EXP-01 a EXP-04), com destaque para o código com falha de rate limiting e o erro de soma matemática de R$ 380,00 no Gemini.
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Como futuros profissionais de tecnologia, decidimos testar empiricamente os limites da Inteligência Artificial em vez de confiar cegamente em suas saídas. Realizamos 4 experimentos laboratoriais controlados. O Gabriel solicitou ao ChatGPT uma rota de autenticação JWT e constatou a omissão perigosa de limitação de requisições, abrindo brecha para ataques de força bruta. O Luiz Miguel detectou no Claude um script de firewall que aplicava a política DROP antes de liberar a porta SSH, o que derrubaria o servidor em produção. O Paulo Germano pegou o Gemini alucinando uma conta de soma em R$ 380,00 reais. E eu demonstrei no Copilot uma interpretação jurídica permissiva sobre cláusulas contratuais abusivas. Esse teste comprovou cientificamente que a IA é apenas uma ferramenta auxiliar que exige auditoria técnica humana permanente."*

---

### Slide 08: Diagnóstico Censitário e Matriz de Decisão
- **Visual no Figma**: Diagrama de Ishikawa detalhando causas estruturais, e a matriz de decisão multicritério destacando a pontuação vencedora da Opção 1 (ÁguaViva PB: 9,05 / 10,0).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 4, que tive a honra de coordenar, estruturamos uma Matriz de Decisão Multicritério com pesos ponderados para selecionar o problema socioambiental a ser enfrentado. Avaliamos três temas concorrentes: a gestão de lixo eletrônico, a prevenção de golpes digitais em idosos e o saneamento básico e monitoramento da água na Paraíba. O tema da água e saneamento sagrou-se vencedor incontestável com nota 9,05 de 10,0. Mapeamos as causas-raiz no Diagrama de Ishikawa e construímos a persona da Dona Maria de Fátima, moradora de comunidade periférica que passa dias sem água, tem celular simples sem pacote de internet e precisa de uma ferramenta rápida e sem burocracia para ser ouvida pelo poder público."*

---

### Slide 09: Arquitetura Técnica C4 e Solução ÁguaViva PB
- **Visual no Figma**: Diagrama de Containers C4 Model demonstrando a interface React PWA, Service Worker, banco local IndexedDB e serviços de backend em nuvem com PostgreSQL/PostGIS.
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Para atender à realidade da Dona Maria de Fátima, concebemos a arquitetura da plataforma ÁguaViva PB. Trata-se de um Progressive Web App (PWA) projetado sob o paradigma Offline-First. O sistema opera com Service Workers que realizam o cache completo da aplicação no primeiro acesso. Caso o cidadão esteja sem sinal de dados móveis no bairro, a denúncia, foto comprimida e coordenadas geográficas são retidas com segurança no banco de dados local IndexedDB do aparelho. Assim que o smartphone detecta o retorno de conexão Wi-Fi ou 4G, os dados são sincronizados assincronamente com nosso backend em nuvem. Modelamos 12 requisitos funcionais com MoSCoW, 8 histórias de usuário em BDD e métricas rigorosas de desempenho e segurança da informação."*

---

### Slide 10: Demonstração Visual do Protótipo (Figma)
- **Visual no Figma**: Telas navegáveis conceituais do protótipo no Figma (Tela Inicial, Mapa de Potabilidade por Bairro, Formulário de Denúncia em 2 passos, Central Emergencial de Carro-Pipa e Modo Alto Contraste).
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"Aqui visualizamos as principais telas do nosso protótipo navegável de alta fidelidade desenhado no Figma. Priorizamos o minimalismo e a acessibilidade digital segundo os padrões WCAG 2.2 AA. Os botões de toque possuem área mínima generosa de 48 por 48 pixels para evitar toques acidentais por pessoas idosas. O mapa interativo utiliza cores semânticas intuitivas: verde para água potável e vermelha para áreas com interrupção ou contaminação. Com apenas três toques, o morador registra a falta d'água, anexa foto da torneira seca e recebe um número de protocolo coletivo, agrupando os vizinhos para cobrar celeridade da concessionária e acionar a Defesa Civil para envio de caminhão-pipa emergencial."*

---

### Slide 11: Validação Empírica de Usabilidade e Escala SUS
- **Visual no Figma**: Tabela com os resultados dos testes com 6 participantes reais (P1 a P6), gráfico de barras de tempo por tarefa e destaque para a nota SUS de 84,2 pontos (Excelente).
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 6, levamos a solução para o teste de fogo: uma avaliação empírica de usabilidade supervisionada com seis voluntários reais, contemplando desde donas de casa e líderes comunitários idosos até agentes de saúde e professores. Coletamos 36 observações controladas em 6 tarefas críticas. O resultado quantitativo foi expressivo: obtivemos 97,2% de taxa de eficácia e um tempo médio de conclusão de apenas 59 segundos. Aplicamos a consagrada Escala de Usabilidade do Sistema (SUS) de John Brooke e alcançamos a pontuação de 84,2 pontos em 100. Na literatura científica de IHC, notas acima de 80 posicionam a aplicação na faixa de excelência máxima (Grade A), comprovando que o design centrado no usuário eliminou barreiras de uso."*

---

### Slide 12: Matriz de Melhorias e Protótipo Revisado (v2.0)
- **Visual no Figma**: Comparativo lado a lado 'Antes x Depois' das telas TEL-03 e TEL-07, destacando a substituição de termos técnicos por frases acolhedoras e a fixação do botão de envio.
- **Orador**: Luiz Miguel (1,5 minuto).
- **Fala oral sugerida**:
  > *"Os testes reais foram vitais para expor pontos de atrito que nossa equipe técnica não havia enxergado. No protótipo inicial, ao ficar offline, o app mostrava uma mensagem técnica dizendo: 'Cache IndexedDB ativo. Sincronização pendente via API REST'. Nosso voluntário idoso de 64 anos ficou com medo de ter quebrado o celular. Aprendemos a lição: refatoramos a mensagem para um aviso acolhedor: 'Tudo salvo no seu celular! Não se preocupe: assim que o sinal voltar, enviamos seu relato sozinho'. Além disso, fixamos o botão de envio no rodapé da tela para não ser engolido pelo teclado virtual e inserimos botões grandes de zoom no mapa. Essa é a essência do aperfeiçoamento contínuo da engenharia de software."*

---

### Slide 13: Conclusão, Impacto e Agradecimentos
- **Visual no Figma**: Mosaico dos 4 integrantes, resumo dos ganhos de aprendizagem (mais de 2 novas ferramentas dominadas por estudante) e roadmap futuro para a Paraíba.
- **Orador**: Todos os 4 Integrantes (1,5 minuto).
- **Falas orais sugeridas**:
  - **Paulo Germano**: *"Este Projeto Integrador nos transformou. Deixamos de ser meros codificadores de laboratório para nos tornarmos profissionais conscientes da relevância social e da ética em TI."*
  - **Gabriel Amancio**: *"Aprendemos na prática a arquitetar sistemas resilientes, a documentar sob normas ABNT e a validar acessibilidade universal."*
  - **Gustavo Antonio**: *"Comprovamos que a segurança, a conformidade com a LGPD e o ceticismo perante a Inteligência Artificial devem nascer no primeiro dia do projeto."*
  - **Luiz Miguel**: *"Agradecemos imensamente ao corpo docente do UNIPÊ pela orientação e estímulo ao longo de todo este semestre. Estamos prontos para as perguntas e considerações da banca examinadora. Muito obrigado!"*
