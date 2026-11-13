---
id: roteiro-apresentacao-slides
etapa: 7
titulo: Roteiro e Script de Apresentação Oral em Slides (Centrado no Impacto Social)
projeto: Laboratório de Carreira e Inovação Responsável em TI - ÁguaViva PB
instituicao: UNIPÊ - Centro Universitário de João Pessoa
curso: CST em Análise e Desenvolvimento de Sistemas
equipe:
  - Gabriel Amancio (Desenvolvimento de Software)
  - Luiz Miguel (Infraestrutura e Redes)
  - Paulo Germano (Dados e IA)
  - Gustavo Antonio (Segurança da Informação)
tempo_total_estimado: "25 a 30 minutos (18 a 20 min de slides + 5 a 7 min de demonstração do protótipo) + 10 min de arguição"
ferramenta_slides: Figma / Google Slides
---

# Roteiro Oficial de Apresentação e Script de Defesa Oral

## Estrutura da Apresentação (10 Slides — Fio Condutor Social e Aderência ao Desafio Prático)

| Slide | Bloco Temático | Orador Titular | Tempo Alocado | Foco do Conteúdo |
|---|---|---|---|---|
| **01** | Capa e Propósito Social | Paulo Germano | 1 min | Equipe, curso, instituição e missão social do ÁguaViva PB |
| **02** | A Dor Real na Paraíba: Água, Saúde e Exclusão | Paulo Germano | 2 min | Censo IBGE 2022, SNIS, DATASUS e barreira burocrática atual |
| **03** | Quem Sofre na Ponta, Causas e Escolha do ODS 6 | Gustavo Antonio | 2 min | Personas (Dona Maria e ACS), Ishikawa e Matriz de Decisão |
| **04** | Do Mercado às Competências Aplicadas (Missão 1 → 2) | Paulo Germano & Luiz Miguel | 2 min | 24 vagas, 4 PDIs SMART, rodízio de liderança e ponte social |
| **05** | Ética, Proteção ao Vulnerável e Inclusão Digital | Gustavo Antonio | 2 min | Casos CESeC/ANPD, LGPD, mediação comunitária e 8 riscos |
| **06** | Como o ÁguaViva PB Ajuda na Prática | Gabriel Amancio | 2 min | Denúncia em 2 passos sem CPF, carro-pipa e modo offline real |
| **07** | Telas do Protótipo e Acessibilidade Universal | Gabriel Amancio | 2 min | 8 telas (`TEL-01` a `TEL-08`), botões 48px, alto contraste e demo |
| **08** | O Choque com a Realidade: Testes com Voluntários | Luiz Miguel | 2 min | 6 voluntários (36 tarefas), SUS 84,2 e dificuldades de P1 e P3 |
| **09** | O Que Mudamos para Incluir de Verdade (v1.0 → v2.0) | Luiz Miguel | 2 min | Humanização do aviso offline, botão fixo, zoom tátil e vibração |
| **10** | Limitações Honestas, Aprendizados e Próximos Passos | Todos | 2 min | Limites da solução/amostra, 24 diários e abertura para arguição |

---

## Script Detalhado por Slide

### Slide 01: Capa e Propósito Social
- **Visual sugerido**: Logo institucional do UNIPÊ, título (*Laboratório de Carreira e Inovação Responsável em TI: Solução ÁguaViva PB*), subtítulo voltado à cidadania hídrica na Paraíba e identificação dos 4 discentes com suas áreas de atuação.
- **Orador**: Paulo Germano (1 minuto).
- **Fala oral sugerida**:
  > *"Boa noite aos professores da banca avaliadora, aos colegas e a todos os presentes. Somos estudantes do curso de Análise e Desenvolvimento de Sistemas do UNIPÊ. Nossa equipe é formada por Gabriel Amancio (Desenvolvimento), Luiz Miguel (Infraestrutura e Redes), Gustavo Antonio (Segurança da Informação) e por mim, Paulo Germano (Dados e IA). Hoje apresentamos o Projeto Integrador que conectou o que o mercado exige de profissionais de TI a um problema urgente do nosso estado: a falta de água potável, a precariedade do saneamento e a dificuldade que comunidades periféricas e rurais da Paraíba enfrentam até mesmo para conseguir denunciar essa situação."*

---

### Slide 02: A Dor Real na Paraíba: Água, Saúde e Exclusão
- **Visual sugerido**: 3 cards de impacto humano e 1 bloco destacando a barreira burocrática:
  - **50,92%** dos lares da PB sem rede geral de esgoto e **1,4 milhão de pessoas** descartando em fossas rudimentares ou valas a céu aberto (88 mil só em João Pessoa) — Censo IBGE 2022.
  - **8 dos 10 municípios** com pior atendimento hídrico do Brasil estão na Paraíba (como Santa Cecília e Baraúna) + **47,0%** de água tratada perdida na rede — IBGE / SNIS Trata Brasil.
  - **Crianças de 0 a 5 anos e idosos** internados por doenças diarreicas agudas (DATASUS).
  - **Barreira invisível:** canais atuais das concessionárias exigem **número de matrícula da conta**, o que exclui famílias de áreas irregulares ou sem ligação formal.
- **Orador**: Paulo Germano (2 minutos).
- **Fala oral sugerida**:
  > *"Antes de pensar em código ou telas, fomos olhar para o problema real na Paraíba. O Censo 2022 do IBGE mostra que mais da metade dos lares paraibanos — 50,92% — não tem rede de esgoto, e cerca de 1,4 milhão de pessoas convivem com fossas rudimentares ou valas a céu aberto. Além disso, 8 dos 10 municípios brasileiros com pior atendimento hídrico ficam aqui no estado, e 47% da água tratada se perde antes de chegar às torneiras. Na ponta, quem paga a conta são crianças pequenas e idosos, que lotam hospitais por doenças diarreicas registradas no DATASUS. E há uma barreira pouco falada: para abrir um chamado hoje na concessionária, exige-se o número de matrícula da conta, excluindo justamente as famílias mais vulneráveis que não têm ligação formal ou crédito no celular para esperar em ligações."*

---

### Slide 03: Quem Sofre na Ponta, Causas e Escolha do ODS 6
- **Visual sugerido**: Retrato das duas personas principais (**Dona Maria de Fátima**, 52 anos, Mandacaru, celular Android básico pré-pago sem internet contínua; e **Carlos Eduardo**, 29 anos, Agente Comunitário de Saúde), síntese do Diagrama de Ishikawa (infraestrutura, gestão opaca, subnotificação e vulnerabilidade social) e quadro da Matriz Multicritério (Água e Saneamento / ODS 6 eleito com **9,05** vs. Desperdício de Alimentos / ODS 2 e 12 com **8,20** e Alagamentos / ODS 11 e 13 com **7,63**).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 4, comparamos três problemas socioambientais da Paraíba em uma matriz ponderada: desperdício de alimentos (8,20), alagamentos em encostas (7,63) e crise hídrica e saneamento (9,05), que selecionamos por sua gravidade e viabilidade em ADS. Mapeamos as causas no Diagrama de Ishikawa e demos rosto ao problema com personas reais: a Dona Maria de Fátima, moradora de comunidade periférica que passa dias sem água, usa um celular simples pré-pago e não sabe a quem recorrer; e o Carlos Eduardo, Agente Comunitário de Saúde que vê casos repetidos de diarreia infantil na rua e precisa de dados organizados para cobrar providências da vigilância sanitária."*

---

### Slide 04: Do Mercado às Competências Aplicadas (Missão 1 → Missão 2)
- **Visual sugerido**: Fluxo conectando **Mercado (Etapa 1: 24 vagas)** → **Formação da Equipe (Etapa 2: 11 competências, 12 metas SMART)** → **Solução Social (ÁguaViva PB)**, com gráfico compacto das top exigências (`SQL 45,8%`, `Git/GitHub 29,2%`, `Python 29,2%`, `Comunicação Clara 29,2%`, `87,5%` remotas) e menção ao rodízio de liderança do grupo nas 7 etapas.
- **Orador**: Paulo Germano (1 min) e Luiz Miguel (1 min).
- **Fala oral sugerida**:
  > *"Para cumprir a segunda missão do projeto com qualidade, começamos investigando 24 vagas reais de estágio e nível júnior no Brasil (6 por área da equipe, sendo 87,5% remotas). Vimos que o mercado exige base sólida em SQL (45,8%), Git (29,2%), Python (29,2%), comunicação clara (29,2%), além de nuvem, Linux e LGPD. Ao comparar essas exigências com nossa autoavaliação de 11 competências, identificamos um gap coletivo em nuvem e contêineres (média 2,75 de 5) e definimos 12 metas SMART com foco em certificações (Oracle Java, AWS, Power BI PL-300, Enap LGPD e Security+) e comunidades locais da Paraíba (GDG João Pessoa, DevOpsDays PB, Python Nordeste e OWASP). Mais importante: alternamos a liderança a cada etapa e transformamos cada especialidade em resposta a uma barreira social — dados para cruzar denúncias com o DATASUS, front-end para acessibilidade, infraestrutura para funcionar sem internet e segurança para proteger o denunciante."*

---

### Slide 05: Ética, Proteção ao Vulnerável e Inclusão Digital
- **Visual sugerido**: 2 blocos: (1) Lições de casos reais no Brasil (**CESeC**: >90% de presos por reconhecimento facial eram negros, violando o Art. 20 da LGPD; **ANPD vs. Meta**: suspensão de uso de dados para IA sem transparência/opt-out); (2) **Como os 8 riscos da matriz protegem o cidadão no ÁguaViva PB** (anonimato sem CPF, proteção contra retaliação, inclusão de quem não tem smartphone via ACS/lideranças, linguagem simples e baixo consumo de dados/energia).
- **Orador**: Gustavo Antonio (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 3, estudamos casos reais no Brasil — como a pesquisa do CESeC sobre viés racial em reconhecimento facial e a intervenção da ANPD contra a Meta — para não repetir erros éticos no nosso sistema. Ao trazer essa reflexão para a realidade das periferias, mapeamos oito riscos e fizemos perguntas difíceis: e se um morador sofrer retaliação por denunciar esgoto clandestino na rua? Por isso, o ÁguaViva PB não coleta CPF, RG nem telefone, agregando os relatos por bairro sob a LGPD. E quem não tem celular nem internet? Preparamos fluxos para que Agentes Comunitários de Saúde e lideranças de bairro registrem demandas coletivas pelas famílias, garantindo que a tecnologia não exclua justamente quem mais precisa."*

---

### Slide 06: Como o ÁguaViva PB Ajuda na Prática
- **Visual sugerido**: Jornada cidadã em 4 cartões simples de benefício humano:
  1. **Denúncia em 2 passos sem cadastro:** relatar falta d'água, água barrenta ou esgoto a céu aberto sem matrícula da CAGEPA.
  2. **Funciona mesmo sem crédito de internet:** o relato fica salvo no celular e é enviado assim que houver sinal.
  3. **Pedido emergencial de Carro-Pipa:** prioridade para creches, escolas e postos de saúde sem água.
  4. **Transparência e Saúde:** mapa de potabilidade do bairro e guia simples de fervura/cloração caseira.
  *(Nota de rodapé discreta: 12 RF MoSCoW, 8 RNF, 8 histórias BDD; protótipo navegável em HTML/CSS/JS + especificação de 8 telas e arquitetura-alvo PWA offline-first).*
- **Orador**: Gabriel Amancio (2 minutos).
- **Fala oral sugerida**:
  > *"O ÁguaViva PB foi projetado para caber na rotina de quem está sem água. Em até dois passos, sem pedir login, CPF ou matrícula da conta, o morador informa se a torneira secou, se a água veio barrenta ou se há esgoto aberto, podendo anexar uma foto leve. Se estiver sem sinal ou sem crédito de celular, o sistema guarda o pedido no próprio aparelho para enviar depois. Além disso, a comunidade pode acompanhar o mapa do bairro, consultar cuidados básicos para tratar a água em casa e acionar pedidos emergenciais de carro-pipa para creches e postos de saúde. Toda a solução foi modelada com 12 requisitos funcionais, 8 não funcionais e histórias de usuário voltadas à arquitetura offline-first."*

---

### Slide 07: Telas do Protótipo e Acessibilidade Universal (Demo ao Vivo)
- **Visual sugerido**: Mosaico limpo das 8 telas estruturais (`TEL-01` a `TEL-08`) destacando ergonomia inclusiva: botões grandes de **48×48 px**, **alto contraste (>14:1)** para ler sob sol forte, ampliação de fonte em **+200%** e linguagem acolhedora. Chamada visual para a **Demonstração do Protótipo**.
- **Orador**: Gabriel Amancio (2 minutos + condução da demonstração ao vivo de 5 a 7 minutos).
- **Fala oral sugerida**:
  > *"Como muitas pessoas do nosso público-alvo usam celulares simples na rua, sob sol forte, ou têm dificuldade visual e motora, aplicamos a diretriz WCAG 2.2 AA desde o primeiro rascunho: botões grandes com área mínima de 48 por 48 pixels, modo de alto contraste e texto ampliável em até 200%. Vamos agora demonstrar ao vivo a navegação pelas telas do protótipo, simulando uma denúncia na Ilha do Bispo e o comportamento em modo offline."*

---

### Slide 08: O Choque com a Realidade: Testes com Voluntários
- **Visual sugerido**: Quadro dos **6 voluntários reais** (P1 a P6, de 23 a 64 anos, com TCLE e anonimização) e métricas da ISO 9241-11 (**97,2% de conclusão** em 36 tarefas, tempo médio **59,4 s**, **escore SUS 84,2 / 100** — Excelente) ao lado do destaque humano das **2 fricções reais descobertas**:
  - **Participante P3 (64 anos, líder comunitário com baixa visão e tremor leve):** travou ao ver o aviso técnico *"Cache IndexedDB ativo; aguardando handshake HTTP"* (achou que perdeu a denúncia) e perdeu o botão de envio quando o teclado do celular abriu.
  - **Participante P1 (52 anos, comerciante periférica):** pediu confirmação por vibração no bolso para não precisar ficar segurando e olhando o celular na rua.
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Na Etapa 6, colocamos o protótipo à prova com seis voluntários adultos de perfis diferentes — entre 23 e 64 anos — incluindo uma comerciante periférica, uma agente de saúde, uma professora e um líder comunitário idoso, todos com termo de consentimento assinado. Mesmo atingindo 97,2% de conclusão das 36 tarefas e pontuação SUS de 84,2, os testes revelaram falhas que nós, como alunos de TI, não tínhamos percebido: o participante idoso P3 ficou assustado ao ler uma mensagem técnica falando em 'Cache IndexedDB' e não encontrou o botão de enviar escondido atrás do teclado virtual; já a participante P1 sugeriu um aviso por vibração para poder guardar o celular no bolso na rua."*

---

### Slide 09: O Que Mudamos para Incluir de Verdade (v1.0 → v2.0)
- **Visual sugerido**: Comparativo visual "Antes × Depois" das 4 melhorias implementadas após os testes:
  1. **Linguagem humana (`TEL-07`):** de *"Cache IndexedDB ativo..."* → para *"Tudo salvo no celular! Enviaremos automaticamente quando o sinal voltar."*
  2. **Botão sempre visível (`TEL-03`):** botão de envio fixado na barra inferior (`sticky bottom`) mesmo com o teclado aberto.
  3. **Zoom acessível (`TEL-04`):** botões táteis `+` e `-` de 48×48 px no mapa para quem não consegue fazer gesto de pinça.
  4. **Leitura no sol e bolso (`TEL-05`/`TEL-07`):** legendas aumentadas para 13 px em alto contraste e confirmação por vibração suave.
- **Orador**: Luiz Miguel (2 minutos).
- **Fala oral sugerida**:
  > *"Cada dificuldade observada virou uma correção concreta na versão 2.0 do protótipo. Tiramos todo jargão técnico das mensagens de tela para tranquilizar quem está sem internet; fixamos o botão de envio no rodapé para nunca sumir atrás do teclado; colocamos botões grandes de mais e menos no mapa para ajudar idosos e pessoas com tremor nas mãos; e ampliamos as legendas dos gráficos com previsão de resposta por vibração. Foi nesse momento que entendemos na prática que usabilidade é inclusão social."*

---

### Slide 10: Limitações Honestas, Aprendizados e Impacto
- **Visual sugerido**: 2 colunas claras:
  - **Limitações explicitadas:** (1) Um software não gera água nem conserta tubulações — ele transforma queixas invisíveis em evidência coletiva para cobrar concessionárias e Defesa Civil; (2) Famílias sem smartphone continuam dependendo de mediação comunitária (ACS); (3) Avaliação exploratória limitada a `N=6` na Região Metropolitana de João Pessoa (sem incluir o semiárido) e fluxo offline simulado no protótipo.
  - **Diários e Próximos Passos:** síntese dos **24 registros nos Diários de Aprendizagem** (6 por integrante, ≥ 2 novas ferramentas por estudante) e evolução futura do ÁguaViva PB.
- **Orador**: Todos os 4 Integrantes (2 minutos).
- **Falas orais sugeridas**:
  - **Gustavo Antonio**: *"Temos clareza dos limites do projeto: um aplicativo não cria água na torneira, mas transforma reclamações isoladas e ignoradas em dados coletivos auditáveis para cobrar o poder público e priorizar caminhões-pipa."*
  - **Paulo Germano**: *"Também reconhecemos que nossa amostra de testes foi exploratória e restrita à Grande João Pessoa, sem cobrir ainda o semiárido paraibano, além da dependência de mediação comunitária para quem não possui smartphone."*
  - **Gabriel Amancio**: *"Ao longo das sete etapas e dos 24 registros nos diários individuais, cada integrante dominou novas ferramentas e aprendeu a colocar o usuário vulnerável no centro de cada decisão técnica."*
  - **Luiz Miguel**: *"Agradecemos aos professores do UNIPÊ pela orientação e nos colocamos à disposição da banca examinadora para a arguição individual."*
