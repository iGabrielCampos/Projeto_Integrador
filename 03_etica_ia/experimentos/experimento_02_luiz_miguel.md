---
id: experimento-ia-02-luiz-miguel
etapa: 3
autor: Luiz Miguel
data: 2026-11-06
status: entregavel-concluido
fontes:
  - F020
  - F026
---

# Registro de Experimento Prático com IA – EXP-02: Automação de Infraestrutura e Regras de Firewall

- **Identificador do Experimento:** EXP-02
- **Integrante Responsável:** Luiz Miguel
- **Função Principal:** Infraestrutura e Redes
- **Data da Execução:** 2026-11-06
- **Ferramenta Utilizada:** Claude 3.5 Sonnet (Anthropic) / Interface Web

---

## 1. Objetivo Específico do Experimento
Avaliar se a IA é capaz de gerar um script em Bash para configurar um firewall básico via `iptables` em um servidor Linux (Ubuntu), analisando se ela adota o princípio do menor privilégio (Default Deny) ou se comete o erro clássico de deixar portas críticas abertas inadvertidamente.

---

## 2. Prompt Exato Utilizado (Entrada)
```text
Crie um script em Shell Script (Bash) para configurar o firewall iptables em um servidor Ubuntu 22.04 que atuará como servidor web seguro. O script deve permitir acesso SSH e tráfego web HTTP e HTTPS, bloqueando todo o restante do tráfego de entrada. Inclua explicações e medidas para evitar que eu perca o acesso remoto à máquina durante a execução.
```

---

## 3. Resposta Gerada pelo Modelo (Síntese e Trecho Central)
O modelo gerou um script Bash completo com políticas padrão de descarte (`DROP`), liberação de loopback e conexões já estabelecidas, além de recomendar a alteração da porta padrão do SSH:

```bash
#!/bin/bash
set -e

echo "[*] Limpando regras anteriores..."
iptables -F
iptables -X
iptables -t nat -F
iptables -t mangle -F

echo "[*] Definindo politicas padrao como DROP..."
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

echo "[*] Permitindo loopback e conexoes estabelecidas..."
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

echo "[*] Permitindo SSH (porta padrao 22)..."
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

echo "[*] Permitindo Web (HTTP 80 e HTTPS 443)..."
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

echo "[+] Firewall configurado com sucesso!"
```

---

## 4. Avaliação Crítica Humana da Resposta
- **Precisão Técnica:** Muito alta. O script seguiu a melhor prática de segurança perimétrica: `INPUT DROP` associado à liberação de conexões `ESTABLISHED,RELATED`, garantindo que respostas de requisições originadas pelo próprio servidor não sejam bloqueadas.
- **Clareza e Didática:** Instruções passo a passo bem comentadas e aviso explícito sobre o risco de bloqueio acidental.
- **Profundidade:** O modelo recomendou o pacote `iptables-persistent` para manter as regras após a reinicialização da máquina.

---

## 5. Vieses, Alucinações e Limitações Identificadas
- **Risco Operacional Crítico na Ordem dos Comandos:** O script executa `iptables -P INPUT DROP` antes de adicionar a regra de liberação da porta 22 (`SSH`). Em uma conexão SSH remota em tempo real sem buffer, se o script falhar ou for executado comando por comando manualmente no terminal, o administrador é **imediatamente desconectado e perde o acesso à máquina**.
- **Omissão de Prevenção contra Ataques de Negação de Serviço (DoS):** Não incluiu limitadores de taxa de conexões novas (`hashlimit` ou `recent`) para mitigar SYN Flood em HTTP/HTTPS.

---

## 6. Procedimento de Verificação Humana (Fact-Checking)
1. O script foi executado em uma máquina virtual isolada Ubuntu Server 22.04 no VirtualBox.
2. Confirmou-se que a regra `iptables -P INPUT DROP` aplicada antes da porta 22 em sessões interativas derrubou a sessão SSH quando não executada dentro de um script empacotado.
3. Foi necessário inverter a ordem dos comandos: primeiro liberar a porta 22 e a interface de loopback, e **somente ao final** alterar a política padrão para `DROP`.

---

## 7. Conclusão e Lição Aprendida
Scripts de automação gerados por IA exigem verificação meticulosa da **ordem de execução** em ambientes de infraestrutura. Um erro de precedência de comandos pode provocar indisponibilidade total do servidor remoto sem possibilidade de recuperação externa.
