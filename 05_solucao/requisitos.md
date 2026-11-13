---
id: requisitos-solucao-aguaviva-pb
etapa: 5
autor: Gabriel Amancio, Gustavo Antonio, Paulo Germano, Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F007
  - F024
  - F070
  - F071
  - F072
---

# Especificação Formal de Requisitos do Sistema: ÁguaViva PB

**Nome da Solução:** ÁguaViva PB – Plataforma Participativa de Monitoramento Hídrico e Saneamento Comunitário  
**Líder Técnico:** Gabriel Amancio (Desenvolvimento de Software)  
**Revisores:** Gustavo Antonio (Segurança/LGPD), Paulo Germano (Dados/Modelagem), Luiz Miguel (Infraestrutura)  

---

## 1. Requisitos Funcionais (Mínimo de 10 Requisitos com Classificação MoSCoW)

| ID | Nome do Requisito | Descrição Detalhada da Funcionalidade | Prioridade (MoSCoW) | Origem / Justificativa Socioambiental |
|---|---|---|---|---|
| **RF-01** | **Registro Simplificado de Ocorrência Hídrica** | Permitir que o cidadão reporte falta de água, turbidez (água barrenta/amarelada), odor fétido ou sabor alterado em até 3 passos intuitivos. | **Must Have** | Atende à necessidade de notificação imediata de anomalias hídricas identificadas na Etapa 4 `[F070]`. |
| **RF-02** | **Reporte de Vazamento de Esgoto e Rompimento de Adutora** | Possibilitar a denúncia de esgoto a céu aberto, fossas transbordando ou vazamentos de tubulação limpa (perdas físicas). | **Must Have** | 50,9% dos lares da PB não possuem rede de esgoto e as perdas na rede alcançam 47% `[F070]`, `[F071]`. |
| **RF-03** | **Georreferenciamento Automático e Seleção Manual de Bairro** | Capturar as coordenadas de latitude/longitude via GPS do dispositivo ou permitir seleção de bairro/comunidade em lista suspensa. | **Must Have** | Essencial para gerar a localização precisa das áreas desabastecidas sem exigir digitação complexa. |
| **RF-04** | **Opção de Reporte Anônimo sob Diretrizes da LGPD** | Garantir que o munícipe possa submeter denúncias sem informar nome ou CPF, gerando identificador pseudonimizado (protocolo hash). | **Must Have** | Princípio da minimização de dados e segurança pessoal do denunciante sob a LGPD `[F001]`. |
| **RF-05** | **Mapa Comunitário Interativo de Calor (Heatmap)** | Exibir mapa público da cidade com manchas de calor indicando a concentração de relatos de falta de água e esgoto por bairro. | **Must Have** | Transparência ativa para a população e visibilidade coletiva das falhas das concessionárias. |
| **RF-06** | **Emissão e Consulta de Alertas Preventivos Locais** | Notificar moradores cadastrados sobre manutenções programadas, cortes na rede ou alertas sanitários de água imprópria emitidos por órgãos de saúde. | **Should Have** | Redução do impacto do desabastecimento surpresa e prevenção de doenças de veiculação hídrica `[F072]`. |
| **RF-07** | **Módulo Especializado para Agentes Comunitários de Saúde (ACS)** | Interface diferenciada para agentes de saúde cadastrarem relatos múltiplos em visitas domiciliares e apontarem sintomas de diarreia/vômito. | **Should Have** | Apoio à vigilância epidemiológica territorial e integração com agentes que atuam na ponta do SUS. |
| **RF-08** | **Painel Analítico de Cruzamento de Dados (Dashboard DATASUS)** | Gráficos e indicadores correlacionando bairros com mais queixas de saneamento e histórico de internações por DDA no DATASUS `[F072]`. | **Should Have** | Subsidia cobranças fundamentadas pelo Ministério Público, Defensoria Pública e lideranças locais. |
| **RF-09** | **Guia Educativo de Higienização e Tratamento Caseiro da Água** | Seção acessível com instruções em linguagem simples sobre uso de hipoclorito de sódio, filtragem e fervura para emergências. | **Should Have** | Mitigação preventiva imediata de contaminações biológicas em áreas desprovidas de água tratada. |
| **RF-10** | **Operação em Modo Offline com Sincronização Automática (PWA)** | Armazenar o reporte no cache local do navegador quando o usuário estiver sem sinal de internet móvel e enviar assim que reconectar. | **Must Have** | Contorna a instabilidade crônica de sinal de telefonia móvel em comunidades periféricas e rurais. |
| **RF-11** | **Upload Opcional de Foto Comprobatória com Metadados Ocultos** | Permitir envio de 1 fotografia do problema (água turva ou esgoto), expurgando metadados EXIF da imagem antes do armazenamento. | **Could Have** | Aumenta a credibilidade do relato resguardando a privacidade do denunciante sob a LGPD `[F001]`. |
| **RF-12** | **Exportação de Relatórios Técnicos Consolidados em PDF/CSV** | Permitir que lideranças comunitárias e conselhos municipais exportem dossiês de ocorrências mensais por bairro. | **Could Have** | Instrumentaliza o controle social perante a CAGEPA e órgãos reguladores de saneamento. |

---

## 2. Requisitos Não Funcionais (Mínimo de 6 Requisitos com Métricas Verificáveis)

| ID | Categoria | Descrição do Requisito Não Funcional | Métrica Verificável / Critério de Aceite |
|---|---|---|---|
| **RNF-01** | **Acessibilidade Digital** | A interface da plataforma deve cumprir integralmente o nível AA das diretrizes internacionais **WCAG 2.2** `[F007]`. | Contraste mínimo de texto de 4.5:1, navegação completa sem mouse (via teclado), botões com alvos táteis ≥ 44x44px e compatibilidade com leitores de tela (TalkBack/NVDA). |
| **RNF-02** | **Desempenho e Leveza** | A aplicação web deve carregar com rapidez mesmo em conexões móveis com restrição de banda (3G/4G). | Tempo de carregamento do conteúdo inicial (Largest Contentful Paint - LCP) **≤ 2,0 segundos** em conexão 3G simulada; peso total da página inicial **≤ 1,5 MB**. |
| **RNF-03** | **Privacidade e Proteção de Dados (LGPD)** | Adoção dos princípios de minimização e privacidade desde a concepção previstos na Lei nº 13.709/2018 `[F001]`. | Zero armazenamento de CPF, RG ou telefone; remoção de metadados de fotos e tráfego protegido por HTTPS. |
| **RNF-04** | **Segurança da Aplicação** | O backend deve aplicar boas práticas básicas contra falhas comuns da web (**OWASP Top 10** `[F024]`). | Consultas SQL parametrizadas (anti SQL Injection), validação de campos no servidor e proteção básica contra XSS. |
| **RNF-05** | **Disponibilidade** | A aplicação web deve permanecer acessível para receber denúncias comunitárias de forma estável. | Hospedagem simples com monitoramento básico de disponibilidade e cópias de segurança periódicas do banco de dados. |
| **RNF-06** | **Usabilidade e Clareza Textual** | O fluxo de envio de ocorrência deve ser autoexplicativo, adotando linguagem simples e ícones visuais descritivos. | Taxa de conclusão de reporte por cidadãos leigos de **≥ 80% sem auxílio externo**, com tempo médio de preenchimento **≤ 120 segundos**. |
| **RNF-07** | **Compatibilidade e Responsividade** | A aplicação deve se adaptar a telas pequenas de celulares básicos (a partir de 320px) e computadores. | Layout mobile-first compatível com Chrome Mobile, Firefox e Safari, sem exigir instalação pesada de loja de apps. |
| **RNF-08** | **Sustentabilidade e Baixo Consumo** | Aplicação leve para não gastar a franquia de dados do morador nem exigir servidores caros. | Compressão de imagens enviadas, páginas leves e reuso de dados em cache local no navegador. |
