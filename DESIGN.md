---
name: ÁguaViva PB
description: Sistema de design cívico, resiliente e offline-first para monitoramento comunitário e cidadania hídrica (ODS 6)
colors:
  primary: "#0d9488"
  primary-hover: "#0f766e"
  primary-dark: "#134e4a"
  primary-deep: "#042f2e"
  primary-subtle: "#ccfbf1"
  accent-alert: "#f59e0b"
  accent-alert-hover: "#facc15"
  accent-critical: "#e11d48"
  accent-critical-light: "#fca5a5"
  accent-critical-border: "#f87171"
  accent-success: "#10b981"
  accent-success-light: "#86efac"
  accent-success-border: "#4ade80"
  neutral-bg: "#f8fafc"
  neutral-track: "#f1f5f9"
  neutral-thumb: "#cbd5e1"
  neutral-placeholder: "#a1a1aa"
  neutral-dark-border: "#3f3f46"
  surface-card: "#ffffff"
  surface-dark: "#09090b"
  surface-dark-elevated: "#18181b"
  pitch-black: "#000000"
  text-main: "#0f172a"
  text-muted: "#64748b"
  text-on-dark: "#ffffff"
  text-on-dark-secondary: "#e4e4e7"
  text-on-dark-soft: "#fef08a"
  border-subtle: "#e2e8f0"
  border-dark: "#27272a"
  high-contrast-yellow: "#ffe500"
typography:
  display:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1.625rem"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  display-large-mode:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1.55rem"
    fontWeight: 800
  headline:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  headline-large-mode:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1.35rem"
    fontWeight: 700
  title:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1rem"
    fontWeight: 600
    lineHeight: 1.3
  body:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.5
  body-large-mode:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 400
  label:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    letterSpacing: "0.05em"
  caption:
    fontFamily: "Sora, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 500
  micro:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "10px"
    fontWeight: 700
  data-mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "0.875rem"
    fontWeight: 700
rounded:
  sm: "8px"
  md: "12px"
  lg: "16px"
  pill: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "#ffffff"
    rounded: "{rounded.md}"
    padding: "14px 20px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "14px 20px"
    height: "48px"
  button-high-contrast:
    backgroundColor: "{colors.high-contrast-yellow}"
    textColor: "#000000"
    rounded: "{rounded.md}"
    padding: "14px 20px"
    height: "48px"
---

# Design System: ÁguaViva PB

## Overview

**Creative North Star: "A Nascente Resiliente"**

O ÁguaViva PB foi construído sob a premissa de que o acesso à água potável e ao saneamento é um direito humano fundamental inegociável. A linguagem visual expressa a pureza, transparência e resiliência da água, contrapondo superfícies limpas e confiáveis com indicadores de alerta imediatamente decodificáveis sob qualquer circunstância ambiental.

O sistema rejeita excessos decorativos, gradientes em textos, sombras pesadas e modais bloqueantes. Cada pixel serve para diminuir a incerteza do cidadão, comunicar com transparência o status do saneamento comunitário e garantir que solicitações emergenciais sejam transmitidas com zero fricção.

**Key Characteristics:**
- **Clareza Hiperlocal:** Informação geográfica precisa sem exposição da identidade do cidadão.
- **Resiliência Offline:** Estados de interface que dignificam o usuário desconectado, informando que seus dados estão protegidos na memória local.
- **Contraste de Campo:** Projetado para telas baratas sob sol tropical brilhante ou ambientes escuros sem energia elétrica.

## Colors

A paleta equilibra tons de água tratada (Teal profundo e esmeralda) com amarelo solar de vigilância cívica e vermelho de interrupção crítica, fundamentada em superfícies limpas no modo claro e preto OLED puro no modo escuro/foco.

### Primary
- **Água Profunda (Teal 700/800)** (`#0f766e` / `#115e59`): Representa autoridade institucional e pureza hídrica. Utilizada na barra superior, botões primários e cabeçalhos.
- **Nascente Cristalina (Teal 500/600)** (`#14b8a6` / `#0d9488`): Foco interativo, estados de hover e links ativos.

### Secondary
- **Alerta Solar (Amber 500/600)** (`#f59e0b` / `#d97706`): Usado no botão central de ação comunitária de denúncia, alertas de turbidez e status em fila.
- **Risco Crítico (Rose 600/700)** (`#e11d48` / `#be123c`): Exclusivo para desabastecimento agudo, interrupções prolongadas e efluentes a céu aberto.
- **Potabilidade Segura (Emerald 600)** (`#10b981`): Laudos conformes e sincronização bem-sucedida.

### Neutral
- **Tela Base Claro** (`#f8fafc`): Fundo suave que previne fadiga ocular em uso contínuo.
- **Superfície Card** (`#ffffff`): Painéis e cartões de conteúdo com bordas estruturais finas.
- **Texto Principal** (`#0f172a`): Contraste 15.8:1 contra o fundo branco.
- **Texto Secundário** (`#64748b`): Contraste 4.6:1 em corpo pequeno, garantindo cumprimento da norma WCAG 2.2 AA.
- **Preto OLED (Black Theme)** (`#000000`): Fundo absoluto do modo foco para economia de bateria e contraste extremo.
- **Amarelo Elétrico (High Contrast)** (`#ffe500`): Contraste 19.5:1 contra o fundo preto puro.

### Named Rules
**A Regra da Sobriedade do Vermelho.** O tom vermelho (`#e11d48`) é estritamente restrito a situações onde a potabilidade ou a interrupção coloca a saúde pública em risco iminente. Nunca deve ser usado para avisos operacionais triviais.

## Typography

**Display & Body Font:** `Sora` (Google Fonts, com fallback em `system-ui, -apple-system, sans-serif`)  
**Data/Mono Font:** `JetBrains Mono` (Google Fonts, para protocolos, coordenadas e percentuais)

**Character:** Tipografia moderna, geométrica e acolhedora, com alturas-x generosas e terminações abertas que preservam excelente legibilidade mesmo em renderizações de baixa resolução em smartphones modestos.

### Hierarchy
- **Display (h1)** (800 Extrabold, 26px / 1.625rem, line-height 1.2): Identificação de telas e títulos de impacto comunitário.
- **Headline (h2)** (700 Bold, 20px / 1.25rem, line-height 1.25): Títulos de seções principais e nomes de bairros/comunidades.
- **Title (h3)** (600 Semibold, 16px / 1rem, line-height 1.3): Títulos de cards, denúncias e categorias de serviço.
- **Body** (400 Regular / 500 Medium, 14px / 0.875rem, line-height 1.5): Textos explicativos, parágrafos e formulários. Comprimento ideal entre 55 e 75 caracteres por linha.
- **Label / Overline** (700 Bold, 12px / 0.75rem, tracking 0.05em, caixa alta): Identificadores de categoria e metadados.
- **Data Mono** (700 Bold, 14px–28px, `font-mono tabular-nums`): Percentuais oficiais de perdas, tempos de espera e protocolos.

### Named Rules
**A Regra dos Números Tabulares.** Todos os dados numéricos de telemetria (percentual do SNIS, contadores de horas sem água, quantitativo de apoios) utilizam `font-variant-numeric: tabular-nums` e fonte monoespacada para alinhamento estável.

## Layout

- **Abordagem Mobile-First:** Concebida primordialmente para visualização vertical em smartphones (largura máxima de 440px centralizada no desktop).
- **Áreas de Toque:** Nenhuma área interativa possui menos de 48px de altura/largura, respeitando WCAG 2.5.5 e 2.5.8.
- **Ritmo Vertical:** Grade de espaçamento baseada em incrementos de 4px (padrões frequentes: 12px, 16px, 20px, 24px).
- **Sem Rolagem Horizontal:** Toda informação é autoajustável e quebra fluidamente sem gerar barras de rolagem horizontais em telas estreitas.

## Elevation & Depth

O sistema prioriza superfícies planas com elevação tonal e bordas nítidas de 1px a 2px (`border: 1px solid #e2e8f0` no modo claro e `border: 1px solid #27272a` no modo escuro). 

Sombras pesadas e efeitos de reflexo artificial são expressamente banidos. Sombras suaves (`0 0 40px rgba(0, 0, 0, 0.05)`) são reservadas exclusivamente para o contorno do frame do dispositivo em visualização desktop.

### Named Rules
**A Regra da Borda Estrutural.** A separação de elementos é dada por linhas de contorno limpas e sutis, e nunca por sombras de bloco espessas ou gradientes falsos.

## Shapes

- **Cantos Arredondados:** 12px (`rounded-xl`) para botões de formulário e inputs; 16px (`rounded-2xl`) para blocos de alerta e cartões estruturais.
- **Pills e Badges:** 9999px (`rounded-full`) para contadores de apoio, etiquetas de conformidade e status de rede online/offline.

## Components

- **Botão Primário:** Altura mínima de 48px, cantos de 12px, texto em peso 700+, ícone alinhado à esquerda.
- **Campo de Formulário:** `input` e `textarea` com preenchimento interno confortável (12px), borda visível de 1px a 2px, fonte mínima de 16px para evitar zoom indesejado em iOS/Android.
- **Anel de Foco (WCAG 2.4.7):** Contorno de 2px a 3px com recuo (`outline-offset: 2px`) perceptível tanto no tema claro quanto no escuro.
- **Toast Acessível:** Caixa de notificação flutuante com `aria-live="polite"`, ícone vetorial claro e botão de descarte direto.

## Do's and Don'ts

### Do
- Use linguagem direta, empática e acolhedora voltada ao cidadão comum.
- Garanta que toda ação de emergência funcione mesmo se o aparelho estiver offline.
- Mantenha áreas de clique generosas para facilitar o uso por idosos e pessoas com tremores motores.
- Teste e valide sempre no modo de alto contraste para leitura sob sol a pino.

### Don't
- Não insira modais bloqueantes que impeçam o cidadão de consultar informações vitais.
- Não use textos em cinza claro sobre fundos coloridos.
- Não colete CPF, telefone ou informações invasivas desnecessárias.
- Não exiba gráficos complexos que dependam de legendas inacessíveis a daltônicos.
