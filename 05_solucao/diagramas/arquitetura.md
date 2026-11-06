---
id: diagrama-arquitetura-aguaviva-pb
etapa: 5
autor: Gabriel Amancio, Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F007
  - F024
---

# Diagrama de Arquitetura de Software e Infraestrutura – ÁguaViva PB

Este documento modela a arquitetura técnica da solução **ÁguaViva PB**, demonstrando a separação em camadas, a integração entre frontend e backend, a persistência geoespacial e os controles de segurança e privacidade.

---

## 1. Diagrama de Contexto e Containers (Arquitetura Geral)

```mermaid
graph TD
    subgraph CLIENTE["Camada de Apresentação (Frontend PWA)"]
        USR["Cidadão / Morador (Dispositivo Móvel 3G/4G)"]
        ACS["Agente Comunitário de Saúde (Tablet/Smartphone)"]
        PWA["ÁguaViva PWA (React + Vite + TailwindCSS)<br>WCAG 2.2 AA / Service Worker Offline"]
    end

    subgraph BORDA["Camada de Borda e Segurança"]
        NGX["Reverse Proxy & Cache (Nginx)<br>Terminação TLS 1.3 / Rate Limiting (OWASP)"]
    end

    subgraph BACKEND["Camada de Aplicação (Backend REST API)"]
        API["API Gateway & Controllers (Node.js + Express + TypeScript)"]
        AUTH["Módulo de Autenticação & Anonimização (JWT / Hash SHA-256)"]
        GEO["Serviço Geoespacial de Ocorrências (PostGIS Spatial Queries)"]
        ALERT["Serviço de Alertas & Notificações Sanitárias"]
    end

    subgraph DADOS["Camada de Persistência & Analytics"]
        DB[(Banco de Dados PostgreSQL 16 + PostGIS)]
        CACHE[(Cache em Memória Redis - Sessões e Mapas de Calor)]
        DATA_OPEN["Repositório Aberto de Indicadores de Saúde (DATASUS / SNIS)"]
    end

    USR -->|Acessa via Navegador| PWA
    ACS -->|Acessa via Navegador| PWA
    PWA -->|Requisições HTTPS / JSON| NGX
    NGX -->|Proxy Seguro| API
    API --> AUTH
    API --> GEO
    API --> ALERT
    GEO -->|Consultas Espaciais| DB
    GEO -->|Cache de Heatmap| CACHE
    ALERT --> DB
    DATA_OPEN -.->|Ingestão de Séries Históricas| DB
```

---

## 2. Descrição dos Componentes da Arquitetura
1. **Frontend PWA (React + Vite):** Interface responsiva, leve e acessível segundo a WCAG 2.2 `[F007]`. Utiliza *Service Workers* para permitir que moradores registrem denúncias mesmo quando a conexão móvel estiver instável.
2. **Reverse Proxy Nginx:** Ponto único de entrada na infraestrutura. Aplica cabeçalhos de segurança (CSP, HSTS), limite de taxa contra ataques de negação de serviço (*rate limiting*) e terminação SSL/TLS 1.3 `[F024]`.
3. **Backend Node.js & TypeScript:** Implementado em arquitetura modular limpa (Clean Architecture), provendo rotas RESTful documentadas e tipagem estrita contra erros em tempo de execução.
4. **PostgreSQL com PostGIS:** Banco de dados relacional com suporte nativo a dados georreferenciados (pontos de ocorrência, polígonos de bairros e buffers de proximidade a focos de contaminação).
5. **Módulo de Anonimização (LGPD `[F001]`):** Assegura que o identificador do cidadão seja substituído por um código hash irreversível antes de ser gravado na tabela pública de ocorrências.
