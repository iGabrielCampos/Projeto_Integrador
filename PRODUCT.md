# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Protótipo em HTML/CSS/JS vanilla (HTML5 semântico, Tailwind CSS via CDN e Vanilla JavaScript ES6+); arquitetura-alvo React + Vite. Web Storage e modo offline simulado no protótipo para demonstração de fluxo; sem dependências pesadas de runtime para assegurar carregamento instantâneo em conexões 2G/3G e aparelhos de entrada.

## Users

Cidadãos e comunidades periféricas em situação de vulnerabilidade hídrica na Paraíba (com foco inicial na Ilha do Bispo, Várzea, Mandacaru e São Rafael em João Pessoa), lideranças comunitárias locais, operadores da Defesa Civil e técnicos de saneamento da CAGEPA.

## Product Purpose

ÁguaViva PB é uma plataforma cívica de monitoramento colaborativo e garantia da cidadania hídrica (ODS 6 da ONU), que capacita o cidadão a reportar desabastecimentos e vazamentos, verificar laudos de potabilidade da água, solicitar carros-pipa emergenciais para creches e postos de saúde, e auditar indicadores de transparência sobre perdas na rede pública. O sucesso do produto significa reduzir o tempo de resposta das concessionárias e garantir abastecimento prioritário a instituições essenciais.

## Positioning

A única solução de telemetria cidadã hiperlocal projetada especificamente para a realidade do Nordeste brasileiro: protótipo conceitual navegável; a persistência offline real (Service Worker + IndexedDB) está especificada para a versão de produção (quando o aparelho está sem crédito ou sinal de celular), consome menos de 300 KB por sessão completa e não exige login, CPF ou burocracia para acolher a denúncia comunitária.

## Operating Context

- Aparelhos Android de entrada com telas compactas (360px a 440px de largura).
- Uso sob incidência direta de luz solar forte tropical (exigindo modo de alto contraste com taxa superior a 14:1) ou em ambientes com iluminação precária durante blecautes e cortes de energia.
- Usuários com baixa literacia digital ou baixa acuidade visual.
- Situações de emergência e alta ansiedade decorrentes da falta prolongada de água potável (mais de 48 horas).

## Capabilities and Constraints

- **Offline-First Nativo (arquitetura-alvo):** Armazenamento resiliente no navegador e fila automática de sincronização assim que a conectividade for detectada.
- **Compressão de Mídia no Cliente:** Compressão client-side de fotografias em formato WebP (redução de 90% no tamanho do arquivo) para preservar a franquia de dados móveis do cidadão.
- **Conformidade Acessível:** Nível WCAG 2.2 AA e AAA em itens críticos (alvos de toque mínimos de 48x48px, indicador de foco `:focus-visible` de 3px, ampliação tipográfica em +200%).
- **Privacidade Cidadã Estrita (LGPD - Lei nº 13.709/2018):** Minimização radical de dados; proibição de coleta de CPF, RG ou números de telefone particulares. Geolocalização agregada por setor censitário para evitar retaliações.

## Brand Commitments

- **Nome Oficial:** ÁguaViva PB.
- **Voz do Produto:** Cidadã, acolhedora, transparente, empática e resolutiva. Sem jargões técnicos herméticos e sem tom burocrático ou punitivo.
- **Paleta Institucional:** Tons oceânicos de água tratada (Teal/Emerald), amarelo solar de alerta cívico e preto absoluto OLED para foco e leitura externa.

## Evidence on Hand

- **Dados Oficiais de Perdas:** SNIS (Sistema Nacional de Informações sobre Saneamento) comprovando 47,0% de perdas físicas na distribuição de água tratada na Paraíba.
- **Parâmetros Sanitários:** Portaria GM/MS nº 888 do Ministério da Saúde para cloro residual (0,2 a 5,0 mg/L) e turbidez (≤ 5,0 NTU).
- **Testes com Usuários Reais:** 6 participantes voluntários (36 registros avaliados), com tempo médio de relato de 59,4 s, taxa de sucesso de 97,2% (35/36) e satisfação média de 4,58 / 5,0 (SUS 84,2).

## Product Principles

1. **Estar offline é operação normal, não um erro:** O aplicativo nunca exibe telas de bloqueio de conexão; na versão de produção, os dados serão guardados localmente; o protótipo atual demonstra o fluxo visual.
2. **Contraste e clareza salvam vidas:** Informações sanitárias e alertas devem ser legíveis sob sol a pino, sem degradar em cinzas lavados.
3. **Respeito absoluto aos dados do cidadão:** Coletar estritamente o necessário para encaminhar a demanda pública, sem identificadores invasivos.
4. **Agilidade máxima em emergências:** Toda ação prioritária (relatar falta d'água ou pedir caminhão-pipa) deve ser concluída em até 2 passos simples.

## Accessibility & Inclusion

- Conformidade com as diretrizes WCAG 2.2 AA/AAA.
- Áreas de clique/toque de no mínimo 48x48px em todos os controles primários.
- Modo de alto contraste verdadeiro (taxa > 14:1) e ampliação tipográfica (+200%).
- Suporte total a leitores de tela com `aria-live="polite"` em notificações e atualizações de fila.
- Compatibilidade nativa com a diretiva `prefers-reduced-motion`.
