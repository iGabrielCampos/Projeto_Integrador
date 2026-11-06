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
  > *"Adotamos o rodízio obrigatório de liderança técnica para garantir que todos os quatro integrantes vivenciassem a responsabilidade direta de planejar, delegar e assinar entregáveis formais perante os portões de qualidade. O líder da etapa atuava como o 'Product Owner' daquela entrega, enquanto os outros três atuavam como revisores por pares (Peer Reviewers). Para mitigar gargalos, implementamos um script autônomo em Python (`verificar.py`) que realizava validação determinística contínua antes de cada commit. Se houvesse qualquer lacuna textual ou fonte não catalogada no arquivo `fontes.md`, o commit era bloqueado. Isso conferiu autonomia com rigor metrológico."*

### Pergunta 02: Como o grupo assegurou que o uso de Inteligência Artificial generativa não substituísse a autoria e a aprendizagem dos estudantes?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Integridade acadêmica, ética algorítmica e trilhas de auditoria.
- **Resposta Sugerida**:
  > *"Estabelecemos desde a Etapa 0 uma política rígida de integridade acadêmica. A IA atuou exclusivamente como ferramenta instrumental — para apoio na formatação Markdown, conversão tabular e apoio à diagramação Mermaid. Todo o conteúdo cognitivo e vivencial, como os 24 registros dos Diários de Aprendizagem, os testes reais de usabilidade com os voluntários e as análises críticas, foi produzido exclusivamente por nós. Além disso, mantivemos um log transparente de auditoria em `00_gestao/uso_ia.md`, onde cada interação com LLMs registrou o modelo, o prompt, a resposta e a validação humana aplicada, acompanhado de nossas declarações individuais assinadas em cartório acadêmico."*

---

## Bloco 2: Pesquisa de Mercado de Trabalho em TI (Etapa 1)

### Pergunta 03: Por que a amostragem de vagas foi fixada em exatamente 24 anúncios e como foi garantida a representatividade no Nordeste e Paraíba?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Amostragem estratificada e metodologia de pesquisa de mercado.
- **Resposta Sugerida**:
  > *"Definimos a amostra de 24 vagas estruturada em quatro estratos homogêneos de exatamente 6 vagas para cada especialidade representada no grupo: Desenvolvimento, Infraestrutura, Dados e Segurança. Isso evitou a distorção comum de pesquisas em que vagas de front-end sobrecarregam a amostra. Para garantir aderência ao nosso contexto regional, filtramos vagas ativas entre 08 e 10 de novembro de 2026 em plataformas como Gupy e Indeed, priorizando empresas com presença física em João Pessoa, Campina Grande e Recife, além de posições nacionais remotas que aceitam contratações no Nordeste. Todas as URLs, títulos e datas de acesso estão catalogadas de forma auditável em nosso repositório."*

### Pergunta 04: Qual foi a constatação mais surpreendente na análise das competências técnicas exigidas para vagas de nível Júnior e Estágio?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Análise de frequência de requisitos em editais e anúncios corporativos.
- **Resposta Sugerida**:
  > *"O dado mais impactante foi a onipresença da cultura DevOps e de contêineres Docker mesmo em vagas de estágio e nível júnior, aparecendo em quase 60% dos anúncios analisados. Antes da pesquisa, tínhamos a impressão de que Docker era um conhecimento restrito a analistas plenos ou de infraestrutura avançada. No entanto, o mercado exige que o desenvolvedor júnior já saiba subir sua aplicação em contêineres locais para garantir paridade com o ambiente de testes e homologação em nuvem. Essa constatação reorientou diretamente nossos planos individuais de capacitação."*

### Pergunta 05: Quais foram as principais dores operacionais relatadas pelas empresas contratantes na pesquisa de mercado?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Mapeamento de desafios do mercado de TI corporativo.
- **Resposta Sugerida**:
  > *"Identificamos cinco dores críticas recorrentes: a necessidade de modernizar monólitos legados para microsserviços sem indisponibilidade; a pressão regulatória da ANPD para adequação de sistemas à LGPD; a gestão de custos descontrolados de computação em nuvem (FinOps); a fragmentação e má qualidade de dados cadastrais; e a escassez de profissionais iniciantes que possuam comunicação assertiva e capacidade de dialogar além de sua própria linha de código."*

---

## Bloco 3: Identidade Profissional, Autoavaliação e PDI (Etapa 2)

### Pergunta 06: Como a matriz de competências da equipe permitiu identificar os 'gaps' compartilhados e qual foi a estratégia para superá-los?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Matriz de autoavaliação, curva de proficiência e aprendizagem colaborativa.
- **Resposta Sugerida**:
  > *"Ao tabularmos nossas autoavaliações em 11 competências padronizadas numa escala de 1 a 5, notamos que a equipe possuía média alta em lógica de programação (3,75), versionamento com Git (4,13) e comunicação em grupo (4,50). Todavia, a competência de orquestração de nuvem e contêineres Docker pontuou apenas 2,75, configurando um gap coletivo prioritário. Para superá-lo, definimos que a arquitetura da nossa solução na Etapa 5 deveria ser conteinerizada em Docker e que eu, como líder da área de infraestrutura, apoiaria os demais discentes na criação de ambientes virtuais controlados, integrando também workshops práticos em nossos PDIs."*

### Pergunta 07: Qual é a diferença prática entre uma meta genérica e uma meta SMART no contexto de carreira em tecnologia?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Metodologia SMART (Doran, 1981).
- **Resposta Sugerida**:
  > *"Uma meta genérica é apenas um desejo abstrato, como por exemplo: 'quero aprender computação em nuvem'. Ela não possui prazo, nem métrica objetiva de comprovação. Uma meta SMART é estruturada em cinco pilares: Específica, Mensurável, Atingível, Relevante e Temporalmente delimitada. No meu caso particular, a meta foi formulada como: 'Obter a certificação oficial AWS Certified Cloud Practitioner (CLF-C02) até 31 de maio de 2027, dedicando 6 horas semanais de estudo no AWS Skill Builder e realizando três simulados com aproveitamento superior a 80%'. A meta SMART estabelece o método, a régua de sucesso e o horizonte temporal inegociável."*

### Pergunta 08: De que maneira as comunidades técnicas locais de João Pessoa e da Paraíba foram incorporadas ao plano profissional do grupo?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Comunidades de prática (Wenger) e networking profissional regional.
- **Resposta Sugerida**:
  > *"Mapeamos que a formação profissional em TI não se esgota nas salas de aula. Catalogamos em nosso repositório comunidades ativas no nosso estado, como o GDG João Pessoa, o capítulo da OWASP João Pessoa, a comunidade Python Nordeste e o DevOpsDays PB. Inserimos em nossos PDIs a participação periódica nesses meetups e conferências, permitindo que a equipe receba mentorias de profissionais seniores, compartilhe projetos autorais de código aberto e monitore as oportunidades de contratação geradas no ecossistema de inovação paraibano."*

---

## Bloco 4: Ética, Riscos Algorítmicos e Experimentos com IA (Etapa 3)

### Pergunta 09: No caso do reconhecimento facial investigado pelo CESeC, qual artigo da LGPD é violado quando uma pessoa é detida exclusivamente por indicação do algoritmo?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: LGPD (Lei nº 13.709/2018, Art. 20) e direitos fundamentais.
- **Resposta Sugerida**:
  > *"O caso viola frontalmente o Artigo 20 da LGPD, que assegura expressamente ao titular dos dados o direito de solicitar a revisão de decisões tomadas unicamente com base em tratamento automatizado de dados pessoais que afetem seus interesses, incluídas as decisões destinadas a definir o seu perfil pessoal ou profissional. Quando as forças de segurança detêm um cidadão baseadas unicamente na pontuação de similaridade de uma câmera inteligente — cuja taxa de falsos positivos em indivíduos negros supera 90%, como comprovou o CESeC —, sem a devida checagem documental e validação humana independente, há violação da lei, inversão inconstitucional do ônus da prova e desrespeito à dignidade da pessoa humana."*

### Pergunta 10: O que os quatro experimentos laboratoriais comprovaram sobre a confiabilidade técnica de modelos de IA generativa (ChatGPT, Claude, Gemini, Copilot)?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Alucinações, omissão de vulnerabilidades e necessidade de auditoria humana.
- **Resposta Sugerida**:
  > *"Os experimentos provaram empiricamente que LLMs são modelos probabilísticos de geração de linguagem, e não motores de validação técnica formal. O ChatGPT gerou código de autenticação JWT sem proteção contra força bruta (falta de rate limiting). O Claude inverteu a ordem de regras de iptables, o que causaria bloqueio remoto acidental de portas essenciais. O Gemini errou uma soma aritmética tabular por uma diferença de R$ 380,00 reais. E o Copilot vacilou ao analisar cláusulas contratuais abusivas. Concluímos que a IA é excelente para gerar rascunhos e acelerar o raciocínio inicial, mas nunca pode substituir o teste automatizado, a depuração e o ceticismo profissional do engenheiro de software."*

### Pergunta 11: Como o grupo tratou a dimensão do Green IT e o impacto ambiental do processamento em nuvem na matriz de riscos éticos?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Sustentabilidade computacional e eficiência energética.
- **Resposta Sugerida**:
  > *"Mapeamos esse risco formalmente sob o código RSK-E05 em nossa matriz. Modelos generativos de grande porte e data centers consomem volumes colossais de energia elétrica e milhões de litros de água para resfriamento de servidores. Para mitigar esse impacto em nossa solução ÁguaViva PB, adotamos arquitetura que privilegia o processamento do lado do cliente (Edge/Client-Side) no próprio navegador móvel via JavaScript nativo e Service Workers, evitando requisições redundantes a servidores em nuvem e dispensando o uso de inferências de IA desnecessárias para tarefas que podem ser resolvidas com algoritmos determinísticos convencionais."*

---

## Bloco 5: Diagnóstico Socioambiental na Paraíba (Etapa 4)

### Pergunta 12: Quais dados oficiais fundamentaram a escolha do problema de água e saneamento em detrimento do descarte de lixo eletrônico ou fraudes financeiras?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Microdados do Censo IBGE 2022, SNIS e DATASUS.
- **Resposta Sugerida**:
  > *"Utilizamos microdados governamentais incontestáveis. O Censo 2022 do IBGE apontou que 50,9% dos lares da Paraíba não possuem conexão à rede geral de esgoto. O Sistema Nacional de Informações sobre Saneamento (SNIS) revelou que o estado perde 47% de toda a água tratada na distribuição física. E os relatórios de internação hospitalar do DATASUS demonstraram uma correlação direta entre picos de desabastecimento em áreas periféricas e o aumento de doenças diarreicas agudas em crianças menores de cinco anos. Quando submetemos as três opções à Matriz de Decisão Multicritério com pesos ponderados, o tema da água e saneamento obteve nota 9,05, enquanto lixo eletrônico alcançou 7,05 e fraudes obteve 7,80."*

### Pergunta 13: Como o Diagrama de Ishikawa ajudou a estruturar o escopo do projeto sem prometer intervenções físicas que cabem à concessionária?
- **Titular Recomendado**: Paulo Germano (Dados e IA)
- **Fundamentação**: Análise de causa-raiz e delimitação estrita de escopo em engenharia.
- **Resposta Sugerida**:
  > *"O diagrama de causa e efeito de Ishikawa organizou as causas em 5 espinhas: infraestrutura, governança, clima, métodos e tecnologia. Isso permitiu que a equipe enxergasse com clareza a fronteira do nosso escopo. Como discentes de software, não temos o poder nem a competência técnica de trocar os canos de amianto obsoletos da concessionária ou perfurar poços artesianos no semiárido. Contudo, podemos solucionar a falha de governança e métodos: a falta de um canal cívico transparente, bidirecional e funcional offline para que a população periférica fiscalize, registre ocorrências e acione suporte emergencial da Defesa Civil. Delimitamos o escopo estritamente no software cidadão."*

### Pergunta 14: Como a persona da Dona Maria de Fátima influenciou as decisões de engenharia da solução?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Design Centrado no Usuário (UCD) e personas orientadas a dados.
- **Resposta Sugerida**:
  > *"A Dona Maria de Fátima é uma senhora de 52 anos que mora na periferia de João Pessoa, utiliza um celular Android de entrada e possui um plano móvel pré-pago sem franquia de dados ativa quando o saldo expira. Se tivéssemos desenhado um aplicativo convencional que exige download de 150 MB na Google Play Store e conexão permanente à internet 4G, ela estaria sumariamente excluída do sistema. A persona dela nos impôs os requisitos inegociáveis do projeto: ser um Progressive Web App leve de até 1,8 MB, com operação offline-first, botões grandes e linguagem popular que não exija conhecimentos avançados de tecnologia."*

---

## Bloco 6: Arquitetura e Engenharia da Solução ÁguaViva PB (Etapa 5)

### Pergunta 15: Por que a equipe escolheu a abordagem Progressive Web App (PWA) e a arquitetura Offline-First em vez de um aplicativo nativo para Android/iOS?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: PWA, Service Workers, economia de dados e compatibilidade multiplataforma.
- **Resposta Sugerida**:
  > *"A escolha do PWA eliminou a barreira de instalação de lojas de aplicativos, que consomem memória e dados preciosos dos cidadãos vulneráveis. O usuário acessa uma URL simples e pode salvar o atalho instantaneamente na tela inicial do celular. A arquitetura Offline-First, por sua vez, foi viabilizada tecnicamente pelo Service Worker: os arquivos da interface ficam armazenados em cache local e as denúncias preenchidas sem conexão são gravadas diretamente no banco de dados IndexedDB do navegador móvel. Quando a conectividade é restabelecida, o sistema dispara uma sincronização assíncrona em segundo plano, garantindo que nenhum relato comunitário seja perdido por falta de sinal."*

### Pergunta 16: Como foi garantida a segurança da informação e a privacidade dos dados das denúncias no banco de dados IndexedDB local?
- **Titular Recomendado**: Gustavo Antonio (Segurança da Informação)
- **Fundamentação**: Criptografia em repouso (Web Crypto API) e pseudonimização da LGPD.
- **Resposta Sugerida**:
  > *"Adotamos o princípio do Privacy by Design. As denúncias geradas no PWA não exigem o fornecimento de CPF, nome completo ou dados bancários do cidadão. Para a visualização pública no mapa comunitário, o sistema aplica pseudonimização imediata, agrupando as ocorrências por setor censitário ou quarteirão, impedindo a identificação da residência exata do denunciante para evitar retaliações. Além disso, as fotos e dados em fila no IndexedDB são protegidos pela política de mesma origem (Same-Origin Policy) do navegador e sanitizados antes da transmissão criptografada via HTTPS/TLS 1.3 para o servidor backend."*

### Pergunta 17: O que motivou a adoção da técnica MoSCoW e da sintaxe BDD para a especificação dos requisitos?
- **Titular Recomendado**: Gabriel Amancio (Desenvolvimento de Software)
- **Fundamentação**: Engenharia de Requisitos ágil e Behavior-Driven Development.
- **Resposta Sugerida**:
  > *"A técnica MoSCoW permitiu priorizar cirurgicamente os 12 requisitos funcionais, separando o essencial para a sobrevivência do produto (como a consulta de potabilidade e o envio offline, classificados como Must Have) de funcionalidades secundárias ou futuras (como telemetria IoT, classificada como Won't Have). A sintaxe BDD com o formato Dado-Quando-Então (Given-When-Then) nas 8 histórias de usuário foi fundamental porque ela une a perspectiva de negócio à de testes: cada critério de aceitação escrito em BDD pode ser transformado diretamente em um teste automatizado no framework de homologação, eliminando ambiguidades entre o que o usuário espera e o que o desenvolvedor programa."*

---

## Bloco 7: Testes de Usabilidade, Validação e Aperfeiçoamento (Etapa 6)

### Pergunta 18: Como foi calculado o escore SUS de 84,2 pontos e qual é o significado metodológico dessa pontuação na literatura de Interação Humano-Computador?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Escala de Usabilidade do Sistema (Brooke, 1996; Bangor et al., 2008).
- **Resposta Sugerida**:
  > *"O cálculo do SUS segue uma fórmula psicométrica padronizada sobre 10 afirmativas na escala de 1 a 5. Para as perguntas ímpares (positivas), subtrai-se 1 da nota do usuário; para as pares (negativas), subtrai-se a nota de 5. Em seguida, somam-se todas as pontuações e multiplica-se o resultado por 2,5 para converter o total para uma escala de 0 a 100. Nossa média consolidada de 84,2 pontos possui alto rigor estatístico. Na literatura internacional de Brooke e nos estudos de benchmark de Sauro e Lewis, a média da indústria é de 68 pontos. Uma pontuação de 84,2 classifica o ÁguaViva PB na categoria 'Excelente' (Grade A), posicionando nossa interface no percentil superior a 90% em facilidade de uso e aprendizado intuitivo."*

### Pergunta 19: Por que a amostra de testes de usabilidade contou com 6 participantes e quais são as limitações estatísticas desse tamanho amostral?
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Modelo de Descoberta de Falhas de Nielsen & Landauer (1993).
- **Resposta Sugerida**:
  > *"Nos fundamentamos no clássico modelo matemático de Nielsen e Landauer (1993), que demonstra empiricamente que realizar testes de usabilidade com 5 a 6 usuários representativos é suficiente para identificar aproximadamente 80% a 85% de todos os problemas ergonômicos e gargalos mais severos de uma interface. No entanto, declaramos com absoluta transparência científica em nosso dossiê que uma amostra de N=6 não permite extrapolações estatísticas probabilísticas para toda a população da Paraíba. Trata-se de uma validação qualitativa e formativa, cujo propósito foi detectar fricções reais de navegação antes de levar o software para um piloto populacional amplo."*

### Pergunta 20: Cite a principal melhoria implementada no protótipo após os testes com os voluntários e explique a justificativa ergonômica dessa mudança.
- **Titular Recomendado**: Luiz Miguel (Infraestrutura e Redes)
- **Fundamentação**: Heurística de Correspondência com o Mundo Real e WCAG.
- **Resposta Sugerida**:
  > *"A melhoria mais emblemática ocorreu na tela de aviso do modo offline. No protótipo v1.0, colocamos um alerta com jargão técnico: 'Cache IndexedDB ativo. Sincronização pendente via API REST'. Quando testamos com o Seu João, nosso participante idoso de 64 anos, ele ficou com receio de ter quebrado o aparelho ou de sua denúncia ter sido perdida. Na Versão 2.0 Revisada, substituímos imediatamente o aviso por uma linguagem acolhedora e cidadã: 'Tudo salvo no seu celular! Não se preocupe: assim que o sinal voltar, enviamos seu chamado sozinho'. Isso atendeu diretamente à Heurística nº 2 de Jakob Nielsen, que exige que o sistema fale a língua do usuário, e não a linguagem do desenvolvedor."*
