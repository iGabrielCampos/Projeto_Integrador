---
id: experimento-ia-04-gustavo-antonio
etapa: 3
autor: Gustavo Antonio
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F027
  - F051
---

# Registro de Experimento Prático com IA – EXP-04: Conformidade Regulatória sob a LGPD e Cláusulas de Privacidade

- **Identificador do Experimento:** EXP-04
- **Integrante Responsável:** Gustavo Antonio
- **Função Principal:** Segurança da Informação
- **Data da Execução:** 2026-11-06
- **Ferramenta Utilizada:** Microsoft Copilot (GPT-4) / Modo Criativo

---

## 1. Objetivo Específico do Experimento
Avaliar se a IA redige uma cláusula de consentimento e retenção de dados pessoais para um protótipo de aplicativo web em conformidade com as exigências formais da Lei Geral de Proteção de Dados (LGPD - Lei nº 13.709/2018 `[F001]`), checando se ela atende aos princípios de finalidade, adequação e transparência ou se sugere autorizações genéricas e abusivas.

---

## 2. Prompt Exato Utilizado (Entrada)
```text
Atue como um especialista em segurança e privacidade digital. Elabore uma cláusula de consentimento para coleta e tratamento de dados pessoais (nome, e-mail e localização aproximada) de usuários que irão testar um protótipo acadêmico de solução socioambiental. A cláusula deve cumprir rigorosamente a LGPD (Lei 13.709/2018), explicitando a finalidade, tempo de retenção, ausência de repasse a terceiros e canal para revogação do consentimento.
```

---

## 3. Resposta Gerada pelo Modelo (Síntese e Trecho Central)
O modelo gerou um termo de consentimento com seções identificadas:
1. *Controlador dos Dados:* Identificação dos pesquisadores acadêmicos.
2. *Dados Coletados e Finalidade Específica:* Uso exclusivo para análise de usabilidade no Projeto Integrador.
3. *Tempo de Guarda e Eliminação:* Retenção até o encerramento do semestre letivo (dezembro/2026) e eliminação definitiva após a apresentação.
4. *Canal de Direitos do Titular:* Disponibilização de e-mail institucional para solicitação de exclusão ou revogação imediata.

```text
"Ao marcar esta opção, você autoriza expressamente os pesquisadores do Projeto Integrador a coletar e tratar seu nome, e-mail e cidade de acesso, nos termos do art. 7º, inciso I da Lei 13.709/2018 (LGPD). Os dados serão utilizados exclusivamente para comprovação acadêmica das sessões de usabilidade, não serão comercializados ou compartilhados com terceiros e serão eliminados de nossos repositórios em até 30 dias após a conclusão da disciplina. Você poderá revogar este consentimento a qualquer momento enviando solicitação para o e-mail informado..."
```

---

## 4. Avaliação Crítica Humana da Resposta
- **Precisão Técnica:** Elevada. O modelo identificou corretamente a base legal do consentimento (art. 7º, I da LGPD `[F001]`) e seguiu o art. 8º, § 4º da lei, que proíbe o consentimento genérico para finalidades indeterminadas.
- **Clareza e Didática:** Linguagem acessível, evitando juridiquês excessivo (*legal design* / linguagem simples).
- **Profundidade:** Bom detalhamento dos direitos do titular (art. 18 da LGPD).

---

## 5. Vieses, Alucinações e Limitações Identificadas
- **Alucinação Potencial de Responsabilidade:** O modelo sugeriu incluir um parágrafo isentando os pesquisadores de qualquer responsabilidade por eventuais vazamentos ocorridos por motivos de força maior. Essa cláusula de exoneração é nula de pleno direito sob a ótica da LGPD e do Código de Defesa do Consumidor `[F051]`.
- **Omissão da Figura do DPO / Encarregado:** Não especificou se em projetos acadêmicos universitários há necessidade de contato com o Encarregado de Proteção de Dados institucional (DPO do UNIPÊ).

---

## 6. Procedimento de Verificação Humana (Fact-Checking)
1. O texto gerado foi comparado diretamente com a redação dos artigos 6º (Princípios), 7º (Bases Legais), 8º (Consentimento) e 18 (Direitos do Titular) da Lei nº 13.709/2018 `[F001]`.
2. Foi suprimida a cláusula de isenção de responsabilidade abusiva.
3. Inseriu-se a garantia explícita de anonimização (pseudônimos P1 a P6), alinhando o termo com o nosso modelo oficial [`apendices/termos/tcle_modelo.md`](../../apendices/termos/tcle_modelo.md).

---

## 7. Conclusão e Lição Aprendida
A IA redige minutas contratuais e termos regulatórios com rapidez, mas tende a importar vícios de contratos comerciais convencionais (como isenções unilaterais de responsabilidade). **O analista humano deve expurgar cláusulas abusivas** para manter a integridade ética e legal do projeto.
