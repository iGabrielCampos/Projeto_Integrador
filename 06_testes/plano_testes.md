---
id: plano-testes
etapa: 6
lider: Luiz Miguel
funcao: Infraestrutura e Redes
subagentes_apoio: [SA-2, SA-4]
data: 2026-11-23
status: concluido
solucao: AguaViva PB
versao_prototipo: 1.0
---

# Plano de Testes de Usabilidade e Validação Técnica: ÁguaViva PB

## 1. Contexto e Objetivos da Avaliação

A solução **ÁguaViva PB** visa capacitar comunidades vulneráveis da Paraíba na fiscalização cidadã da água e saneamento (ODS 6). O presente plano define o protocolo de testes de usabilidade com protótipo de alta fidelidade e cenários interativos, focado em avaliar a eficácia, a eficiência, a tolerância a falhas e a satisfação de uso, em conformidade com as normas ISO 9241-11 e as diretrizes de acessibilidade WCAG 2.1 nível AA.

### 1.1 Objetivos Específicos
1. Mensurar a taxa de conclusão independente em 6 tarefas críticas do fluxo de monitoramento e denúncia comunitária.
2. Identificar gargalos cognitivos, ruídos visuais e barreiras de acessibilidade para usuários com baixa escolaridade ou baixo letramento digital.
3. Testar a clareza da comunicação do estado de rede offline (PWA) e fila de sincronização.
4. Coletar percepções qualitativas e pontuações na escala SUS (*System Usability Scale*) para fundamentar a matriz de melhorias e a iteração do protótipo (Versão 2.0).

---

## 2. Perfil da Amostra de Participantes (Critérios Éticos e LGPD)

Para evitar viés exclusivo de estudantes da área de computação, a amostra de 6 participantes voluntários adultos foi desenhada para contemplar diversidade etária, socioeconômica e níveis de proficiência digital, representando as personas estabelecidas na Etapa 4 (Maria de Fátima, Carlos Eduardo e comunidade geral):

| ID | Faixa Etária | Ocupação / Perfil | Nível de Letramento Digital | Dispositivo Utilizado no Teste |
|---|---|---|---|---|
| **P1** | 52 anos | Comerciante autônoma (Residente em comunidade periférica de João Pessoa) | Básico (Usa prioritariamente WhatsApp e chamadas) | Smartphone Android 6.5" |
| **P2** | 23 anos | Estudante universitário de Pedagogia (Morador da Região Metropolitana de JP) | Intermediário (Navegação web frequente, redes sociais) | Smartphone Android 6.1" |
| **P3** | 64 anos | Aposentado / Líder comunitário de associação de moradores (Várzea Nova / Santa Rita) | Básico (Dificuldade motora fina e baixa acuidade visual) | Smartphone Android 6.7" |
| **P4** | 28 anos | Agente Comunitária de Saúde (ACS) | Intermediário a Avançado (Usa tablets e sistemas de prontuário) | Tablet Android 10.1" / Mobile |
| **P5** | 35 anos | Técnico em Edificações / Encanador autônomo | Básico a Intermediário (Aplicações utilitárias de mapas e mensagens) | Smartphone Android 6.4" |
| **P6** | 41 anos | Professora do Ensino Fundamental da rede pública | Intermediário (Sistemas de gestão escolar e navegação mobile) | Smartphone iPhone iOS 6.1" |

### 2.1 Salvaguardas Éticas e Consentimento
- **Anonimização estrita**: Nenhum nome civil, CPF, endereço domiciliar ou número telefônico foi coletado ou persistido nos registros do projeto.
- **TCLE**: Todos os voluntários assinaram previamente o Termo de Consentimento Livre e Esclarecido (`apendices/termos/tcle.md`), com autorização para registro de métricas de tempo e observações de tela.
- **Voluntariedade e Parada Livre**: Os participantes foram informados de que o teste avaliava o sistema, e não a capacidade individual do usuário, podendo interromper a sessão a qualquer momento sem qualquer ônus.

---

## 3. Ambiente e Metodologia de Execução

- **Método**: Avaliação supervisionada individual com técnica de *Think-Aloud* (pensar em voz alta), moderada pelo líder da etapa (Luiz Miguel) e observada por Gabriel Amancio e Paulo Germano.
- **Ambiente**: Laboratório de Informática do UNIPÊ e sessões remotas via Google Meet com espelhamento de tela móvel para voluntários externos.
- **Instrumentos**: Cronômetro digital de alta precisão, formulário padronizado de anotações comportamentais e questionário SUS pós-teste.

---

## 4. Relação de Tarefas de Teste Padronizadas (T01 a T06)

### Tarefa T01: Consulta de Potabilidade e Qualidade da Água do Bairro
- **Cenário**: O participante percebeu coloração turva na água da torneira de sua residência e deseja saber se o sistema acusa contaminação ou inconformidade recente no seu bairro.
- **Instrução dada**: *"Localize no aplicativo o mapa da sua região e verifique se a água distribuída hoje em seu bairro está classificada como Própria ou Imprópria para consumo."*
- **Caminho ideal**: Tela Inicial (TEL-01) -> Clicar no botão 'Ver Mapa de Qualidade' -> Selecionar ou buscar bairro -> Visualizar card de indicador com status verde/vermelho (TEL-04).
- **Critério de Sucesso**: Conclusão autônoma em até 60 segundos, identificando corretamente o status de potabilidade sem assistência do facilitador.

### Tarefa T02: Registro de Denúncia de Desabastecimento com Anexo de Foto
- **Cenário**: O bairro está sem abastecimento há mais de 72 horas consecutivas sem aviso prévio da concessionária. O participante precisa registrar um relato para gerar protocolo coletivo.
- **Instrução dada**: *"Abra o formulário de relato, selecione o problema 'Falta d’Água', tire ou anexe uma foto da torneira seca e envie o relato confirmando a localização."*
- **Caminho ideal**: Tela Inicial (TEL-01) -> Botão flutuante 'Nova Denúncia' -> Selecionar 'Falta d’Água' -> Anexar foto -> Validar endereço via GPS/manual -> Clicar 'Enviar Relato' -> Receber comprovante com número de protocolo (TEL-02 e TEL-03).
- **Critério de Sucesso**: Conclusão em até 120 segundos, gerando com sucesso o protocolo alfanumérico sem erros impeditivos de preenchimento.

### Tarefa T03: Funcionamento e Verificação de Sincronização em Modo Offline
- **Cenário**: Em decorrência de chuva forte ou instabilidade de operadora, o smartphone fica completamente sem sinal de internet (dados móveis desligados). O usuário precisa enviar um reporte de esgoto a céu aberto.
- **Instrução dada**: *"Com a internet desligada, faça um relato de 'Esgoto a Céu Aberto'. Verifique se o aplicativo informa que o chamado ficou salvo na fila para envio automático quando o sinal voltar."*
- **Caminho ideal**: Desconexão da rede móvel -> Abertura de formulário de relato -> Preenchimento e clique em 'Enviar' -> Exibição do banner 'Modo Offline: Registro guardado no dispositivo' -> Acesso à aba 'Meus Relatos / Fila Local' (TEL-07).
- **Critério de Sucesso**: Conclusão em até 90 segundos, compreendendo que o dado não foi perdido e localizando o ícone de pendência amarela na fila local.

### Tarefa T04: Solicitação Comunitária de Abastecimento Emergencial (Carro-Pipa)
- **Cenário**: Creche comunitária ou unidade básica de saúde do bairro está desprovida de água potável há 4 dias. O participante precisa solicitar o direcionamento de caminhão-pipa da Defesa Civil.
- **Instrução dada**: *"Acesse a área de 'Serviços Emergenciais', selecione 'Solicitação de Carro-Pipa', confirme o endereço da instituição e confirme a solicitação."*
- **Caminho ideal**: Tela Inicial -> Menu 'Serviços Emergenciais' -> Opção 'Caminhão-Pipa Comunitário' -> Preenchimento de endereço e ponto de referência comunitário -> Botão 'Confirmar Solicitação' -> Exibição de prazo estimado de atendimento.
- **Critério de Sucesso**: Conclusão em até 90 segundos com confirmação do ponto de referência comunitário.

### Tarefa T05: Visualização do Painel de Transparência e Exportação de Relatório Comunitário
- **Cenário**: O voluntário participará de audiência pública no bairro e deseja extrair um resumo dos últimos 30 dias de interrupções de água da sua região para apresentar à concessionária.
- **Instrução dada**: *"Acesse o Painel de Transparência, filtre os dados pelo seu município/bairro e localize a opção de gerar o Resumo Comunitário em PDF."*
- **Caminho ideal**: Menu Principal -> 'Painel de Transparência' (TEL-05) -> Seleção de filtro territorial -> Visualização de gráficos de horas de desabastecimento -> Clique em 'Baixar Resumo em PDF'.
- **Critério de Sucesso**: Conclusão em até 100 segundos com visualização da prévia do documento.

### Tarefa T06: Ativação de Recursos de Acessibilidade (Alto Contraste e Aumento de Fonte)
- **Cenário**: O usuário possui baixa visão ou está em ambiente ensolarado e necessita de contraste reforçado e tipografia ampliada para ler as informações.
- **Instrução dada**: *"Acesse as configurações do aplicativo e ative o 'Modo Alto Contraste' e aumente o tamanho da letra do sistema."*
- **Caminho ideal**: Tela Inicial ou Menu -> Ícone de Acessibilidade no topo -> Alternar chave 'Alto Contraste' -> Deslizar seletor de fonte para '+200%' -> Validar adaptação instantânea da tela.
- **Critério de Sucesso**: Conclusão em até 45 segundos, confirmando verbalmente que a leitura dos textos ficou mais confortável.

---

## 5. Indicadores e Métricas de Usabilidade Coletadas

Para cada par (Participante x Tarefa), foram aferidas quatro métricas rigorosas:
1. **Taxa de Eficácia (Conclusão)**: Binário (S/N) — Se a tarefa foi realizada com sucesso sem intervenção direta do moderador.
2. **Eficiência Temporal (Duração)**: Tempo total em segundos desde a leitura da instrução até o alcance do estado final da tarefa.
3. **Frequência de Erros e Desvios**: Quantidade de cliques errôneos, retornos de tela desnecessários ou dúvidas de navegação.
4. **Nível de Satisfação Subjetiva**: Escala Likert de 1 (Muito Difícil/Insatisfeito) a 5 (Muito Fácil/Satisfeito) atribuída imediatamente após a conclusão da tarefa.
5. **Escore SUS Consolidado**: Questionário padronizado de 10 perguntas aplicado ao encerramento da bateria de testes.
