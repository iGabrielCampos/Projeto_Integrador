---
id: roteiro-defesa-banca
etapa: 7
titulo: Banco de Perguntas Prováveis da Banca Examinadora e Roteiro de Respostas Técnicas
projeto: Laboratório de Carreira e Inovação Responsável em TI - ÁguaViva PB
instituicao: UNIPÊ - Centro Universitário de João Pessoa
curso: CST em Análise e Desenvolvimento de Sistemas
equipe:
  - Gabriel Amancio (Desenvolvimento de Software)
  - Luiz Miguel (Infraestrutura e Redes)
  - Paulo Germano (Dados e IA)
  - Gustavo Antonio (Segurança da Informação)
total_perguntas: 20
---

# Banco de Perguntas Prováveis da Banca Examinadora e Respostas Técnicas

Este documento prepara os quatro discentes para a arguição oral individual perante a banca examinadora do Projeto Integrador de ADS do UNIPÊ. As 20 questões estão organizadas cronologicamente pelas 7 etapas do projeto, contemplando o titular recomendado, os conceitos teóricos envolvidos e a sugestão de resposta verbal fundamentada.

---

## Bloco 1: Governança, Metodologia e Integridade (Etapa 0)

### Pergunta 01: Qual foi o critério para a adoção do rodízio de liderança técnica por etapa e como o grupo evitou gargalos operacionais?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Engenharia de processos, metodologias ágeis e governança de software.
- **Resposta Sugerida**:
  > *"Adotamos o rodízio de liderança técnica para que cada integrante assumisse a responsabilidade direta de organizar tarefas, revisar entregas e responder pelos critérios de qualidade de sua fase. O líder da etapa coordenava o escopo daquela entrega, enquanto os demais atuavam na revisão de código e documentação. Para evitar gargalos e inconsistências, criamos um script de verificação em Python (verificar.py) executado antes dos commits. Caso existisse alguma pendência textual ou citação sem correspondência no arquivo de fontes, a alteração era barrada. Isso trouxe autonomia ao grupo e manteve a qualidade das entregas sem depender de revisões manuais repetitivas."*

### Pergunta 02: Como o grupo assegurou que o uso de Inteligência Artificial generativa não substituísse a autoria e a aprendizagem dos estudantes?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Integridade acadêmica, ética algorítmica e trilhas de auditoria.
- **Resposta Sugerida**:
  > *"Definimos desde o início regras claras de integridade acadêmica. As ferramentas de IA foram usadas apenas como apoio instrumental, ajudando na formatação em Markdown, organização de tabelas e rascunho de diagramas Mermaid. Toda a parte analítica e prática, como os registros dos diários de aprendizagem, a aplicação dos testes de usabilidade com voluntários e as decisões de arquitetura, foi elaborada diretamente por nós. Além disso, registramos todas as interações com modelos de linguagem em um log de auditoria (00_gestao/uso_ia.md), detalhando o modelo, o prompt, a resposta gerada e a revisão humana, além das declarações individuais de uso ético anexadas ao relatório."*

---

## Bloco 2: Pesquisa de Mercado de Trabalho em TI (Etapa 1)

### Pergunta 03: Por que a amostragem de vagas foi fixada em exatamente 24 anúncios e como foi garantida a representatividade no Nordeste e Paraíba?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Amostragem estratificada e metodologia de pesquisa de mercado.
- **Resposta Sugerida**:
  > *"Fixamos a amostra em 24 vagas distribuídas em quatro grupos iguais de 6 oportunidades para cada área da equipe: Desenvolvimento, Infraestrutura, Dados e Segurança. Essa divisão impediu que vagas de desenvolvimento web concentrassem a maior parte da amostra e garantiu uma leitura equilibrada de cada nicho. Para aproximar os dados do cenário regional, selecionamos vagas ativas em 06/11/2026 no Portal Gupy [F020], dando prioridade a empresas com atuação em João Pessoa, Campina Grande e Recife, além de vagas remotas nacionais acessíveis a profissionais do Nordeste. Todos os links, cargos e datas de consulta constam na planilha do repositório."*

### Pergunta 04: Qual foi a constatação mais surpreendente na análise das competências técnicas exigidas para vagas de nível Júnior e Estágio?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Análise de frequência de requisitos em editais e anúncios corporativos.
- **Resposta Sugerida**:
  > *"O ponto que mais chamou atenção foi a exigência de conhecimentos transversais de engenharia mesmo para nível júnior e estágio — como SQL em 45,8% do total (100% em Dev e 83,3% em Dados), Git/GitHub em 29,2% e Python em 29,2% — além da presença de contêineres Docker e computação em nuvem como diferenciais práticos já em vagas iniciais (como VAG-001, VAG-004 e VAG-010). Como 87,5% das vagas analisadas eram remotas, a comunicação clara também se destacou (29,2%). Esse resultado orientou diretamente as metas de estudo nos nossos planos de desenvolvimento."*

### Pergunta 05: Quais foram as principais dores operacionais relatadas pelas empresas contratantes na pesquisa de mercado?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Mapeamento de desafios do mercado de TI corporativo.
- **Resposta Sugerida**:
  > *"Identificamos cinco desafios frequentes nas descrições de vagas: a modernização de sistemas legados para arquiteturas modulares sem interromper operações; a adequação dos sistemas às exigências da LGPD; o controle de custos em serviços de nuvem (FinOps); a inconsistência e baixa qualidade de bases de dados cadastrais; e a dificuldade em encontrar profissionais que aliem conhecimento técnico a uma boa comunicação em equipe."*

---

## Bloco 3: Identidade Profissional, Autoavaliação e PDI (Etapa 2)

### Pergunta 06: Como a matriz de competências da equipe permitiu identificar os 'gaps' compartilhados e qual foi a estratégia para superá-los?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Matriz de autoavaliação, curva de proficiência e aprendizagem colaborativa.
- **Resposta Sugerida**:
  > *"Ao consolidar as autoavaliações em 11 competências com notas de 1 a 5, vimos que a equipe tinha boas médias em lógica de programação (3,75), Git (4,13) e comunicação em grupo (4,50). Por outro lado, o uso prático de Docker e serviços de nuvem teve média de 2,75, apontando uma lacuna comum. Para trabalhar esse ponto, definimos que a solução técnica da Etapa 5 utilizaria contêineres Docker e que eu, como responsável pela área de infraestrutura, apoiaria os colegas na configuração de ambientes locais e virtuais, alinhando essa prática às metas dos nossos planos de desenvolvimento."*

### Pergunta 07: Qual é a diferença prática entre uma meta genérica e uma meta SMART no contexto de carreira em tecnologia?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Metodologia SMART (Doran, 1981).
- **Resposta Sugerida**:
  > *"Uma meta genérica expressa uma intenção sem critérios de acompanhamento, como dizer 'quero aprender computação em nuvem'. Ela não define prazo nem forma de avaliar o progresso. Já uma meta no padrão SMART é estruturada em cinco critérios: Específica, Mensurável, Atingível, Relevante e com Prazo definido. No meu caso, defini a meta de obter a certificação AWS Certified Cloud Practitioner (CLF-C02) até 31 de maio de 2027, dedicando 6 horas semanais de estudo e realizando três simulados com aproveitamento mínimo de 80%. O método SMART estabelece o caminho de estudo, o indicador de conclusão e uma data limite clara."*

### Pergunta 08: De que maneira as comunidades técnicas locais de João Pessoa e da Paraíba foram incorporadas ao plano profissional do grupo?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Comunidades de prática (Wenger) e networking profissional regional.
- **Resposta Sugerida**:
  > *"Reconhecemos que o aprendizado em tecnologia vai além da sala de aula. Por isso, mapeamos grupos e iniciativas ativas na Paraíba, como o GDG João Pessoa, o capítulo da OWASP, a comunidade Python Nordeste e o evento DevOpsDays PB. Incluímos nos nossos planos de desenvolvimento a participação nesses encontros, o que nos conecta a profissionais mais experientes, abre espaço para troca de experiências em projetos práticos e nos mantém informados sobre demandas do mercado local."*

---

## Bloco 4: Ética, Riscos Algorítmicos e Experimentos com IA (Etapa 3)

### Pergunta 09: No caso do reconhecimento facial investigado pelo CESeC, qual artigo da LGPD é violado quando uma pessoa é detida exclusivamente por indicação do algoritmo?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: LGPD (Lei nº 13.709/2018, Art. 20) e direitos fundamentais.
- **Resposta Sugerida**:
  > *"O caso fere o Artigo 20 da LGPD, que garante ao titular o direito de solicitar a revisão de decisões tomadas unicamente por tratamento automatizado de dados pessoais que afetem seus interesses. Quando a abordagem policial se apoia exclusivamente no índice de similaridade de uma câmera com reconhecimento facial (tecnologia que apresentou taxa de falsos positivos superior a 90% em pessoas negras, segundo o relatório do CESeC [F050]), sem checagem prévia de documentos nem confirmação humana independente, a decisão contraria a legislação de proteção de dados, inverte o ônus da prova e expõe pessoas inocentes a constrangimentos graves."*

### Pergunta 10: O que os quatro experimentos laboratoriais comprovaram sobre a confiabilidade técnica de modelos de IA generativa (ChatGPT, Claude, Gemini, Copilot)?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Alucinações, omissão de vulnerabilidades e necessidade de auditoria humana.
- **Resposta Sugerida**:
  > *"Os experimentos evidenciaram que modelos de linguagem operam por aproximação probabilística de texto, sem garantias formais de exatidão. O ChatGPT gerou uma rota de autenticação JWT sem mecanismo de rate limiting, permitindo ataques de força bruta. O Claude sugeriu uma regra de iptables aplicando a política de bloqueio antes de liberar a porta SSH, o que derrubaria o acesso remoto ao servidor. O Gemini cometeu um erro aritmético ao calcular a soma de dados de candidatos. E o Copilot teve dificuldade em apontar a nulidade de cláusulas contratuais abusivas perante o Código de Defesa do Consumidor e a LGPD. A conclusão prática é que a IA auxilia no rascunho de código e documentação, mas testes automatizados e revisão técnica humana são indispensáveis."*

### Pergunta 11: Como o grupo tratou a dimensão do Green IT e o impacto ambiental do processamento em nuvem na matriz de riscos éticos?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Sustentabilidade computacional e eficiência energética.
- **Resposta Sugerida**:
  > *"Catalogamos essa questão na matriz de riscos sob o código RSK-E08. Servidores em nuvem e modelos de inteligência artificial de grande porte demandam alto consumo de energia elétrica e água para refrigeração. No projeto ÁguaViva PB, adotamos uma estratégia alinhada aos princípios de Green IT: priorizamos o processamento no navegador do usuário com JavaScript nativo e Service Workers, aplicamos cache local para evitar requisições repetidas ao servidor e evitamos o uso de modelos de IA para tarefas que podem ser resolvidas com cálculos simples e código determinístico."*

---

## Bloco 5: Diagnóstico Socioambiental na Paraíba (Etapa 4)

### Pergunta 12: Quais dados oficiais fundamentaram a escolha do problema de água e saneamento em detrimento do descarte de lixo eletrônico ou fraudes financeiras?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Microdados do Censo IBGE 2022, SNIS e DATASUS.
- **Resposta Sugerida**:
  > *"Baseamo-nos em dados públicos e oficiais. O Censo 2022 do IBGE [F070] registrou que 50,9% dos lares paraibanos não contam com ligação à rede geral de esgoto. O Sistema Nacional de Informações sobre Saneamento [F071] indicou que 47% da água tratada no estado se perde nas tubulações antes de chegar aos usuários. Além disso, dados do DATASUS [F072] mostram a relação entre a falta d'água e o aumento de internações por doenças diarreicas em comunidades vulneráveis. Ao comparar as opções na matriz de decisão multicritério, a temática de água e saneamento obteve nota 9,05, superando a gestão de lixo eletrônico (8,20) e a prevenção a fraudes (7,63), tanto pela gravidade social quanto pela viabilidade técnica para a equipe."*

### Pergunta 13: Como o Diagrama de Ishikawa ajudou a estruturar o escopo do projeto sem prometer intervenções físicas que cabem à concessionária?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Análise de causa-raiz e delimitação estrita de escopo em engenharia.
- **Resposta Sugerida**:
  > *"O Diagrama de Ishikawa estruturou as causas em cinco categorias: infraestrutura, governança, clima, métodos e cidadania. Essa análise ajudou a definir os limites do nosso projeto. Como estudantes de desenvolvimento de software, não cabe à nossa equipe substituir tubulações físicas da rede pública ou gerenciar reservatórios. Nosso foco concentrou-se na camada de informação e acesso: criar uma ferramenta digital acessível, que funcione sem internet contínua e permita ao cidadão relatar problemas, acompanhar a situação do bairro e solicitar suporte emergencial quando necessário."*

### Pergunta 14: Como a persona da Dona Maria de Fátima influenciou as decisões de engenharia da solução?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Design Centrado no Usuário (UCD) e personas orientadas a dados.
- **Resposta Sugerida**:
  > *"A Dona Maria de Fátima representa uma pessoa de 52 anos, moradora de comunidade periférica em João Pessoa, com aparelho celular básico e conexão móvel pré-paga que oscila frequentemente. Se o projeto dependesse de um aplicativo pesado de loja virtual e conexão 4G constante, ela não conseguiria utilizar o sistema. A definição dessa persona guiou os requisitos centrais: criar uma aplicação web progressiva (PWA) leve, capaz de salvar denúncias offline no aparelho, com botões amplos, alto contraste e textos claros, sem jargões de informática."*

---

## Bloco 6: Arquitetura e Engenharia da Solução ÁguaViva PB (Etapa 5)

### Pergunta 15: Por que a equipe escolheu a abordagem Progressive Web App (PWA) e a arquitetura Offline-First em vez de um aplicativo nativo para Android/iOS?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: PWA, Service Workers, economia de dados e compatibilidade multiplataforma.
- **Resposta Sugerida**:
  > *"A escolha por um PWA evitou a necessidade de download em lojas virtuais, economizando espaço no celular e franquia de dados. O usuário acessa pelo navegador e pode adicionar o ícone à tela inicial. O funcionamento offline foi implementado com Service Workers e IndexedDB: a página carrega os recursos necessários no primeiro acesso e, caso o usuário esteja sem sinal ao preencher um chamado, os dados e a foto ficam armazenados localmente no navegador. Assim que a conexão for restabelecida, os registros são transmitidos automaticamente ao backend em nuvem, evitando perda de relatos."*

### Pergunta 16: Como foi garantida a segurança da informação e a privacidade dos dados das denúncias no banco de dados IndexedDB local?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Criptografia em repouso (Web Crypto API) e pseudonimização da LGPD.
- **Resposta Sugerida**:
  > *"Seguimos os princípios de privacidade desde a concepção (Privacy by Design). O aplicativo permite registrar relatos sem exigir CPF, nome completo ou dados bancários. No mapa público, as ocorrências são agrupadas por bairro ou setor censitário, sem expor o endereço exato ou a identidade do morador. Antes do envio das imagens, os metadados de localização e da câmera (EXIF) são removidos pelo sistema. Além disso, a transmissão ocorre sob conexão segura HTTPS/TLS 1.3 e o armazenamento temporário no navegador segue a política de mesma origem."*

### Pergunta 17: O que motivou a adoção da técnica MoSCoW e da sintaxe BDD para a especificação dos requisitos?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Engenharia de Requisitos ágil e Behavior-Driven Development.
- **Resposta Sugerida**:
  > *"A técnica MoSCoW nos ajudou a organizar as prioridades entre os 12 requisitos funcionais, separando recursos centrais como o registro offline e a consulta do mapa (classificados como Must Have) de itens para versões futuras, como integração com telemetria de sensores físicos (Won't Have). Já o uso de BDD com a sintaxe Dado-Quando-Então nas histórias de usuário aproximou as regras de uso dos critérios de teste. Cada cenário de aceite escrito nesse formato pode ser validado diretamente em rotinas de teste automatizado, reduzindo divergências entre o comportamento esperado pelo usuário e a implementação do código."*

---

## Bloco 7: Testes de Usabilidade, Validação e Aperfeiçoamento (Etapa 6)

### Pergunta 18: Como foi calculado o escore SUS de 84,2 pontos e qual é o significado metodológico dessa pontuação na literatura de Interação Humano-Computador?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Escala de Usabilidade do Sistema (Brooke, 1996; Bangor et al., 2008).
- **Resposta Sugerida**:
  > *"O cálculo do questionário SUS utiliza dez afirmativas pontuadas de 1 a 5. Nas perguntas ímpares, subtrai-se 1 da nota indicada; nas perguntas pares, subtrai-se a resposta do valor 5. Os valores ajustados são somados e multiplicados por 2,5, convertendo o resultado para uma escala de 0 a 100. Nossa média consolidada foi de 84,2 pontos. Na literatura de Brooke e nas referências de Sauro e Lewis, a média de sistemas em geral fica em torno de 68 pontos. Um escore de 84,2 posiciona o protótipo na faixa de classificação 'Excelente' (Grau A), indicando boa aceitação da interface e facilidade de navegação entre os voluntários testados."*

### Pergunta 19: Por que a amostra de testes de usabilidade contou com 6 participantes e quais são as limitações estatísticas desse tamanho amostral?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Modelo de Descoberta de Falhas de Nielsen & Landauer (1993).
- **Resposta Sugerida**:
  > *"Apoiamos o tamanho da amostra no modelo de Nielsen e Landauer (1993) [F081], que indica que testes com cinco a seis participantes conseguem detectar cerca de 80% a 85% dos principais problemas de usabilidade de uma interface. Ressaltamos, porém, que uma amostra de seis voluntários tem objetivo formativo e qualitativo, não permitindo generalizações estatísticas para toda a população do estado. O objetivo principal foi identificar atritos de navegação e falhas ergonômicas antes de avançar para um teste em escala maior."*

### Pergunta 20: Cite a principal melhoria implementada no protótipo após os testes com os voluntários e explique a justificativa ergonômica dessa mudança.
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Heurística de Correspondência com o Mundo Real e WCAG.
- **Resposta Sugerida**:
  > *"A principal melhoria ocorreu na mensagem do modo offline. Na primeira versão do protótipo, a interface exibia um aviso técnico: 'Cache IndexedDB ativo. Sincronização pendente via API REST'. Durante o teste com o participante P3, de 64 anos, ele relatou receio de ter cometido um erro ou perdido os dados. Na versão revisada, trocamos o aviso por uma frase direta e acessível: 'Tudo salvo no seu celular! Não se preocupe: assim que o sinal voltar, enviamos seu chamado sozinho'. Essa mudança atende à segunda heurística de Nielsen, que orienta a correspondência entre o sistema e o mundo real, usando vocabulário familiar ao usuário em vez de termos internos de desenvolvimento."*
