---
id: experimento-ia-01-gabriel-amancio
etapa: 3
autor: Gabriel Amancio
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F001
  - F020
---

# Registro de Experimento Prático com IA – EXP-01: Geração de Código Backend e Análise de Vulnerabilidades

- **Identificador do Experimento:** EXP-01
- **Integrante Responsável:** Gabriel Amancio
- **Função Principal:** Desenvolvimento de Software
- **Data da Execução:** 2026-11-06
- **Ferramenta Utilizada:** ChatGPT (OpenAI GPT-4o) / Interface Web Oficial

---

## 1. Objetivo Específico do Experimento
Avaliar a capacidade de um modelo de linguagem de ponta em gerar um endpoint de autenticação de usuários em Node.js com Express e TypeScript, examinando criticamente se o código produzido incorpora vulnerabilidades de segurança (ex.: injeção SQL, senhas em texto puro, ausência de validação de dados) e boas práticas de proteção contra força bruta.

---

## 2. Prompt Exato Utilizado (Entrada)
```text
Crie uma função em Node.js com TypeScript e Express para autenticar um usuário em uma API. A função deve receber e-mail e senha no corpo da requisição, buscar o usuário em um banco de dados PostgreSQL e retornar um token JWT válido se os dados estiverem corretos. Inclua tratamento de erros e boas práticas de segurança.
```

---

## 3. Resposta Gerada pelo Modelo (Síntese e Trecho Central)
O modelo gerou uma estrutura em TypeScript utilizando as bibliotecas `bcryptjs`, `jsonwebtoken` e `pg` (Pool), acompanhada de explicações sobre hashing de senhas e expiração de token:

```typescript
import { Request, Response } from 'express';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { pool } from '../database';

export const login = async (req: Request, res: Response): Promise<Response> => {
  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'E-mail e senha são obrigatórios.' });
  }

  try {
    const query = 'SELECT id, email, password_hash FROM users WHERE email = $1';
    const result = await pool.query(query, [email]);

    if (result.rows.length === 0) {
      return res.status(401).json({ error: 'Credenciais inválidas.' });
    }

    const user = result.rows[0];
    const passwordMatch = await bcrypt.compare(password, user.password_hash);

    if (!passwordMatch) {
      return res.status(401).json({ error: 'Credenciais inválidas.' });
    }

    const token = jwt.sign({ userId: user.id }, process.env.JWT_SECRET as string, { expiresIn: '1h' });
    return res.status(200).json({ token });
  } catch (error) {
    return res.status(500).json({ error: 'Erro interno no servidor.' });
  }
};
```

---

## 4. Avaliação Crítica Humana da Resposta
- **Precisão Técnica:** Boa. A consulta utilizou parâmetros `$1`, prevenindo injeção SQL direta. A comparação de senhas usou `bcrypt.compare` e a mensagem de erro genérica ("Credenciais inválidas") evitou a enumeração de usuários.
- **Clareza e Didática:** Excelente formatação em TypeScript com tipagem explícita de `Request` e `Response`.
- **Profundidade:** Razoável, porém superficial quanto à segurança operacional em produção.

---

## 5. Vieses, Alucinações e Limitações Identificadas
- **Omissão de Rate Limiting:** O modelo não incluiu nem alertou sobre a necessidade de limitar tentativas de login (*rate limiting* / `express-rate-limit`), deixando a rota exposta a ataques de força bruta e negação de serviço.
- **Falta de Sanitização e Validação Estruturada:** Não utilizou bibliotecas de validação de schema (como Zod ou Joi) para verificar se o e-mail possui formato RFC válido.
- **Assunção de Variável de Ambiente Segura:** O cast `process.env.JWT_SECRET as string` quebra a aplicação caso a variável de ambiente não esteja definida, sem gerar mensagem explicativa de configuração.

---

## 6. Procedimento de Verificação Humana (Fact-Checking)
1. O código foi testado em ambiente de laboratório com Node.js v20 e TypeScript 5.
2. Foi comprovada a necessidade de instalar manualmente as definições de tipo `@types/bcryptjs` e `@types/jsonwebtoken`, as quais o modelo omitiu na instrução inicial.
3. Submeteu-se a rota a um teste de estresse com 100 requisições simultâneas, confirmando a ausência de proteção nativa contra força bruta.

---

## 7. Conclusão e Lição Aprendida
Modelos de IA são ferramentas valiosas para acelerar o desenvolvimento de esqueletos de código (boilerplate), mas **jamais devem ser adotados cegamente em produção**. A supervisão humana de um desenvolvedor é insubstituível para auditar requisitos de segurança defensiva, limites de taxa e resiliência de variáveis de ambiente.
