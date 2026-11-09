# Comparativo Detalhado: Protótipo Versão 1.0 vs. Versão 2.0 Revisada: ÁguaViva PB

## 1. Contexto da Evolução do Protótipo
Após a conclusão dos testes com usuários (N = 6, 36 tarefas executadas), as observações qualitativas e os pontos de atrito registrados orientaram ajustes ergonômicos em telas centrais da aplicação **ÁguaViva PB**, resultando na **Versão 2.0 Revisada**.

## 2. Quadro Comparativo por Componente de Interface

| Componente / Tela | Versão Inicial (v1.0) | Versão 2.0 Revisada (Pós-Testes) | Justificativa Ergonômica & Normativa |
|---|---|---|---|
| **Tela de Denúncia (TEL-02 e TEL-03)** | Botão "Enviar Relato" posicionado no rodapé da página longa; exigia rolagem manual em telas menores. | Botão "Enviar Relato" fixo em barra inferior (*sticky bottom action bar*), com sombra de destaque e alto contraste. | Elimina a oclusão provocada pela abertura do teclado virtual no smartphone; evita abandonos de formulário observados no teste com o participante P3. |
| **Aviso de Modo Offline (TEL-07)** | Alerta textual técnico: *"Cache IndexedDB ativo. Sincronização pendente via API REST"*. | Card com ícone de nuvem: *"Tudo salvo no celular! Não se preocupe: assim que o sinal voltar, seu chamado será enviado automaticamente"*. | Atendimento à Heurística de Nielsen nº 2 (*Correspondência com o mundo real*), esclarecendo o estado da solicitação sem exigir conhecimento técnico do usuário. |
| **Mapa de Potabilidade e Desabastecimento (TEL-04)** | Navegação cartográfica controlada exclusivamente pelo gesto *pinch-to-zoom* (pinça na tela). | Adição de botões flutuantes grandes de zoom (+ / -) e recentralização no canto inferior direito com área de clique de 48 × 48 px. | Atende ao critério de sucesso WCAG 2.5.5 (*Target Size*), assegurando acessibilidade motora para idosos e aparelhos com telas de baixa sensibilidade tátil. |
| **Painel de Transparência Cívica (TEL-05)** | Legendas dos gráficos estatísticos em fonte de 10 px com escala monocromática suave. | Legendas ampliadas para 13 px em negrito com paleta de alto contraste (> 4.5:1) e ícones semânticos de apoio visual. | Facilita a consulta visual de dados em ambientes sob luz solar direta e apoia usuários com acuidade visual reduzida (WCAG 1.4.3). |
| **Feedback de Sincronização em Segundo Plano (TEL-07)** | Notificação estritamente visual na barra superior do navegador móvel. | Disparo de feedback háptico (vibração curta de 100 ms) acompanhado de sinalização visual verde de confirmação. | Confirmação multissensorial; atende a demanda levantada pela participante P1, permitindo guardar o aparelho no bolso enquanto aguarda área de cobertura. |

## 3. Impacto Ergonômico Mensurado
As alterações da Versão 2.0 responderam aos 4 pontos de atrito mapeados nos testes empíricos, sustentando a taxa de eficácia de 97,2% e o índice SUS de aceitabilidade em 84,2 pontos (Classificação Excelente / Grade A).

Para mais detalhes sobre as métricas e matriz de priorização, consulte o [Plano de Testes](file:///home/campos/Documents/Projetos/Projeto_Integrador/06_testes/plano_testes.md), a [Matriz de Melhorias](file:///home/campos/Documents/Projetos/Projeto_Integrador/06_testes/melhorias.md) e o [Dossiê de Testes](file:///home/campos/Documents/Projetos/Projeto_Integrador/06_testes/dossie_testes.md).
