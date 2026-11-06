---
id: relatorio-vagas-etapa-1
etapa: 1
autor: opencode / Main Agent
data: 2026-11-06
status: ativo
fontes:
  - F020
  - F021
  - F022
---

# Relatório Técnico de Coleta e Mapeamento de Vagas de TI (Etapa 1A)

Este relatório detalha a metodologia de pesquisa empírica, os critérios de inclusão/exclusão, os dados brutos obtidos e a síntese analítica dos 24 anúncios reais de vagas coletados no ecossistema de TI no Brasil, com foco em oportunidades remotas e no Nordeste (Paraíba) `[F020]`.

---

## 1. Metodologia de Pesquisa e Coleta de Dados

### 1.1 Objetivos e Escopo Amostral
A investigação teve como finalidade levantar as exigências reais contemporâneas do mercado de trabalho para subsidiar o planejamento de carreira dos quatro estudantes de ADS do UNIPÊ e orientar o desenvolvimento responsável da solução tecnológica do grupo.
- **Amostra Total:** 24 anúncios reais (superando a meta mínima de 20 vagas exigida pelo DESAFIO_PRATICO, com 6 vagas por função para formação de margem de reserva).
- **Recorte Temporal:** Coleta realizada em 06 de novembro de 2026.
- **Recorte Geográfico:** Vagas no Brasil com modelo prioritariamente Remoto (Home Office) ou localizadas/com polos no Nordeste (especialmente João Pessoa - PB e Recife - PE) `[F022]`.
- **Nível Profissional:** Estágio e Júnior.

### 1.2 Palavras-Chave e Filtros Utilizados
A busca foi executada sobre portais públicos de recrutamento em conformidade estrita com termos de uso (Portal Gupy `[F020]`, páginas públicas de carreiras de empresas de tecnologia), com as seguintes combinações booleanas:
- **Função 1 (Desenvolvimento de Software):** `"desenvolvedor junior"`, `"estágio desenvolvimento"`, `"software developer jr"`, `"full stack junior"`.
- **Função 2 (Infraestrutura e Redes):** `"analista de infraestrutura jr"`, `"analista de redes junior"`, `"estágio infraestrutura"`, `"cloud junior"`.
- **Função 3 (Dados e IA):** `"analista de dados junior"`, `"inteligência de dados jr"`, `"estágio dados"`, `"desenvolvedor de IA junior"`.
- **Função 4 (Segurança da Informação):** `"analista de segurança da informação jr"`, `"cibersegurança jr"`, `"estágio segurança da informação"`, `"soc junior"`.

### 1.3 Critérios de Inclusão e Exclusão
- **Critérios de Inclusão:** Anúncios com descrição explícita de requisitos técnicos (hard skills), competências comportamentais (soft skills), nível de escolaridade/formação exigido, empresa contratante identificada e URL de acesso público verificável.
- **Critérios de Exclusão:** Vagas sem identificação da empresa contratante (anônimas), anúncios duplicados, vagas com requisitos genéricos ou sem menção a tecnologias específicas, e posições de nível Pleno/Sênior rotuladas inadequadamente como entrada.

---

## 2. Resumo Qualitativo por Função Profissional

### 2.1 Desenvolvimento de Software (Gabriel Amancio - VAG-001 a VAG-006)
- **Perfil Geral:** Ampla exigência de arquitetura web moderna (Full Stack), com forte prevalência de ecossistemas JavaScript/TypeScript (React, Node.js), além de C# (.NET) e Java (Spring Boot) no segmento corporativo.
- **Destaques:** O domínio de versionamento colaborativo com Git/GitHub e a capacidade de consumir/desenvolver APIs RESTful figuram em 100% dos anúncios. Há menção crescente ao uso produtivo de ferramentas de IA (ex: Copilot) como diferencial de agilidade (VAG-006).

### 2.2 Infraestrutura e Redes (Luiz Miguel - VAG-007 a VAG-012)
- **Perfil Geral:** Transição expressiva do suporte tradicional para a administração híbrida de ambientes: coexistência de servidores locais (Windows Server, Active Directory, Linux) com nuvens públicas (AWS, Azure) e serviços de colaboração (Microsoft Entra ID / M365).
- **Destaques:** Protocolos de rede TCP/IP, roteamento/switching e ferramentas de monitoramento contínuo (Zabbix, Grafana, CloudWatch) são obrigatórios para sustentar alta disponibilidade (uptime) em operações distribuídas.

### 2.3 Dados e Inteligência Artificial (Paulo Germano - VAG-013 a VAG-018)
- **Perfil Geral:** Centralidade absoluta de SQL para extração e modelagem de dados relacionais e dimensionais, associado à construção de dashboards interativos em ferramentas de Business Intelligence (Power BI, Tableau).
- **Destaques:** A linguagem Python (Pandas/NumPy) consolida-se como requisito-chave para automação e análise exploratória. Surge com destaque a demanda por integração prática com APIs de Modelos de Linguagem (LLMs) e automação inteligente (VAG-016).

### 2.4 Segurança da Informação (Gustavo Antonio - VAG-019 a VAG-024)
- **Perfil Geral:** Foco na segurança defensiva: monitoramento contínuo em SOC (SIEM, triagem de logs de eventos anômalos), controle rigoroso de identidades e acessos (IAM) e configuração de firewalls de borda (Fortinet, pfSense).
- **Destaques:** Princípios de conformidade com a LGPD (Lei nº 13.709/2018 `[F001]`) e aplicação de segurança por padrão (Privacy by Design / OWASP Top 10) são cobrados mesmo em posições iniciais e de estágio (VAG-024).

---

## 3. Síntese dos Desafios e Dores dos Contratantes

A análise semântica dos 24 anúncios revelou dores críticas enfrentadas pelas organizações no preenchimento de posições de tecnologia:

| ID | Tema do Desafio | Descrição da Dor Identificada | Evidência Direta (IDs das Vagas) | Frequência |
|---|---|---|---|---|
| **DES-01** | Exigência Desproporcional de Experiência Prévia | Anúncios classificados como Júnior solicitando experiência prática com múltiplos frameworks e arquiteturas de microsserviços | VAG-001, VAG-002, VAG-004, VAG-010, VAG-019 | 5 vagas (20,8%) |
| **DES-02** | Demanda por Comunicação Assíncrona e Autonomia Remota | Dificuldade das empresas em encontrar iniciantes com disciplina, clareza textual e maturidade para trabalho à distância | VAG-001, VAG-004, VAG-009, VAG-010, VAG-014, VAG-020 | 6 vagas (25,0%) |
| **DES-03** | Pressão Regulatória e Vulnerabilidade de Dados | Necessidade imperativa de evitar incidentes de vazamento e sanções da ANPD, exigindo postura preventiva desde a base | VAG-019, VAG-021, VAG-023, VAG-024 | 4 vagas (16,7%) |
| **DES-04** | Adoção Emergente de IA Generativa nos Processos | Escassez de talentos que saibam orquestrar modelos de linguagem sem incorrer em alucinações ou infrações éticas | VAG-006, VAG-016 | 2 vagas (8,3%) |
| **DES-05** | Perfil Multidisciplinar em "T" | Empresas buscando desenvolvedores que compreendam nuvem, analistas de dados que codifiquem e analistas de segurança com automação | VAG-001, VAG-010, VAG-013, VAG-015, VAG-023 | 5 vagas (20,8%) |

---

## 4. Limitações Metodológicas e Vieses da Amostra

1. **Concentração de Plataforma:** A amostragem concentrou-se majoritariamente no ecossistema Gupy `[F020]`, refletindo o padrão de contratação de médias e grandes corporações, podendo sub-representar dinâmicas de microempresas locais.
2. **Janela Temporal:** Coleta pontual de 06/11/2026, sujeita a sazonalidades contratuais de final de ano (fechamento de orçamentos e abertura de programas de estágio para o ano seguinte).
3. **Viés da Modalidade Remota:** A predominância de vagas remotas eleva o nível de exigência por soft skills e autonomia investigativa em comparação com posições exclusivamente presenciais locais.
