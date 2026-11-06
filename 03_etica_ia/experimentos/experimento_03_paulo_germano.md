---
id: experimento-ia-03-paulo-germano
etapa: 3
autor: Paulo Germano
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F020
  - F021
---

# Registro de Experimento Prático com IA – EXP-03: Análise Estatística de Dados e Detecção de Alucinações Numéricas

- **Identificador do Experimento:** EXP-03
- **Integrante Responsável:** Paulo Germano
- **Função Principal:** Dados e Inteligência Artificial
- **Data da Execução:** 2026-11-06
- **Ferramenta Utilizada:** Google Gemini 1.5 Pro (Interface Web Oficial)

---

## 1. Objetivo Específico do Experimento
Verificar a acurácia de um modelo de linguagem em realizar cálculos estatísticos descritivos (média, desvio padrão, percentuais e detecção de assimetria) sobre um conjunto de dados brutos fornecido no prompt, comparando a saída da IA com cálculos matemáticos exatos executados em Python via biblioteca `pandas` e `scipy`.

---

## 2. Prompt Exato Utilizado (Entrada)
```text
Dado o seguinte conjunto de idades de 15 candidatos inscritos em uma vaga de TI:
[21, 23, 24, 25, 25, 26, 27, 28, 29, 31, 33, 35, 42, 48, 56]
Calcule:
1) A média aritmética;
2) A mediana;
3) O desvio padrão amostral;
4) O percentual de candidatos com idade igual ou superior a 30 anos.
Apresente os passos do cálculo e informe se a distribuição apresenta assimetria positiva ou negativa.
```

---

## 3. Resposta Gerada pelo Modelo (Síntese e Trecho Central)
O modelo apresentou a resolução passo a passo:
- Soma total: 498. Média: `498 / 15 = 33,2 anos`. (Nota: erro de soma!)
- Mediana: 8º elemento ordenado = `28 anos`.
- Desvio padrão amostral calculado pelo modelo: `10,48 anos`.
- Percentual ≥ 30 anos: 6 candidatos (31, 33, 35, 42, 48, 56) em 15 = `40,0%`.
- Classificação: Assimetria positiva (à direita), pois a média calculada foi maior que a mediana.

---

## 4. Avaliação Crítica Humana da Resposta
- **Precisão Técnica:** Parcialmente falha. O modelo cometeu um erro aritmético elementar na soma dos valores do vetor.
  - A soma real dos 15 valores é: `21+23+24+25+25+26+27+28+29+31+33+35+42+48+56 = 442`.
  - A média real é `442 / 15 = 29,47 anos`, e **não 33,2 anos** como alucinado pelo modelo!
  - O desvio padrão amostral real é `9,91 anos`, e não `10,48`.
- **Clareza e Didática:** Excelente explicação teórica dos conceitos de mediana e assimetria, com redação didática.
- **Identificação da Assimetria:** A conclusão qualitativa de assimetria positiva permaneceu correta (pois `Média (29,47) > Mediana (28)`), mas os números que embasaram o cálculo estavam incorretos.

---

## 5. Vieses, Alucinações e Limitações Identificadas
- **Alucinação Aritmética (LLMs como Calculadoras):** Modelos de linguagem baseados em predição de tokens não são motores de cálculo determinístico. Eles tentam "adivinhar" o resultado de somas longas com base em padrões textuais em vez de executar operações na CPU.
- **Falsa Sensação de Certeza:** O modelo apresentou os valores com duas casas decimais com tom de autoridade irretocável, o que induziria um analista desatento a incorporar números falsos em um relatório executivo ou científico.

---

## 6. Procedimento de Verificação Humana (Fact-Checking)
1. Escreveu-se um script em Python utilizando `numpy`:
   ```python
   import numpy as np
   dados = [21, 23, 24, 25, 25, 26, 27, 28, 29, 31, 33, 35, 42, 48, 56]
   print("Soma:", sum(dados)) # 442
   print("Media:", np.mean(dados)) # 29.4666...
   print("Mediana:", np.median(dados)) # 28.0
   print("Std Amostral:", np.std(dados, ddof=1)) # 9.9129...
   ```
2. Confirmou-se a divergência de quase 4 anos na média etária gerada pelo modelo.

---

## 7. Conclusão e Lição Aprendida
**Jamais delegar cálculos matemáticos ou contagens estatísticas a LLMs puros**. Para análise de dados, a IA deve ser empregada para redigir o código Python/SQL que executará o cálculo no interpretador, e nunca para executar o cálculo mentalmente em seu espaço latente.
