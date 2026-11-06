import json
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(".")
vagas_file = ROOT / "01_mercado/vagas_brutas.json"

with open(vagas_file, encoding="utf-8") as f:
    vagas = json.load(f)

# 1. Normalização de competências
# Mapeamento: Termo Bruto -> Termo Padronizado, Categoria
norm_map = {
    # Técnicas - Dev
    "git": ("Git / GitHub", "Técnica"),
    "github": ("Git / GitHub", "Técnica"),
    "javascript": ("JavaScript", "Técnica"),
    "typescript": ("TypeScript", "Técnica"),
    "node.js": ("Node.js", "Técnica"),
    "react": ("React", "Técnica"),
    "angular": ("Angular", "Técnica"),
    "c#": ("C# / .NET", "Técnica"),
    ".net core": ("C# / .NET", "Técnica"),
    "asp.net": ("C# / .NET", "Técnica"),
    "php moderno": ("PHP", "Técnica"),
    "laravel": ("Laravel", "Técnica"),
    "java": ("Java / Spring Boot", "Técnica"),
    "spring boot": ("Java / Spring Boot", "Técnica"),
    "apis restful": ("APIs RESTful", "Técnica"),
    "consumo de apis": ("APIs RESTful", "Técnica"),
    "lógica de programação": ("Lógica e Algoritmos", "Técnica"),
    "algoritmos e estruturas de dados": ("Lógica e Algoritmos", "Técnica"),

    # Técnicas - Infra / Cloud
    "windows server": ("Windows Server / AD", "Técnica"),
    "active directory": ("Windows Server / AD", "Técnica"),
    "linux": ("Linux (Ubuntu/Debian)", "Técnica"),
    "administração linux": ("Linux (Ubuntu/Debian)", "Técnica"),
    "tcp/ip": ("Redes e Protocolos TCP/IP", "Técnica"),
    "roteamento e switching": ("Roteamento e Switching", "Técnica"),
    "dns, dhcp, vpn": ("Serviços de Rede (DNS/DHCP/VPN)", "Técnica"),
    "zabbix": ("Monitoramento (Zabbix/Grafana)", "Técnica"),
    "cloudwatch/grafana": ("Monitoramento (Zabbix/Grafana)", "Técnica"),
    "virtualização": ("Virtualização (VMware/Proxmox)", "Técnica"),
    "cloud computing": ("Cloud Computing (AWS/Azure)", "Técnica"),
    "nuvem": ("Cloud Computing (AWS/Azure)", "Técnica"),
    "microsoft entra id": ("Microsoft Entra ID / M365", "Técnica"),
    "backup": ("Rotinas de Backup e Uptime", "Técnica"),

    # Técnicas - Dados / IA
    "sql": ("SQL (Postgres/SQL Server/MySQL)", "Técnica"),
    "power bi": ("Power BI / Data Viz", "Técnica"),
    "tableau": ("Power BI / Data Viz", "Técnica"),
    "python": ("Python", "Técnica"),
    "modelagem": ("Modelagem de Dados Relacional/Dimensional", "Técnica"),
    "etl": ("Pipelines ETL / Fluxo de Dados", "Técnica"),
    "modelos de linguagem": ("IA Generativa e LLMs", "Técnica"),
    "prompt engineering": ("IA Generativa e LLMs", "Técnica"),

    # Técnicas - Segurança
    "gestão de identidade e acesso": ("IAM (Gestão de Identidade e Acesso)", "Técnica"),
    "iam": ("IAM (Gestão de Identidade e Acesso)", "Técnica"),
    "siem": ("SIEM e Análise de Logs", "Técnica"),
    "logs de segurança": ("SIEM e Análise de Logs", "Técnica"),
    "vulnerabilidades": ("Gestão de Vulnerabilidades", "Técnica"),
    "firewalls": ("Firewalls de Borda e Perímetro", "Técnica"),
    "edr/xdr": ("EDR/XDR e Endpoint Security", "Técnica"),
    "lgpd": ("LGPD e Privacidade por Padrão", "Técnica"),
    "owasp": ("Segurança de Aplicações (OWASP)", "Técnica"),

    # Comportamentais
    "comunicação": ("Comunicação Clara e Transparente", "Comportamental"),
    "comunicação verbal": ("Comunicação Clara e Transparente", "Comportamental"),
    "trabalho em equipe": ("Trabalho em Equipe e Cooperação", "Comportamental"),
    "espírito colaborativo": ("Trabalho em Equipe e Cooperação", "Comportamental"),
    "proatividade": ("Proatividade e Iniciativa", "Comportamental"),
    "vontade de aprender": ("Aprendizado Contínuo (Growth Mindset)", "Comportamental"),
    "curiosidade intelectual": ("Aprendizado Contínuo (Growth Mindset)", "Comportamental"),
    "resolução de problemas": ("Resolução de Problemas Complexos", "Comportamental"),
    "organização": ("Organização Operacional e Disciplina", "Comportamental"),
    "atenção a detalhes": ("Atenção Rigorosa a Detalhes", "Comportamental"),
    "ética": ("Postura Ética e Sigilo Profissional", "Comportamental"),
    "resiliência": ("Resiliência e Adaptabilidade", "Comportamental")
}

# 2. Contagem de frequência por função
# Funções canônicas:
funcoes = [
    "Desenvolvimento de Software",
    "Infraestrutura e Redes",
    "Dados e IA",
    "Segurança da Informação"
]

freq = defaultdict(lambda: {f: 0 for f in funcoes})
categoria_comp = {}

for v in vagas:
    f_vaga = v["funcao"]
    txt = (v["requisitos_tecnicos"] + " " + v["requisitos_comportamentais"]).lower()
    
    # Checar cada termo mapeado
    achados_nesta_vaga = set()
    for raw_term, (canon_term, cat) in norm_map.items():
        if raw_term in txt:
            achados_nesta_vaga.add((canon_term, cat))
            
    for canon_term, cat in achados_nesta_vaga:
        freq[canon_term][f_vaga] += 1
        categoria_comp[canon_term] = cat

# 3. Gerar CSV de Competências Padronizadas
padronizadas_rows = []
for raw, (canon, cat) in sorted(norm_map.items()):
    padronizadas_rows.append({
        "Termo_Bruto": raw,
        "Competencia_Padronizada": canon,
        "Categoria": cat
    })

with open(ROOT / "01_mercado/planilha_Competencias_Padronizadas.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Termo_Bruto", "Competencia_Padronizada", "Categoria"])
    writer.writeheader()
    writer.writerows(padronizadas_rows)

# 4. Gerar CSV de Frequência por Função
freq_rows = []
for comp, counts in sorted(freq.items(), key=lambda x: sum(x[1].values()), reverse=True):
    total = sum(counts.values())
    pct_total = round((total / len(vagas)) * 100, 1)
    row = {
        "Competencia": comp,
        "Categoria": categoria_comp.get(comp, "Geral"),
        "Dev_Software_Qtd": counts["Desenvolvimento de Software"],
        "Dev_Software_Pct": f"{round((counts['Desenvolvimento de Software']/6)*100, 1)}%",
        "Infra_Redes_Qtd": counts["Infraestrutura e Redes"],
        "Infra_Redes_Pct": f"{round((counts['Infraestrutura e Redes']/6)*100, 1)}%",
        "Dados_IA_Qtd": counts["Dados e IA"],
        "Dados_IA_Pct": f"{round((counts['Dados e IA']/6)*100, 1)}%",
        "Seguranca_Qtd": counts["Segurança da Informação"],
        "Seguranca_Pct": f"{round((counts['Segurança da Informação']/6)*100, 1)}%",
        "Total_Absoluto": total,
        "Frequencia_Geral_Pct": f"{pct_total}%"
    }
    freq_rows.append(row)

with open(ROOT / "01_mercado/planilha_Frequencia_por_Funcao.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = [
        "Competencia", "Categoria",
        "Dev_Software_Qtd", "Dev_Software_Pct",
        "Infra_Redes_Qtd", "Infra_Redes_Pct",
        "Dados_IA_Qtd", "Dados_IA_Pct",
        "Seguranca_Qtd", "Seguranca_Pct",
        "Total_Absoluto", "Frequencia_Geral_Pct"
    ]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(freq_rows)

# 5. Desafios dos Contratantes
desafios = [
    {
        "ID_Desafio": "DES-01",
        "Tema": "Exigência de Experiência Prática em Vagas de Entrada",
        "Descricao": "Anúncios para nível Júnior frequentemente exigem domínio prévio de múltiplos frameworks, padrões de arquitetura e ferramentas avançadas que historicamente pertenciam a níveis Plenos.",
        "Vagas_Evidencia": "VAG-001, VAG-002, VAG-004, VAG-010, VAG-019",
        "Frequencia_Absoluta": 5,
        "Impacto_na_Carreira": "Cria barreiras de acesso para formandos, exigindo compensação obrigatória via portfólio no GitHub com projetos reais e aplicados."
    },
    {
        "ID_Desafio": "DES-02",
        "Tema": "Demanda Crítica por Comunicação Assíncrona e Autogestão no Trabalho Remoto",
        "Descricao": "Com a prevalência de contratos remotos, a capacidade de expressar ideias com precisão em textos, documentar rotinas e manter disciplina sem supervisão direta tornou-se pré-requisito eliminatório.",
        "Vagas_Evidencia": "VAG-001, VAG-004, VAG-009, VAG-010, VAG-014, VAG-020",
        "Frequencia_Absoluta": 6,
        "Impacto_na_Carreira": "Exige dos estudantes desenvolvimento socioemocional precoce para atuação em squads distribuídas geograficamente."
    },
    {
        "ID_Desafio": "DES-03",
        "Tema": "Conformidade Regulatória (LGPD) e Postura Preventiva em Segurança",
        "Descricao": "A preocupação com vazamentos e responsabilidade legal faz com que vagas de Infraestrutura, Dados e Segurança exijam noções de privacidade, segregação de privilégios e auditoria de acessos.",
        "Vagas_Evidencia": "VAG-019, VAG-021, VAG-023, VAG-024",
        "Frequencia_Absoluta": 4,
        "Impacto_na_Carreira": "O conhecimento em LGPD deixa de ser atributo jurídico e passa a ser requisito de projeto de software e gestão de dados."
    },
    {
        "ID_Desafio": "DES-04",
        "Tema": "Adoção Emergente de IA Generativa e Automação de Processos",
        "Descricao": "Início da formalização de requisitos envolvendo uso de APIs de LLMs, engenharia de prompts e ferramentas de apoio à codificação (Copilot/LangChain) já nos primeiros estágios da carreira.",
        "Vagas_Evidencia": "VAG-006, VAG-016",
        "Frequencia_Absoluta": 2,
        "Impacto_na_Carreira": "Alunos que incorporam IA responsável em seus fluxos de estudo ganham vantagem competitiva destacada."
    },
    {
        "ID_Desafio": "DES-05",
        "Tema": "Multidisciplinaridade e Hibridismo de Competências (Dev + Cloud + Data)",
        "Descricao": "Desenvolvedores precisam entender de bancos em nuvem e Docker; analistas de dados precisam programar em Python; analistas de segurança precisam de scripts em PowerShell/Python.",
        "Vagas_Evidencia": "VAG-001, VAG-010, VAG-013, VAG-015, VAG-023",
        "Frequencia_Absoluta": 5,
        "Impacto_na_Carreira": "Fim do profissional isolado: o mercado busca o perfil em 'T' (profundo em uma área, versátil nas interfaces vizinhas)."
    }
]

with open(ROOT / "01_mercado/planilha_Desafios_Contratantes.csv", "w", encoding="utf-8", newline="") as f:
    fieldnames = ["ID_Desafio", "Tema", "Descricao", "Vagas_Evidencia", "Frequencia_Absoluta", "Impacto_na_Carreira"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(desafios)

print("Planilhas analíticas processadas e salvas com sucesso em 01_mercado/!")
