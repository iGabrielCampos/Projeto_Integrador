---
id: especificacao-telas-prototipo-aguaviva-pb
etapa: 5
autor: Gabriel Amancio, Gustavo Antonio
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F007
---

# Especificação Textual e Wireframes do Protótipo – ÁguaViva PB

Esta especificação descreve a composição visual, elementos interativos, rotulagem acessível e comportamento das **8 telas e estados de interface** projetados para o protótipo da solução tecnológica no **Figma**.

---

### Tela 01: Página Inicial / Dashboard Comunitário (Home)
- **Objetivo:** Fornecer visão panorâmica do abastecimento local, acesso imediato ao botão de reporte e alertas sanitários ativos.
- **Componentes Principais:**
  - *Cabeçalho:* Logotipo "ÁguaViva PB", botão de acessibilidade (aumento de contraste / tamanho de fonte) e seletor rápido de cidade ("João Pessoa / PB").
  - *Card de Alerta Superior (Destaque):* Faixa amarela/vermelha com alto contraste (4.5:1 `[F007]`): "Atenção: Interrupção programada de água em Mangabeira e Valentina - Previsão de retorno: 18h".
  - *Ação Principal (CTA Central):* Botão grande (altura mínima de 56px) com ícone de gota d'água: **"Reportar Falta de Água ou Esgoto"**.
  - *Mini-Mapa de Calor:* Mapa compacto da região metropolitana indicando bairros com mais queixas nas últimas 24h.
  - *Barra de Navegação Inferior (Bottom Bar):* Ícones descritivos com rótulos textuais: "Início", "Mapa de Queixas", "Guia de Saúde" e "Ajuda".

---

### Tela 02: Formulário Acessível de Registro de Ocorrência
- **Objetivo:** Coleta ágil e intuitiva de relatos por cidadãos em smartphones simples.
- **Componentes Principais:**
  - *Passo 1 (Seleção de Categoria):* 4 botões de seleção grandes com ícones e texto:
    1. "Falta de Água (Torneira Seca)"
    2. "Água com Cor ou Cheiro Estranho (Barrenta / Amarela)"
    3. "Esgoto a Céu Aberto / Fossa Estourada"
    4. "Cano Limpo Vazando na Rua (Desperdício)"
  - *Passo 2 (Localização):* Botão "Usar Minha Localização Atual (GPS)" ou campo de texto com autocompletar de bairros de João Pessoa (ex.: Cristo Redentor, Mandacaru, Gramame).
  - *Passo 3 (Detalhes Opcionais):* Caixa de texto simples: "Comentário (opcional: há quantos dias está sem água?)" e botão "Anexar Foto da Água/Esgoto".
  - *Botão de Envio:* Botão verde acessível: **"Confirmar e Enviar Relato"**.

---

### Tela 03: Confirmação de Envio com Protocolo Anônimo (Sucesso)
- **Objetivo:** Assegurar ao cidadão que sua ocorrência foi registrada, resguardando sua identidade sob a LGPD `[F001]`.
- **Componentes Principais:**
  - *Ícone de Sucesso:* Checkmark verde com mensagem: "Relato Registrado com Sucesso!".
  - *Código do Protocolo:* Número alfanumérico gerado (ex.: `#AV-2026-8941`).
  - *Nota de Privacidade (LGPD):* "Seus dados foram anonimizados. Nenhuma informação pessoal será compartilhada com terceiros."
  - *Orientações Imediatas:* "Se a água estiver com cor ou odor alterado, consulte as recomendações de fervura e cloração caseira no Guia de Saúde."
  - *Botões de Ação:* "Ver no Mapa Comunitário" e "Voltar ao Início".

---

### Tela 04: Mapa Interativo de Calor e Dados de Saúde (Heatmap)
- **Objetivo:** Visualização geoespacial das ocorrências acumuladas e correlação com indicadores públicos do DATASUS `[F072]`.
- **Componentes Principais:**
  - *Filtros de Camada:* Alternar visualização entre "Falta de Água", "Água Contaminada" e "Vazamento de Esgoto".
  - *Filtro Temporal:* "Últimas 24 horas", "Últimos 7 dias", "Este mês".
  - *Cards Informativos por Bairro:* Ao clicar em um bairro (ex.: Bairro São José), abre-se painel lateral:
    - Ocorrências registradas: 42 relatos;
    - Tempo médio sem abastecimento: 36 horas;
    - Alerta epidemiológico correlacionado: Risco moderado de doenças diarreicas agudas.

---

### Tela 05: Guia Prático de Cuidados e Higienização da Água
- **Objetivo:** Fornecer educação em saúde preventiva para famílias em situação de desabastecimento ou suspeita de água contaminada.
- **Componentes Principais:**
  - *Cards Educativos Ilustrados em Linguagem Simples:*
    1. "Como clorar a água com água sanitária (2 gotas por litro para beber)";
    2. "Tempo correto de fervura (pelo menos 3 minutos em borbulha)";
    3. "Como lavar a caixa d'água com segurança a cada 6 meses".
  - *Alerta de Saúde:* "Sintomas de alerta em crianças e idosos: vômito frequente, diarreia e febre. Procure a Unidade de Saúde da Família (USF) mais próxima."

---

### Tela 06: Módulo Especializado do Agente Comunitário de Saúde (ACS)
- **Objetivo:** Permitir ao ACS registrar relatórios coletivos obtidos durante visitas domiciliares no território.
- **Componentes Principais:**
  - *Identificação do Agente:* Login simplificado por matrícula institucional (ex.: USF Mangabeira).
  - *Registro em Lote:* Formulário rápido para apontar: "Nesta rua (Rua do Sol), 12 famílias relatam água barrenta há 3 dias".
  - *Checklist Epidemiológico:* Campo para notificar número de moradores com sintomas diarreicos na microárea visitada.
  - *Botão Exportar:* "Gerar Relatório para a Secretaria Municipal de Saúde".

---

### Tela 07: Estado Vazio e Conexão Offline (Empty State)
- **Objetivo:** Informar com transparência quando não há queixas ativas ou quando o morador está sem conexão de internet.
- **Componentes Principais:**
  - *Ilustração:* Desenho vetorial de torneira fechada e gota serena.
  - *Mensagem Principal (Modo Offline):* "Você está sem sinal de internet no momento. Não se preocupe: seu relato foi salvo na memória do aparelho e será transmitido automaticamente assim que a conexão retornar."
  - *Indicador Visual:* Faixa superior azul com ícone de nuvem sincronizando: "Modo Offline Ativo".

---

### Tela 08: Estado de Erro e Tratamento Acessível de Falhas (Error State)
- **Objetivo:** Comunicar falhas operacionais sem assustar o usuário e indicando caminho de recuperação.
- **Componentes Principais:**
  - *Ilustração:* Ícone amigável de alerta de rede.
  - *Mensagem Clara (Sem Códigos Técnicos incompreensíveis):* "Não conseguimos enviar seu relato agora devido a uma oscilação no servidor. Seus dados estão seguros."
  - *Botão de Ação Primária:* **"Tentar Novamente Agora"**.
  - *Canal Alternativo:* "Se o problema persistir, anote o protocolo temporário e tente mais tarde."
