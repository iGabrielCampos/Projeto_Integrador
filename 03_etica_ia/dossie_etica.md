---
id: dossie-etica-inteligencia-artificial
etapa: 3
autor: Gabriel Amancio, Gustavo Antonio, Paulo Germano, Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F002
  - F003
  - F004
  - F005
  - F007
  - F008
  - F020
  - F021
  - F024
  - F027
  - F050
  - F051
---

# DOSSIÊ MESTRE DA ETAPA 3: INTELIGÊNCIA ARTIFICIAL, ÉTICA TECNOLÓGICA E CIDADANIA DIGITAL

**Instituição:** UNIPÊ – Centro Universitário de João Pessoa  
**Curso:** Superior de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)  
**Disciplina:** Projeto Integrador – Design Profissional  
**Líder da Etapa 3:** Gabriel Amancio (Desenvolvimento de Software)  
**Revisores Pares:** Paulo Germano, Luiz Miguel, Gustavo Antonio  

---

## 1. INTRODUÇÃO E OBJETIVOS DA INVESTIGAÇÃO ÉTICA

A integração de sistemas de Inteligência Artificial generativa e preditiva nas organizações exige análise técnica e ética sobre a responsabilidade social dos futuros profissionais de Análise e Desenvolvimento de Sistemas `[F008]`. Os sistemas de software reproduzem critérios, modelos de dados e decisões de projeto definidos por seus desenvolvedores e gestores `[F021]`.

Nesse contexto, a **Etapa 3** do Projeto Integrador investiga a relação entre inovação tecnológica, integridade ética, cidadania digital e conformidade regulatória no Brasil. O documento consolida quatro eixos investigativos:
1. **Análise Crítica de Dois Casos Reais:** Um estudo sobre sistemas de reconhecimento facial e direitos fundamentais (biometria e viés algorítmico) e um caso focado em governança de privacidade, incidentes de segurança e sanções regulatórias da ANPD sob a LGPD `[F001]`;
2. **Matriz de Riscos Éticos e Operacionais:** Mapeamento de 8 ameaças técnicas e éticas inerentes ao desenvolvimento de sistemas, com causas-raiz e planos de mitigação;
3. **Consolidação dos Experimentos Práticos com Ferramentas de IA:** Avaliação empírica conduzida individualmente pelos quatro integrantes da equipe (Gabriel, Luiz, Paulo e Gustavo), demonstrando limitações, erros de predição e riscos da automação não supervisionada;
4. **Diretrizes para o Desenvolvimento Responsável de Tecnologias:** Recomendações operacionais para orientar a concepção da solução tecnológica nas Etapas 4 e 5.

---

## 2. ANÁLISE CRÍTICA DOS CASOS REAIS DE ÉTICA TECNOLÓGICA

### 2.1 Caso Real 1: Algoritmos de Reconhecimento Facial na Segurança Pública e o Viés Racial no Brasil

#### 2.1.1 Contexto e Organizações Envolvidas
A partir de 2019, secretarias estaduais de segurança pública no Brasil implantaram sistemas de videovigilância com reconhecimento facial em espaços públicos (estações de transporte, vias urbanas e eventos populares) `[F050]`. A tecnologia foi adquirida de fornecedores privados para modernização do trabalho policial e captura de foragidos da justiça. O processo gerou contestações de entidades civis e órgãos de justiça, como o Centro de Estudos de Segurança e Cidadania (CESeC, pelo projeto *O Panóptico*) `[F050]` e as Defensorias Públicas dos Estados do Rio de Janeiro, Bahia, Ceará e da União.

#### 2.1.2 Cronologia dos Acontecimentos e Consequências
- **2019–2021:** Implantação de câmeras com algoritmos biométricos em vias públicas sem audiências públicas ou estudos prévios de impacto aos direitos fundamentais.
- **2021–2024:** Relatórios técnicos consolidados pelas Defensorias Públicas estaduais revelaram que mais de **80% das pessoas presas ou abordadas indevidamente** por falsos positivos do reconhecimento facial eram **homens negros** `[F050]`. Casos documentados registraram cidadãos inocentes detidos por semanas devido a erros de identificação visual automatizada.
- **Consequências:** Violações de direitos fundamentais, estigmatização de minorias e abertura de processos de reparação civil contra o poder público. O Conselho Nacional de Justiça (CNJ) publicou diretrizes que vedam prisões fundamentadas unicamente em reconhecimento fotográfico ou automatizado sem confirmação probatória autônoma.

#### 2.1.3 Problema Ético Central
O problema ético central decorre do **viés algorítmico estrutural e da discriminação algorítmica**. Os modelos de visão computacional foram treinados predominantemente com bases fotográficas de pessoas brancas, apresentando taxas de falsos positivos mais altas na identificação de pessoas negras `[F050]`. A automação das abordagens sem validação humana crítica fragilizou a presunção de inocência e transferiu decisões operacionais a modelos estatísticos opacos.

#### 2.1.4 Enquadramento Legal e Ético
- **Constituição Federal de 1988:** Violação do princípio da dignidade da pessoa humana (art. 1º, III), da igualdade perante a lei (art. 5º, *caput*) e da presunção de inocência (art. 5º, LVII).
- **LGPD (Lei nº 13.709/2018) `[F001]`:** Infração ao art. 6º, IX (Princípio da Não Discriminação: impossibilidade de tratamento para fins discriminatórios ilícitos ou abusivos) e desrespeito ao art. 20 (Direito à revisão por pessoa natural de decisões tomadas unicamente com base em tratamento automatizado).
- **Marco Civil da Internet (Lei nº 12.965/2014) `[F002]`:** Descumprimento das garantias de preservação da privacidade e dos direitos humanos na rede.

---

### 2.2 Caso Real 2: Processos Administrativos Sancionadores da ANPD e o Treinamento Não Autorizado de IA

#### 2.2.1 Contexto e Organizações Envolvidas
Com a entrada em vigor das sanções administrativas da Lei Geral de Proteção de Dados Pessoais `[F001]`, a Autoridade Nacional de Proteção de Dados (ANPD) instaurou processos de fiscalização contra organizações públicas e privadas por vazamentos, comercialização ilícita e coleta excessiva de dados de usuários `[F051]`. As ações incluíram a primeira sanção pecuniária aplicada à empresa Telekall Infoservice (por venda irregular de dados de eleitores sem nomeação de Encarregado de Dados) e a medida preventiva contra a Meta (controladora de Facebook e Instagram), que alterou unilateralmente sua política de privacidade para utilizar publicações, imagens e textos de usuários brasileiros no treinamento de modelos de IA generativa `[F051]`.

#### 2.2.2 Cronologia dos Acontecimentos e Consequências
- **Agosto de 2021:** Entrada em vigor dos artigos 52 a 54 da LGPD relativos a penalidades administrativas.
- **Julho de 2023:** Aplicação da primeira sanção pecuniária pela ANPD no caso Telekall, com multas simples cumulativas e determinação de eliminação de bases ilegais `[F051]`.
- **Julho de 2024:** Expedição de **Medida Cautelar Preventiva** pela Coordenação-Geral de Fiscalização da ANPD com fixação de multa diária de R$ 50 mil, determinando a suspensão da política de privacidade da Meta no Brasil para o treinamento de modelos com dados de titulares locais sem consentimento explícito e sem opção simples de recusa (*opt-out*) `[F051]`.
- **Consequências:** Estabelecimento de parâmetro regulatório nacional indicando que o treinamento de modelos de inteligência artificial em território brasileiro deve respeitar a autodeterminação informativa e a transparência no tratamento de dados pessoais.

#### 2.2.3 Problema Ético Central
O problema ético envolve **privacidade, autonomia individual e consentimento informado**. O uso de publicações e comunicações de usuários para alimentação de modelos proprietários de linguagem sem consentimento prévio e sem opção simples de oposição desrespeita as finalidades originais para as quais as contas haviam sido criadas.

#### 2.2.4 Enquadramento Legal e Ético
- **LGPD (Lei nº 13.709/2018) `[F001]`:** Infração aos artigos 6º, I e VI (Princípios da Finalidade e Transparência), art. 7º (Ausência de base legal legítima para o tratamento de dados pessoais com finalidade distinta da original) e art. 18 (Cerceamento do direito de oposição e livre revogação).
- **Lei de Direitos Autorais (Lei nº 9.610/1998) `[F003]`:** Violação de prerrogativas morais e patrimoniais de autores cujas obras artísticas e textuais foram ingeridas em esteiras de aprendizado de máquina sem créditos ou autorização expressa.

---

## 3. MATRIZ CONSOLIDADA DE RISCOS ÉTICOS E REGULATÓRIOS

A Tabela 1 detalha os 8 riscos prioritários mapeados pelo grupo, estabelecendo a conexão direta entre a causa técnica, o impacto regulatório e a medida de salvaguarda implementada no projeto.

### Tabela 1: Matriz de Riscos Éticos, Regulatórios e Socioambientais do Projeto

| ID | Risco Identificado | Causa Primária | Consequência | Prob. | Impacto | Severidade | Medida de Mitigação | Responsável |
|---|---|---|---|---|---|---|---|---|
| **RSK-E01** | Viés Algorítmico e Discriminação Indireta `[F050]` | Treinamento sobre bases de dados desbalanceadas e históricas | Exclusão de minorias e decisões automatizadas lesivas | Média | Crítico | **Crítico** | Testes de equidade estatística, uso de datasets balanceados e supervisão humana obrigatória (*Human-in-the-Loop*). | Paulo Germano (Dados/IA) |
| **RSK-E02** | Vazamento de Dados e Não Conformidade com a LGPD `[F001]` | Fragilidades em controles de acesso e endpoints expostos | Sanções da ANPD `[F051]`, multas e danos morais a titulares | Média | Alto | **Alto** | *Privacy by Design*, princípio da minimização, uso de HTTPS e segregação de privilégios. | Gustavo Antonio (Segurança) |
| **RSK-E03** | Alucinação Factual e Dependência Cega de LLMs | Limitações probabilísticas de predição de tokens dos modelos | Códigos vulneráveis em produção e decisões baseadas em falsidades | Alta | Alto | **Alto** | Protocolo de checagem factual obrigatória (*fact-checking*), testes em interpretador e log em `uso_ia.md`. | Gabriel Amancio (Dev) |
| **RSK-E04** | Opacidade Algorítmica e Falta de Explicabilidade | Modelos de aprendizado profundo tipo "caixa-preta" sem interpretabilidade | Descumprimento do dever de transparência do Marco Civil `[F002]` | Média | Médio | **Médio** | Adoção de modelos explicáveis, geração de justificativas em linguagem simples e direito a recurso humano. | Paulo Germano (Dados/IA) |
| **RSK-E05** | Barreiras de Acessibilidade Digital | Não atendimento às diretrizes internacionais WCAG 2.2 `[F007]` | Exclusão de pessoas com deficiência e descumprimento legal | Média | Alto | **Alto** | Conformidade estrita com WCAG 2.2 AA, navegação completa por teclado, contraste e testes na Etapa 6. | Gabriel Amancio (Dev) |
| **RSK-E06** | Injeção de Código e Vulnerabilidades em APIs | Falta de sanitização de entradas HTTP (OWASP Top 10 `[F024]`) | Invasão de banco de dados, roubo de credenciais e indisponibilidade | Baixa | Crítico | **Alto** | Validação com schemas estritos (Zod), uso de ORM parametrizado e esteiras automatizadas de SAST. | Gustavo Antonio (Segurança) |
| **RSK-E07** | Falhas de Disponibilidade e Perda de Backups | Ausência de redundância e negligência em testes de restore | Parada prolongada de serviços e perda irreversível de informações | Baixa | Alto | **Médio** | Estratégia de backup 3-2-1, monitoramento de saúde via Zabbix/Grafana e testes de recuperação de desastres. | Luiz Miguel (Infra) |
| **RSK-E08** | Pegada Energética e Consumo de Nuvem (Green IT) | Microsserviços ociosos e pipelines de dados ineficientes | Desperdício de recursos naturais e impacto no aquecimento global | Média | Médio | **Médio** | Arquitetura de computação sustentável (Green IT): desligamento de ambientes ociosos e cache inteligente. | Luiz Miguel (Infra) |

*Fonte: Consolidação analítica do artefato canônico [`03_etica_ia/matriz_riscos.md`](matriz_riscos.md).*

---

## 4. SÍNTESE DOS EXPERIMENTOS PRÁTICOS COM FERRAMENTAS DE IA REAL

Os quatro integrantes do grupo conduziram experimentos práticos com ferramentas de Inteligência Artificial generativa, registrando prompts, saídas geradas e a validação técnica humana dos resultados. A Tabela 2 sintetiza os experimentos documentados na pasta [`03_etica_ia/experimentos/`](experimentos/).

### Tabela 2: Síntese dos Experimentos Individuais com Ferramentas de IA

| ID | Integrante Responsável | Ferramenta Utilizada | Objetivo Prático Submetido | Alucinação / Falha Crítica Identificada | Procedimento de Verificação Humana (Fact-Checking) |
|---|---|---|---|---|---|
| **EXP-01** | **Gabriel Amancio** (Dev) | ChatGPT (GPT-4o) | Geração de endpoint de autenticação com Express, TypeScript e PostgreSQL | Omissão de proteção contra força bruta (*rate limiting*) e assunção insegura de variável de ambiente. | Compilação em ambiente de laboratório Node.js v20 e teste de estresse simulando ataques de repetição. |
| **EXP-02** | **Luiz Miguel** (Infra) | Claude 3.5 Sonnet | Automação de script Bash para configuração de firewall perimétrico com iptables | **Erro de precedência de comandos:** o script inseria `INPUT DROP` antes de liberar a porta SSH (22), o que trava o acesso remoto da máquina. | Execução em máquina virtual isolada Ubuntu Server 22.04 no VirtualBox, comprovando a queda da sessão. |
| **EXP-03** | **Paulo Germano** (Dados) | Google Gemini 1.5 Pro | Resolução de cálculos estatísticos descritivos (média, mediana e desvio padrão) sobre vetor bruto de idades | **Alucinação aritmética:** o modelo errou a soma dos dados por 56 unidades, gerando média falsa de 33,2 anos (o real é 29,47 anos). | Execução de script determinístico em Python com bibliotecas científicas `numpy` e `scipy`. |
| **EXP-04** | **Gustavo Antonio** (Segurança) | Microsoft Copilot (GPT-4) | Elaboração de cláusula de consentimento informado para coleta de dados sob a LGPD | Inclusão de cláusula abusiva de isenção unilateral de responsabilidade civil em caso de vazamento de dados. | Confronto direto com a redação dos artigos 7º, 8º, 18 e 42 da Lei nº 13.709/2018 (LGPD) `[F001]`. |

---

## 5. RECOMENDAÇÕES PARA O DESENVOLVIMENTO RESPONSÁVEL DE TECNOLOGIAS

A partir dos casos examinados e dos dados empíricos obtidos nos experimentos, a equipe definiu seis diretrizes operacionais para orientar a arquitetura e o protótipo do sistema:

```mermaid
graph TD
    subgraph PILARES["Princípios de Desenvolvimento Responsável em TI"]
        R1["1. Supervisão Humana Obrigatória (Human-in-the-Loop)"]
        R2["2. Privacidade por Padrão (Privacy by Design - LGPD F001)"]
        R3["3. Acessibilidade Universal (WCAG 2.2 Nível AA F007)"]
        R4["4. Verificação Factual e Auditoria de Código (OWASP F024)"]
        R5["5. Transparência Algorítmica e Linguagem Simples"]
        R6["6. Sustentabilidade e Eficiência de Recursos (Green IT)"]
    end

    R1 --> DECISOES["Decisões Automatizadas no Protótipo"]
    R2 --> MODELAGEM["Modelagem de Banco de Dados e APIs"]
    R3 --> INTERFACE["Telas e Componentes de Interface"]
    R4 --> SEGURANCA["Esteira de Deploy e Sustentação"]
    R5 --> COMUNICACAO["Termos de Uso e Feedback ao Usuário"]
    R6 --> INFRAESTRUTURA["Servidores e Consultas em Nuvem"]
    ```

1. **Supervisão Humana Obrigatória (*Human-in-the-Loop*):** Decisões automatizadas que afetem direitos, notas, diagnósticos ou acesso a serviços públicos devem dispor de canal acessível para revisão humana independente `[F050]`.
2. **Privacidade por Concepção (*Privacy by Design*):** A coleta de dados limita-se ao estritamente necessário para o funcionamento da plataforma (minimização), sem persistência de dados sensíveis ou identificadores desnecessários `[F001]`.
3. **Acessibilidade Digital Universal:** A interface atenderá às diretrizes WCAG 2.2 Nível AA `[F007]`, com contraste mínimo de 4.5:1, compatibilidade com leitores de tela e navegação funcional via teclado.
4. **Auditoria de Código e Validação Técnica:** Trechos de código gerados com auxílio de modelos de linguagem exigem execução em ambiente de testes e checagem de vulnerabilidades alinhada ao padrão OWASP Top 10 `[F024]`.
5. **Transparência e Linguagem Simples (*Legal Design*):** Termos de uso, orientações operacionais e mensagens do sistema serão apresentados em redação direta, sem termos ambíguos ou cláusulas de exoneração indevida de responsabilidade.
6. **Eficiência Computacional e Sustentabilidade:** Consultas de banco de dados e rotinas de nuvem serão otimizadas para diminuir tráfego de rede e tempo de processamento, reduzindo o consumo energético da infraestrutura.

---

## 6. CONSIDERAÇÕES FINAIS E DESDOBRAMENTOS

A investigação desenvolvida na Etapa 3 indicou a necessidade de incorporar critérios éticos e regulatórios ao ciclo de desenvolvimento de software. Os testes práticos confirmaram que ferramentas de IA apresentam erros factuais e exigem validação técnica contínua antes de qualquer integração em produção.

Essas conclusões orientam as etapas seguintes do projeto:
- **Etapa 4 (Problema Social ou Ambiental):** O diagnóstico foca no impacto social direto em comunidades vulneráveis e nas restrições de infraestrutura hídrica local;
- **Etapa 5 (Solução Tecnológica):** A especificação de requisitos incorpora as medidas da Matriz de Riscos (RSK-E01 a RSK-E08), assegurando conformidade com a LGPD e acessibilidade WCAG.

---

## 7. REFERÊNCIAS NORMATIVAS E BIBLIOGRÁFICAS

- **[F001]** BRASIL. **Lei nº 13.709, de 14 de agosto de 2018**. Dispõe sobre a proteção de dados pessoais e altera a Lei nº 12.965, de 23 de abril de 2014 (LGPD). Brasília, DF, 2018.
- **[F002]** BRASIL. **Lei nº 12.965, de 23 de abril de 2014**. Estabelece princípios, garantias, direitos e deveres para o uso da Internet no Brasil (Marco Civil da Internet). Brasília, DF, 2014.
- **[F003]** BRASIL. **Lei nº 9.610, de 19 de fevereiro de 1998**. Altera, atualiza e consolida a legislação sobre direitos autorais. Brasília, DF, 1998.
- **[F004]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 14724: Trabalhos acadêmicos — Apresentação**. Rio de Janeiro: ABNT, 2011.
- **[F005]** ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. **ABNT NBR 6023: Referências — Elaboração**. Rio de Janeiro: ABNT, 2018.
- **[F007]** W3C. **Web Content Accessibility Guidelines (WCAG) 2.2**. W3C Recommendation, 2023.
- **[F008]** UNIPÊ. **Manual de Normas Acadêmicas e Diretrizes do Projeto Integrador de ADS**. João Pessoa: UNIPÊ, 2026.
- **[F020]** GUPY TECNOLOGIA LTDA. **Portal de Vagas e Empregos Gupy: Mapeamento de Oportunidades em TI**. São Paulo: Gupy, 2026.
- **[F021]** BRASSCOM. **Relatório Setorial de TIC: Demanda de Talentos no Brasil (2024–2029)**. São Paulo: Brasscom, 2024.
- **[F024]** OPEN WORLDWIDE APPLICATION SECURITY PROJECT (OWASP). **OWASP João Pessoa Chapter**. 2026.
- **[F027]** ENAP. **Curso Fundamentos da Lei Geral de Proteção de Dados (LGPD)**. Brasília: Enap, 2024.
- **[F050]** CENTRO DE ESTUDOS DE SEGURANÇA E CIDADANIA (CESeC). **O Panóptico: Reconhecimento Facial e Desigualdades no Sistema de Justiça Criminal**. Rio de Janeiro: CESeC, 2023.
- **[F051]** AUTORIDADE NACIONAL DE PROTEÇÃO DE DADOS (ANPD). **Processos Administrativos Sancionadores e Medida Preventiva sobre IA**. Brasília: ANPD, 2024.
