---
id: diagrama-fluxo-usuario-aguaviva-pb
etapa: 5
autor: Gabriel Amancio, Gustavo Antonio
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F007
---

# Fluxo de Interação do Usuário (User Journey) – ÁguaViva PB

Este documento mapeia o fluxo navegacional completo vivenciado pelo cidadão desde o acesso inicial à plataforma até o recebimento de alertas e confirmação anônima de reporte de saneamento.

---

## 1. Diagrama de Fluxo de Navegação (Jornada do Cidadão)

```mermaid
flowchart TD
    INICIO(["Início: Cidadão acessa ÁguaViva PB via smartphone"]) --> HOME["Tela 01: Página Inicial / Dashboard Comunitário"]
    
    HOME --> DECISAO{"Qual a ação desejada?"}
    
    DECISAO -->|Ver Alertas ou Mapa| MAPA["Tela 04: Mapa de Calor e Indicadores por Bairro"]
    DECISAO -->|Aprender Tratamento de Água| GUIA["Tela 05: Guia de Cuidados e Higienização Caseira"]
    DECISAO -->|Reportar Problema de Água/Esgoto| FORM["Tela 02: Formulário Acessível de Registro"]
    
    FORM --> TIPO_PROBLEMA["Selecionar tipo de anomalia:<br>• Falta de Água<br>• Água Barrenta/Turva<br>• Mau Cheiro / Esgoto"]
    TIPO_PROBLEMA --> LOCALIZACAO["Capturar localização GPS ou escolher bairro"]
    LOCALIZACAO --> OPCAO_FOTO{"Deseja anexar foto opcional?"}
    
    OPCAO_FOTO -->|Sim| UPLOAD["Anexar foto (Remoção automática de metadados EXIF)"]
    OPCAO_FOTO -->|Não| TERMO_LGPD["Tela de Confirmação e Consentimento LGPD (F001)"]
    UPLOAD --> TERMO_LGPD
    
    TERMO_LGPD --> CONEXAO{"Dispositivo está online?"}
    
    CONEXAO -->|Sim| ENVIO_SUCESSO["Tela 03: Protocolo Gerado e Sucesso no Envio"]
    CONEXAO -->|Não| CACHE_OFFLINE["Tela 07: Salvo no Dispositivo (Modo Offline PWA)"]
    
    CACHE_OFFLINE -.->|Reconectar à internet| ENVIO_SUCESSO
    ENVIO_SUCESSO --> FIM(["Fim: Ocorrência computada no Mapa Comunitário"])
```

---

## 2. Princípios de Acessibilidade no Fluxo (WCAG 2.2 `[F007]`)
- O fluxo de envio principal pode ser concluído em **no máximo 3 toques/cliques** a partir da tela inicial.
- Toda transição de tela possui foco gerenciado para tecnologias assistivas (leitores de tela anunciam o carregamento e o resultado do envio).
- As mensagens de validação de formulário são apresentadas inline com texto explícito e contraste alto, sem depender unicamente de diferenciação de cores.
