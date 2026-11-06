---
id: diario-gustavo-antonio
integrante: Gustavo Antonio
funcao: Segurança da Informação
curso: ADS - Unipê
periodo: 2026.2
---

# Diário Individual de Aprendizagem: Gustavo Antonio

## Registro 01: Conformidade Regulatória (LGPD) e Governança de Dados
- **Data:** 2026-11-07 (Etapa 0)
- **Conhecimento desenvolvido:** Princípios fundamentais da Lei Geral de Proteção de Dados Pessoais (LGPD - Lei nº 13.709/2018), com foco em minimização de dados, consentimento e bases legais.
- **Importância:** Assegurar que desde o primeiro dia o projeto integrador adote o paradigma de *Privacy by Design* e obedeça aos requisitos do comitê de ética institucional.
- **Fontes consultadas:** Texto oficial da Lei nº 13.709/2018 e Guias Orientativos da Autoridade Nacional de Proteção de Dados (ANPD).
- **Atividade prática:** Estruturação da Matriz de Conformidade do projeto (`00_gestao/matriz_conformidade.md`) e elaboração dos modelos de TCLE e Declaração de Uso Ético de IA.
- **Dificuldades:** Adaptar o jargão jurídico da lei para requisitos práticos de desenvolvimento de software em nível de estudante.
- **Estratégias de superação:** Consulta ao curso oficial de LGPD da Enap e debate com os demais integrantes.
- **Resultados obtidos:** Sistema de governança 100% alinhado à legislação e aos critérios do DESAFIO_PRATICO.
- **Novas ferramentas aprendidas:** Framework de Privacy by Design e elaboração de Matrizes de Conformidade.

---

## Registro 02: Modelagem de Ameaças em Soluções Móveis e Portfólio de Segurança
- **Data:** 2026-11-13 (Etapa 2)
- **Conhecimento desenvolvido:** Metodologia de modelagem de ameaças STRIDE e planejamento profissional para certificação CompTIA Security+.
- **Importância:** Definir meus objetivos de capacitação em cibersegurança e planejar a arquitetura de defesa da futura aplicação do grupo.
- **Fontes consultadas:** Microsoft Threat Modeling Tool Documentation e CompTIA Security+ SY0-701 Objectives.
- **Atividade prática:** Redação da minha matriz individual de autoavaliação, PDI com 3 metas SMART e perfil técnico do GitHub com foco em cibersegurança e pentest.
- **Dificuldades:** Encontrar projetos práticos de cibersegurança em nível júnior que pudessem ser publicados publicamente sem expor infraestruturas reais.
- **Estratégias de superação:** Foco em laboratórios controlados do TryHackMe e repositórios de auditoria de código seguro.
- **Resultados obtidos:** PDI e portfólio GitHub consolidados em `02_carreira/por_integrante/gustavo_antonio/`.
- **Novas ferramentas aprendidas:** Metodologia STRIDE para análise de vulnerabilidades e laboratórios do TryHackMe.

---

## Registro 03: Auditoria de Termos de Uso e Expurgo de Cláusulas Abusivas com IA
- **Data:** 2026-11-16 (Etapa 3)
- **Conhecimento desenvolvido:** Análise de termos de privacidade e detecção de cláusulas abusivas de isenção de responsabilidade civil em plataformas digitais sob a ótica da LGPD e CDC.
- **Importância:** Como profissional de segurança, validar se ferramentas de IA conseguem apontar cláusulas ilegais e se respeitam a jurisprudência brasileira.
- **Fontes consultadas:** Código de Defesa do Consumidor (Lei nº 8.078/1990, Art. 51), LGPD e jurisprudência da ANPD.
- **Atividade prática:** Condução do Experimento EXP-04 com Microsoft Copilot, submetendo cláusula de isenção total de danos por vazamento de dados e auditando a resposta gerada.
- **Dificuldades:** Identificar quando a IA emitia interpretações baseadas no direito consuetudinário norte-americano (*common law*) em vez do direito brasileiro (*civil law*).
- **Estratégias de superação:** Formulação de prompts restritivos exigindo enquadramento estrito na legislação brasileira e súmulas do STJ.
- **Resultados obtidos:** Relatório de experimento auditado em `03_etica_ia/experimentos/experimento_04_gustavo_antonio.md`.
- **Novas ferramentas aprendidas:** Auditoria legal assistida por IA e detecção de vieses jurisdicionais em modelos proprietários.

---

## Registro 04: Liderança do Diagnóstico Socioambiental com Diagrama de Ishikawa
- **Data:** 2026-11-18 (Etapa 4)
- **Conhecimento desenvolvido:** Metodologia de análise de causa-raiz (Diagrama de Causa e Efeito / Espinha de Peixe de Ishikawa) e elaboração de Matriz de Decisão Ponderada.
- **Importância:** Liderança da Etapa 4; garantir que a escolha do problema social fosse respaldada por método científico inquestionável e dados públicos oficiais.
- **Fontes consultadas:** Metodologias de Gestão da Qualidade (Kaoru Ishikawa) e relatórios de vulnerabilidade hídrica do Trata Brasil.
- **Atividade prática:** Construção do diagrama de Ishikawa em Mermaid detalhando as causas estruturais, operacionais e governamentais do desabastecimento na Paraíba; redação da matriz de decisão com 6 critérios ponderados.
- **Dificuldades:** Atribuir pesos objetivos e justificar as notas dos 3 problemas socioambientais concorrentes.
- **Estratégias de superação:** Uso direto dos microdados censitários do IBGE e do SNIS para calcular a severidade populacional.
- **Resultados obtidos:** Dossiê da Etapa 4 e matriz de decisão concluídos com nota 9,05 para o ODS 6.
- **Novas ferramentas aprendidas:** Diagramação de Ishikawa em Mermaid e matriz de decisão multicritério (MCDA).

---

## Registro 05: Proteção Criptográfica e Segurança na Camada de Dados Offline
- **Data:** 2026-11-21 (Etapa 5)
- **Conhecimento desenvolvido:** Criptografia em repouso no navegador móvel (Web Cryptography API e AES-GCM 256-bit) e proteção contra ataques de injeção e violação de integridade.
- **Importância:** Proteger os dados das denúncias cidadãs guardadas no smartphone do usuário caso o aparelho seja perdido ou acessado por terceiros antes da sincronização.
- **Fontes consultadas:** W3C Web Cryptography API Specification e OWASP Mobile Top 10.
- **Atividade prática:** Especificação dos requisitos não funcionais de segurança (RNF-04 e RNF-05) da solução ÁguaViva PB, definindo hashing seguro de senhas com Argon2id e criptografia no IndexedDB.
- **Dificuldades:** Equilibrar a sobrecarga computacional da criptografia local em dispositivos móveis populares de baixo desempenho.
- **Estratégias de superação:** Adoção de chaves simétricas e limites de tamanho para anexos fotográficos sanitizados.
- **Resultados obtidos:** Especificação técnica de segurança consolidada no Dossiê da Etapa 5.
- **Novas ferramentas aprendidas:** Web Cryptography API nativa e sanitização de dados móveis.

---

## Registro 06: Validação de Conformidade Final e Preparação do Roteiro de Defesa
- **Data:** 2026-11-26 (Etapa 7)
- **Conhecimento desenvolvido:** Auditoria de conformidade cruzada de entregáveis acadêmicos e técnicas de resposta a questionamentos críticos de bancas examinadoras.
- **Importância:** Garantir que o grupo apresente uma monografia sem nenhuma falha de conformidade ou brecha de segurança não justificada.
- **Fontes consultadas:** Roteiros de avaliação de TCC e projetos integradores do UNIPÊ.
- **Atividade prática:** Auditoria completa de todas as 28 referências catalogadas em `00_gestao/fontes.md`, redação das perguntas de segurança no `roteiro_defesa.md` e preparação dos slides no Figma.
- **Dificuldades:** Prever perguntas capciosas da banca sobre riscos de denúncias falsas ou ataques de negação de serviço (DoS) contra a plataforma comunitária.
- **Estratégias de superação:** Formulação prévia de respostas técnicas demonstrando os mecanismos de rate limiting, validação por geolocalização e aprovação cruzada por outros cidadãos do bairro.
- **Resultados obtidos:** Roteiro de defesa estruturado com 20 perguntas gabaritadas e matriz de conformidade 100% cumprida.
- **Novas ferramentas aprendidas:** Técnicas de auditoria de conformidade de projetos acadêmicos e oratória de defesa técnica.
