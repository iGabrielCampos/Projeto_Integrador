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

# Diagrama de Funcionamento e Arquitetura – ÁguaViva PB

Este documento descreve como o **ÁguaViva PB** funciona do ponto de vista do protótipo entregue (navegador mobile) e como seria organizado em uma versão completa para produção, mantendo infraestrutura simples e de baixo custo.

## 1. Diagrama de Funcionamento da Aplicação

```mermaid
graph TD
    subgraph CLIENTE["No Celular do Cidadão ou ACS (Navegador Web)"]
        USR["Morador (Celular simples 3G/4G)"]
        ACS["Agente Comunitário de Saúde"]
        PWA["ÁguaViva PB (Protótipo: HTML/CSS/JS; Versão completa: PWA)<br>Acessível (WCAG 2.2 AA) e fila local sem internet"]
    end

    subgraph SERVIDOR["Servidor Web e API (Backend Simples)"]
        API["API REST (Node.js + Express)<br>Validação de dados e proteção básica (OWASP)"]
        ANON["Anonimização de Relatos (LGPD)<br>Remove dados pessoais e metadados de foto"]
    end

    subgraph DADOS["Banco de Dados e Fontes Públicas"]
        DB[(Banco Relacional PostgreSQL<br>Registros por bairro e protocolo)]
        DATA_OPEN["Dados Públicos (IBGE, SNIS e DATASUS)"]
    end

    USR --> PWA
    ACS --> PWA
    PWA -->|Envio por HTTPS quando há sinal| API
    API --> ANON
    ANON --> DB
    DATA_OPEN -.->|Cruzamento de indicadores| DB
```

## 2. Descrição dos Componentes

1. **Interface Web no Navegador (Protótipo entregue e versão PWA):** Páginas leves em HTML/CSS/JS (com evolução prevista para PWA com *Service Worker*) para que moradores consigam registrar faltas d'água mesmo com conexão fraca ou sem internet no momento.
2. **Backend REST (Node.js + Express):** Recebe os relatos do formulário, valida os campos obrigatórios e aplica proteções básicas contra entradas inválidas `[F024]`.
3. **Camada de Privacidade (LGPD `[F001]`):** Não exige CPF, RG ou telefone, remove metadados de fotos e agrupa a localização por bairro/região para evitar exposição individual de quem denuncia.
4. **Banco de Dados (PostgreSQL):** Armazena as ocorrências com data, tipo de problema, bairro e número de protocolo, permitindo gerar relatórios e cruzar informações com dados abertos de saúde e saneamento.
