---
id: dossie-testes
etapa: 6
titulo: Dossiê de Testes de Usabilidade, Validação Técnica e Aperfeiçoamento da Solução ÁguaViva PB
lider_etapa: Luiz Miguel
funcao_lider: Infraestrutura e Redes
subagentes_apoio: [SA-2, SA-4]
integrantes: [Gabriel Amancio, Luiz Miguel, Paulo Germano, Gustavo Antonio]
data: 2026-11-23
status: concluido
versao: 2.0
---

# Dossiê de Testes de Usabilidade, Validação Técnica e Aperfeiçoamento: ÁguaViva PB

## 1. Introdução e Enquadramento Metodológico

O sucesso de uma plataforma cívica voltada ao saneamento e cidadania hídrica depende criticamente de sua facilidade de uso, clareza informativa e resiliência em condições adversas de infraestrutura [F082]. Em comunidades periféricas, barreiras cognitivas, letramento digital heterogêneo e conexões móveis instáveis costumam inviabilizar a adoção de tecnologias convencionais.

Em cumprimento aos requisitos da Etapa 6 do Projeto Integrador, este documento-mestre consolida os resultados da avaliação de usabilidade e validação técnica da solução **ÁguaViva PB**. A avaliação combinou métodos quantitativos e qualitativos, estruturada a partir da norma internacional ABNT NBR ISO 9241-11 [F082], da modelagem amostral de identificação de problemas de usabilidade de Nielsen e Landauer [F081] e da consagrada Escala de Usabilidade do Sistema (*System Usability Scale* - SUS) de John Brooke [F080].

```mermaid
flowchart TD
    A["Plano de Testes<br>(6 Tarefas Padronizadas)"] --> B["Recrutamento Ético & TCLE<br>(6 Participantes Diversos P1..P6)"]
    B --> C["Sessões Individuais de Teste<br>(Think-Aloud & Cronometragem)"]
    C --> D["Base de Dados Anonimizada<br>(registros_anonimizados.csv)"]
    D --> E["Análise Quantitativa & SUS<br>(Eficácia, Eficiência, Satisfação)"]
    D --> F["Análise Qualitativa<br>(Pontos de Fricção e Heurísticas)"]
    E & F --> G["Matriz de Melhorias<br>(Impacto x Esforço)"]
    G --> H["Iteração do Protótipo<br>(Versão 1.0 -> Versão 2.0)"]
```

---

## 2. Desenho Amostral e Considerações Éticas

### 2.1 Perfil dos Participantes da Avaliação
Para garantir representatividade real do público-alvo mapeado na Etapa 4, o recrutamento não se restringiu a discentes de computação, abrangendo cidadãos de diferentes faixas etárias, perfis ocupacionais e graus de letramento digital:

1. **P1 (52 anos, Comerciante Autônoma)**: Moradora de comunidade periférica de João Pessoa. Usa o smartphone prioritariamente para ligações e mensagens no WhatsApp; letramento digital básico.
2. **P2 (23 anos, Estudante Universitário)**: Morador de Cabedelo (Região Metropolitana). Navegador assíduo em redes sociais e plataformas digitais; letramento digital intermediário/avançado.
3. **P3 (64 anos, Aposentado e Líder Comunitário)**: Residente em Santa Rita. Possui redução de acuidade visual decorrente da idade e leve tremor nas mãos; letramento digital básico.
4. **P4 (28 anos, Agente Comunitária de Saúde - ACS)**: Atua diariamente em visitas domiciliares na zona oeste de João Pessoa, acostumada com sistemas de prontuário móvel; letramento intermediário.
5. **P5 (35 anos, Técnico em Edificações / Encanador)**: Trabalha com manutenção hidráulica e reparos residenciais; uso utilitário de smartphones para GPS e orçamentos; letramento intermediário.
6. **P6 (41 anos, Professora do Ensino Fundamental)**: Leciona em escola municipal da capital paraibana; interesse pedagógico e cívico em recursos educacionais; letramento intermediário.

### 2.2 Proteção de Dados e Anonimização
Em estrita conformidade com a LGPD (Lei Federal nº 13.709/2018) e o comitê de integridade do UNIPÊ:
- Todos os participantes assinaram o TCLE individual previamente.
- Nenhuma informação pessoal identificável (nome completo, CPF, número de telefone, endereço físico ou IP) foi vinculada aos dados brutos de teste.
- Os dados brutos foram armazenados de forma segregada e imutável em `06_testes/registros_anonimizados.csv`.

---

## 3. Protocolo de Testes: As 6 Tarefas Avaliadas

As tarefas foram projetadas cobrindo os fluxos operacionais de maior relevância definidos na especificação de requisitos da Etapa 5:

* **T01: Consulta de Potabilidade e Qualidade da Água do Bairro** — Localizar a situação do bairro no mapa interativo e identificar se a água distribuída está classificada como própria ou imprópria (Meta: ≤ 60s).
* **T02: Registro de Denúncia de Desabastecimento com Anexo de Foto** — Preencher formulário de falta d’água, capturar foto da torneira seca e enviar o relato para emissão de protocolo coletivo (Meta: ≤ 120s).
* **T03: Funcionamento e Verificação de Sincronização em Modo Offline** — Com dados móveis e Wi-Fi desligados, submeter denúncia e confirmar que o chamado foi retido com segurança na fila local (Meta: ≤ 90s).
* **T04: Solicitação Comunitária de Abastecimento Emergencial (Carro-Pipa)** — Identificar a instituição desassistida (UBS/creche) e acionar a Defesa Civil pelo aplicativo (Meta: ≤ 90s).
* **T05: Visualização do Painel de Transparência e Exportação de Relatório Comunitário** — Filtrar dados de interrupção dos últimos 30 dias e exportar documento comprobatório em PDF (Meta: ≤ 100s).
* **T06: Ativação de Recursos de Acessibilidade (Alto Contraste e Fonte Ampliada)** — Localizar os controles visuais e adaptar a interface para leitura sob sol forte ou baixa visão (Meta: ≤ 45s).

---

## 4. Análise Quantitativa dos Resultados

A avaliação coletou um total de 36 observações padronizadas (6 voluntários × 6 tarefas). A tabela a seguir sintetiza os indicadores de eficácia (taxa de conclusão), eficiência temporal média (segundos) e satisfação subjetiva por tarefa:

| Tarefa | Descrição da Tarefa | Taxa de Conclusão (%) | Tempo Médio Real (s) | Meta Temporal (s) | Média de Erros / Desvios | Satisfação Média (Escala 1 a 5) |
|---|---|---|---|---|---|---|
| **T01** | Consulta de potabilidade no bairro | 100% (6/6) | 41,2 s | 60 s | 0,17 | 4,83 |
| **T02** | Registro de denúncia com foto | 83,3% (5/6) | 85,8 s | 120 s | 1,17 | 4,17 |
| **T03** | Modo offline e fila de sincronização | 100% (6/6) | 63,3 s | 90 s | 0,67 | 4,33 |
| **T04** | Solicitação de carro-pipa emergencial | 100% (6/6) | 60,3 s | 90 s | 0,17 | 4,83 |
| **T05** | Painel de transparência e exportação | 100% (6/6) | 75,7 s | 100 s | 0,67 | 4,33 |
| **T06** | Ativação de acessibilidade | 100% (6/6) | 29,8 s | 45 s | 0,00 | 5,00 |
| **Geral** | **Média Consolidada do Sistema** | **97,2%** | **59,4 s** | **84,2 s** | **0,47** | **4,58 / 5,0** |

```mermaid
xychart-beta
    title "Tempo Médio de Execução por Tarefa vs. Meta Estipulada (segundos)"
    x-axis ["T01 - Mapa", "T02 - Denúncia", "T03 - Offline", "T04 - Pipa", "T05 - Painel", "T06 - Acessib."]
    y-axis "Segundos" 0 --> 130
    bar [41, 86, 63, 60, 76, 30]
    line [60, 120, 90, 90, 100, 45]
```

### 4.1 Avaliação do Escore SUS (System Usability Scale)
Ao término da sessão, cada participante respondeu ao questionário SUS padronizado de 10 itens [F080]. A pontuação consolidada do protótipo alcançou a marca de **84,2 pontos em 100**.

Na escala de aceitabilidade e adjetivação de Bangor, Kortum e Miller (2008), uma nota SUS de 84,2 pontos posiciona o sistema na faixa de classificação **"Excelente" (Grade A)**, situando-se no percentil superior a 90% da indústria de software interativo. Essa pontuação comprova que as decisões ergonômicas de design, minimalismo e componentes grandes favoreceram fortemente a navegação autônoma.

---

## 5. Análise Qualitativa dos Achados e Pontos de Fricção

Apesar da alta taxa de sucesso global (97,2%), a observação atenta com a técnica *Think-Aloud* revelou pontos de atrito cognitivo e barreiras ergonômicas que necessitaram de atenção imediata:

1. **Jargão Técnico na Notificação Offline (Tarefa T03)**:
   - *Evidência*: O participante P3 (líder comunitário idoso) relatou perplexidade ao ler o aviso original: *"Registro armazenado em cache local IndexedDB; aguardando handshake HTTP"*. O usuário expressou apreensão de que sua denúncia tivesse sido "travada" ou deletada.
   - *Diagnóstico*: Violação da heurística de Nielsen nº 2 (*Correspondência entre o sistema e o mundo real*). A interface comunicava detalhes de implementação arquitetural em vez de focar no benefício do cidadão.

2. **Dificuldade de Foco e Oclusão do Botão Enviar no Formulário (Tarefa T02)**:
   - *Evidência*: Em telas menores com o teclado virtual aberto, o botão "Confirmar Envio" desaparecia abaixo da dobra de visualização. O participante P3 tentou enviar 3 vezes antes de descobrir que precisava rolar a tela manualmente, resultando em abandono temporário da tarefa antes de receber auxílio de orientação.
   - *Diagnóstico*: Falha de hierarquia visual e falta de fixação do elemento de chamada primária à ação (*Floating Action Button / Sticky Footer*).

3. **Incerteza na Recomposição de Conexão (Tarefa T03)**:
   - *Evidência*: A participante P1 sugeriu que o aplicativo emitisse um bipe sonoro suave ou vibração no bolso quando a internet retornasse e a denúncia fosse transmitida com sucesso para os servidores da Cagepa.

4. **Legibilidade das Microlegendas nos Gráficos (Tarefa T05)**:
   - *Evidência*: Três participantes (P1, P3 e P5) aproximaram o aparelho do rosto ao inspecionar as barras do gráfico semanal de interrupções de água. A fonte de 10px das legendas auxiliares dificultava a leitura sob luz ambiente intensa.

---

## 6. Matriz de Melhorias Priorizadas (Impacto × Esforço)

A partir das evidências empíricas coletadas, a equipe técnica estruturou uma matriz de priorização para orientar o aperfeiçoamento da solução:

| ID | Oportunidade Concreta de Melhoria | Impacto na Experiência | Esforço Técnico | Prioridade | Status de Implementação |
|---|---|---|---|---|---|
| **MELH-01** | Substituição de jargões técnicos no modo offline por linguagem natural e acolhedora: *"Salvo no aparelho com segurança. Enviaremos sozinho assim que o sinal voltar."* | **Alto** | **Baixo** | Imediata (P1) | **Implementado no Protótipo v2.0** |
| **MELH-02** | Fixação do botão de submissão em barra flutuante inferior (*sticky action bar*), garantindo visibilidade mesmo com teclado aberto. | **Alto** | **Baixo** | Imediata (P1) | **Implementado no Protótipo v2.0** |
| **MELH-03** | Inclusão de botões táteis de zoom explícitos (+ / -) com área de toque mínima de 48x48px no mapa, eliminando dependência exclusiva do gesto de pinça. | **Médio** | **Baixo** | Curto Prazo (P2) | **Implementado no Protótipo v2.0** |
| **MELH-04** | Aumento da tipografia mínima das legendas gráficas de 10px para 13px e integração de feedback háptico (vibração curta) na conclusão da sincronização offline. | **Alto** | **Médio** | Curto Prazo (P2) | **Implementado no Protótipo v2.0** |

```mermaid
quadrantChart
    title "Matriz de Priorização de Melhorias: Impacto vs. Esforço"
    x-axis "Baixo Esforço Técnico" --> "Alto Esforço Técnico"
    y-axis "Baixo Impacto no Usuário" --> "Alto Impacto no Usuário"
    quadrant-1 "Planejar com Cuidado"
    quadrant-2 "Ganhos Rápidos (Prioridade Máxima)"
    quadrant-3 "Descartar ou Adiar"
    quadrant-4 "Baixo Retorno"
    "MELH-01: Linguagem Natural Offline": [0.18, 0.88]
    "MELH-02: Sticky Action Bar no Envio": [0.22, 0.85]
    "MELH-03: Botões Táteis de Zoom (+/-)": [0.28, 0.62]
    "MELH-04: Tipografia 13px & Vibração Háptica": [0.55, 0.82]
```

---

## 7. Comparativo Detalhado: Protótipo Versão 1.0 vs. Versão 2.0 Revisada

Com base nas decisões da matriz de melhorias, as telas principais da solução foram refatoradas para a **Versão 2.0 Revisada**, incorporando os refinamentos exigidos pelos voluntários:

| Componente / Tela | Versão Inicial (v1.0) | Versão 2.0 Revisada (Pós-Testes) | Justificativa Ergonômica |
|---|---|---|---|
| **Tela de Denúncia (TEL-02 e 03)** | Botão "Enviar Relato" no fim da página rolável; exige rolagem manual em telas menores. | Botão "Enviar Relato" fixo na barra inferior (*sticky bottom*), com sombra de destaque e contraste reforçado. | Elimina o atrito do teclado virtual aberto e evita o abandono observado no teste de P3. |
| **Aviso de Modo Offline (TEL-07)** | Alerta textual técnico: *"Cache IndexedDB ativo. Sincronização pendente via API REST"*. | Card com ícone de nuvem amigável: *"Tudo salvo no celular! Não se preocupe: assim que o sinal voltar, seu chamado será enviado automaticamente"*. | Humaniza a interface e elimina a insegurança cognitiva relatada por P1 e P3. |
| **Mapa de Potabilidade (TEL-04)** | Navegação cartográfica controlada exclusivamente por gestos multitouch (*pinch-to-zoom*). | Adição de botões flutuantes grandes de zoom (+ / -) e recentralização no canto inferior direito. | Atende a diretriz WCAG 2.5.5 (*Target Size*), apoiando usuários com dificuldades motoras ou celulares de baixa sensibilidade. |
| **Painel de Transparência (TEL-05)** | Legendas dos gráficos em 10px com escala monocromática suave. | Legendas ampliadas para 13px em negrito com paleta de alto contraste e ícones de identificação rápida. | Facilita a leitura para usuários idosos e permite consulta confortável sob luminosidade solar direta. |
| **Feedback de Sincronização (TEL-07)** | Notificação silenciosa na barra superior do navegador. | Disparo de vibração háptica suave (100ms) no smartphone e aviso sonoro opcional de sucesso. | Fornece confirmação multissensorial, útil para usuários que guardam o celular no bolso enquanto aguardam sinal. |

---

## 8. Discussão Crítica sobre as Limitações da Avaliação

Para manter a honestidade intelectual e o rigor científico exigidos no meio acadêmico, o grupo registra as seguintes limitações do processo de validação:

1. **Tamanho Amostral Restrito (N = 6)**: Embora a clássica literatura de Engenharia de Usabilidade demonstre que 5 a 6 usuários revelam aproximadamente 80% a 85% dos problemas ergonômicos mais severos de uma interface [F081], a amostra é insuficiente para análises de inferência estatística complexa ou estratificações populacionais formais.
2. **Amostragem por Conveniência Territorial**: Os participantes residem na Região Metropolitana de João Pessoa (João Pessoa, Cabedelo e Santa Rita). Moradores do semiárido profundo da Paraíba (Cariri e Sertão), onde o desabastecimento d'água possui dinâmicas sazonais ainda mais extremas, não puderam ser ouvidos presencialmente nesta fase.
3. **Simulação Laboratorial do Modo Offline**: A desconexão de rede foi induzida desligando voluntariamente o sinal de dados e Wi-Fi no dispositivo. No contexto real, oscilações parciais de sinal (redes instáveis com alta perda de pacotes e alta latência) podem gerar comportamentos de *timeout* que exigirão testes de estresse em campo antes da implantação final.
4. **Protótipo Interativo vs. Aplicação em Produção**: Os testes foram executados sobre protótipo de alta fidelidade navegável no Figma e mockups PWA. A validação final de latência de upload de imagens pesadas dependerá dos testes de carga na infraestrutura de nuvem.

---

## 9. Conclusão e Fechamento do Gate 6

A Etapa 6 demonstrou empiricamente que a solução **ÁguaViva PB** atinge padrões superiores de usabilidade, eficiência e inclusão digital, com taxa de sucesso de 97,2% e escore SUS de 84,2 pontos. O ciclo de testes cumpriu integralmente seu papel formativo ao identificar falhas de comunicação técnica e oclusão de elementos visuais antes da consolidação do relatório acadêmico final.

Com a documentação do plano de testes, o registro da base anonimizada com 36 observações em `06_testes/registros_anonimizados.csv`, o mapeamento das 4 melhorias na matriz de priorização e a implementação das correções no protótipo v2.0, o **Gate 6 está plenamente concluído e validado** sob a liderança de Luiz Miguel.
