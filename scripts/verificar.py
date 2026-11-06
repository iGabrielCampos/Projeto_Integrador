#!/usr/bin/env python3
"""
scripts/verificar.py
Verificador determinístico de conformidade, integridade e consistência do Projeto Integrador.
Uso: python scripts/verificar.py  (a partir da raiz do projeto)
"""

from pathlib import Path
import csv
import json
import re
import sys
import importlib.util

ROOT = Path(__file__).resolve().parent.parent

REQUIRED = [
    "00_gestao/estado_projeto.json",
    "00_gestao/fontes.md",
    "00_gestao/matriz_conformidade.md",
    "01_mercado/vagas_brutas.csv",
    "01_mercado/dossie_mercado.md",
    "02_carreira/dossie_carreira.md",
    "03_etica_ia/dossie_etica.md",
    "04_problema/dossie_problema.md",
    "05_solucao/dossie_solucao.md",
    "06_testes/dossie_testes.md",
    "06_testes/registros_anonimizados.csv",
    "07_relatorio/relatorio_final.md",
]

def check_structure() -> None:
    print("--- 1. Verificação de Estrutura de Arquivos Obrigatórios ---")
    for rel in REQUIRED:
        p = ROOT / rel
        print(("[OK] " if p.exists() else "[PENDENTE] ") + rel)

def check_state() -> None:
    print("\n--- 2. Verificação de Estado do Projeto (estado_projeto.json) ---")
    p = ROOT / "00_gestao/estado_projeto.json"
    if not p.exists():
        print("[!!] estado_projeto.json inexistente")
        return
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
        etapa = data.get("etapa_atual", "N/A")
        status = data.get("status_geral", "N/A")
        print(f"[OK] estado_projeto.json válido (Etapa atual: {etapa} - {status})")
    except json.JSONDecodeError as exc:
        print(f"[!!] estado_projeto.json inválido: {exc}")

def md_files():
    skip_dirs = {"templates", "subagentes", "build", "apendices", ".git"}
    # Foca nos diretórios operacionais do projeto
    target_prefixes = ("00_", "01_", "02_", "03_", "04_", "05_", "06_", "07_")
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT)
        if skip_dirs & set(rel.parts):
            continue
        if len(rel.parts) > 1 and rel.parts[0].startswith(target_prefixes):
            yield p

def check_placeholders() -> None:
    print("\n--- 3. Verificação de Campos em Aberto ([...] ou TODO) ---")
    encontrou = False
    for p in md_files():
        text = p.read_text(encoding="utf-8", errors="ignore")
        hits = re.findall(r"\[\.\.\.\]|\bTODO\b", text)
        if hits:
            encontrou = True
            print(f"[!!] {p.relative_to(ROOT)} — {len(hits)} campo(s) em aberto")
    if not encontrou:
        print("[OK] Nenhum campo pendente ([...] ou TODO) nos documentos vigentes")

def check_sources() -> None:
    print("\n--- 4. Verificação de Rastreabilidade de Fontes ([Fxxx]) ---")
    fontes = ROOT / "00_gestao/fontes.md"
    if not fontes.exists():
        print("[!!] 00_gestao/fontes.md inexistente")
        return
    defined = set(re.findall(r"\[(F\d{3})\]", fontes.read_text(encoding="utf-8")))
    print(f"[INFO] {len(defined)} fonte(s) formalmente catalogada(s) em fontes.md")
    encontrou_inconsistencia = False
    for p in md_files():
        if p == fontes:
            continue
        used = set(re.findall(r"\[(F\d{3})\]", p.read_text(encoding="utf-8")))
        missing = used - defined
        if missing:
            encontrou_inconsistencia = True
            print(f"[!!] {p.relative_to(ROOT)} — fontes inexistentes: {sorted(missing)}")
    if not encontrou_inconsistencia:
        print("[OK] Todas as citações [Fxxx] apontam para fontes registradas")

def count_rows() -> None:
    print("\n--- 5. Verificação de Bases de Dados e Quantitativos Mínimos ---")
    # Checagem de vagas (Etapa 1)
    csv_vagas = ROOT / "01_mercado/vagas_brutas.csv"
    if csv_vagas.exists():
        linhas = sum(1 for _ in csv_vagas.open(encoding="utf-8")) - 1
        print(("[OK] " if linhas >= 20 else "[!!] ") + f"vagas em 01_mercado/vagas_brutas.csv: {linhas} (mín. 20)")
    else:
        print("[PENDENTE] 01_mercado/vagas_brutas.csv (Etapa 1 não iniciada)")

    # Checagem de registros e participantes de teste (Etapa 6)
    csv_testes = ROOT / "06_testes/registros_anonimizados.csv"
    if csv_testes.exists():
        with csv_testes.open(encoding="utf-8", newline="") as f:
            registros = list(csv.DictReader(f))
        participantes = len({r["participante_id"] for r in registros})
        label = f"registros de teste: {len(registros)} | participantes únicos: {participantes} (mín. 6)"
        print(("[OK] " if participantes >= 6 else "[!!] ") + label)
    else:
        print("[PENDENTE] 06_testes/registros_anonimizados.csv (Etapa 6 não iniciada)")

def run_plugged_rules() -> None:
    regras_dir = ROOT / "scripts/regras"
    if not regras_dir.exists():
        return
    scripts = sorted(regras_dir.glob("regra_*.py"))
    if scripts:
        print("\n--- 6. Execução de Regras Plugáveis (scripts/regras/) ---")
        for s in scripts:
            try:
                spec = importlib.util.spec_from_file_location(s.stem, s)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                if hasattr(mod, "verificar"):
                    mod.verificar(ROOT)
            except Exception as e:
                print(f"[!!] Erro ao executar regra {s.name}: {e}")

if __name__ == "__main__":
    for check in (check_structure, check_state, check_placeholders, check_sources, count_rows, run_plugged_rules):
        check()
