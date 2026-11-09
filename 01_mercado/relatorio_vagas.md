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

# Relatório de Coleta e Mapeamento de Vagas em TI

Este relatório apresenta a metodologia de coleta, os critérios de seleção e a síntese dos 24 anúncios de vagas em Tecnologia da Informação obtidos para o estudo, com ênfase em oportunidades remotas e no Nordeste `[F020]`.

---

## 1. Metodologia de Pesquisa e Coleta de Dados

### 1.1 Objetivos e Escopo Amostral
O objetivo da coleta foi mapear requisitos técnicos e comportamentais atuais do mercado para orientar os planos individuais de carreira dos estudantes e embasar a concepção da solução tecnológica.
- **Amostra total:** 24 anúncios (6 por função, atendendo ao piso de 20 vagas com margem de segurança).
- **Período de coleta:** 06 de novembro de 2026.
- **Recorte geográfico:** vagas no Brasil com formato remoto preponderante ou sediadas no Nordeste (principalmente João Pessoa e Recife) `[F022]`.
- **Nível profissional:** posições de estágio e júnior.

### 1.2 Palavras-Chave e Filtros Utilizados
A busca foi feita em páginas públicas de recrutamento e portais de empresas (como o Portal Gupy `[F020]`), utilizando os seguintes termos de pesquisa:
- **Função 1 (Desenvolvimento de Software):** `"desenvolvedor junior"`, `"estágio desenvolvimento"`, `"software developer jr"`, `"full stack junior"`.
- **Função 2 (Infraestrutura e Redes):** `"analista de infraestrutura jr"`, `"analista de redes junior"`, `"estágio infraestrutura"`, `"cloud junior"`.
- **Função 3 (Dados e IA):** `"analista de dados junior"`, `"inteligência de dados jr"`, `"estágio dados"`, `"desenvolvedor de IA junior"`.
- **Função 4 (Segurança da Informação):** `"analista de segurança da informação jr"`, `"cibersegurança jr"`, `"estágio segurança da informação"`, `"soc junior"`.

### 1.3 Critérios de Inclusão e Exclusão
- **Critérios de inclusão:** anúncios com descrição clara de requisitos técnicos e comportamentais, escolaridade exigida, identificação da empresa contratante e link público ativo.
- **Critérios de exclusão:** anúncios anônimos, vagas duplicadas, descrições genéricas sem tecnologias especificadas e vagas com exigências de nível pleno ou sênior rotuladas como iniciais.

---

## 2. Resumo Qualitativo por Função Profissional

### 2.1 Desenvolvimento de Software (Gabriel Amancio - VAG-001 a VAG-006)
- **Perfil geral:** predomínio do desenvolvimento web (Full Stack), com presença frequente de JavaScript e TypeScript (React, Node.js), além de C# (.NET) e Java (Spring Boot) no meio corporativo.
- **Observações:** controle de versão com Git/GitHub e consumo de APIs RESTful aparecem em 100% dos anúncios da área. Nota-se também menção ao uso de assistentes de código como diferencial de produtividade (VAG-006).

### 2.2 Infraestrutura e Redes (Luiz Miguel - VAG-007 a VAG-012)
- **Perfil geral:** transição do suporte tradicional para a administração híbrida de sistemas, com servidores locais (Windows Server, Active Directory, Linux) associados a serviços em nuvem (AWS, Azure) e plataformas de identidade (Microsoft Entra ID).
- **Observações:** protocolos de rede (TCP/IP), conceitos de roteamento e ferramentas de monitoramento (Zabbix, Grafana, CloudWatch) aparecem com regularidade para suporte à operação contínua.

### 2.3 Dados e Inteligência Artificial (Paulo Germano - VAG-013 a VAG-018)
- **Perfil geral:** uso frequente de SQL para extração e manipulação de dados relacionais, além da elaboração de painéis visuais em ferramentas de BI (Power BI, Tableau).
- **Observações:** a linguagem Python (Pandas, NumPy) é comum em análises exploratórias e rotinas de automação. Identificou-se também menção ao consumo de APIs de modelos de linguagem (VAG-016).

### 2.4 Segurança da Informação (Gustavo Antonio - VAG-019 a VAG-024)
- **Perfil geral:** ênfase em segurança defensiva, com monitoramento de logs em SOC (SIEM), gestão de identidades e acessos (IAM) e operação de firewalls (Fortinet, pfSense).
- **Observações:** noções de conformidade com a LGPD (Lei nº 13.709/2018 `[F001]`) e práticas do OWASP Top 10 surgem como requisitos mesmo em vagas de estágio e nível júnior (VAG-024).

---

## 3. Síntese dos Desafios e Demandas dos Contratantes

A análise dos 24 anúncios evidenciou demandas e desafios frequentes enfrentados pelas organizações no recrutamento em tecnologia:

| ID | Tema do Desafio | Descrição da Dor Identificada | Evidência Direta (IDs das Vagas) | Frequência |
|---|---|---|---|---|
| **DES-01** | Exigência Elevada de Experiência Prévia | Anúncios de nível júnior solicitando experiência prática com múltiplos frameworks e arquitetura de microsserviços | VAG-001, VAG-002, VAG-004, VAG-010, VAG-019 | 5 vagas (20,8%) |
| **DES-02** | Demanda por Comunicação Assíncrona e Autonomia | Necessidade de profissionais com clareza textual e autonomia para o modelo de trabalho à distância | VAG-001, VAG-004, VAG-009, VAG-010, VAG-014, VAG-020 | 6 vagas (25,0%) |
| **DES-03** | Pressão Regulatória e Proteção de Dados | Preocupação com incidentes de segurança e adequação às diretrizes da ANPD, demandando postura preventiva nas equipes | VAG-019, VAG-021, VAG-023, VAG-024 | 4 vagas (16,7%) |
| **DES-04** | Uso de Ferramentas de IA Generativa | Procura por profissionais capazes de integrar ferramentas de IA ao fluxo de trabalho com controle de respostas | VAG-006, VAG-016 | 2 vagas (8,3%) |
| **DES-05** | Perfil Multidisciplinar (Profissional em "T") | Empresas buscando desenvolvedores com noções de nuvem, analistas de dados que programem e profissionais de segurança com foco em automação | VAG-001, VAG-010, VAG-013, VAG-015, VAG-023 | 5 vagas (20,8%) |

---

## 4. Limitações Metodológicas e Vieses da Amostra

1. **Concentração de plataforma:** a coleta concentrou-se principalmente na plataforma Gupy `[F020]`, refletindo perfis de médias e grandes empresas e podendo sub-representar dinâmicas de pequenos negócios locais.
2. **Recorte temporal:** coleta realizada em novembro de 2026, sujeita a sazonalidades de final de ano nas contratações.
3. **Proporção do modelo remoto:** a presença significativa de vagas remotas amplia a cobrança por autonomia e comunicação escrita quando comparada a posições presenciais.
