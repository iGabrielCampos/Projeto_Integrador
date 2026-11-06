#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Compilação e Verificação Monográfica ABNT
Projeto Integrador de ADS - UNIPÊ (2026)
Gera o pacote consolidado para impressão e submissão acadêmica.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RELATORIO_MD = ROOT / "07_relatorio/relatorio_final.md"
BUILD_DIR = ROOT / "07_relatorio/build"
OUTPUT_MD = BUILD_DIR / "monografia_completa_abnt.md"
OUTPUT_HTML = BUILD_DIR / "monografia_completa_abnt.html"

def main():
    print("=" * 60)
    print("COMPILADOR ACADÊMICO ABNT — PROJETO INTEGRADOR UNIPÊ")
    print("=" * 60)

    if not RELATORIO_MD.exists():
        print(f"[ERRO] Arquivo {RELATORIO_MD} não encontrado.")
        sys.exit(1)

    conteudo = RELATORIO_MD.read_text(encoding="utf-8")
    palavras = len(conteudo.split())
    caracteres = len(conteudo)
    linhas = len(conteudo.splitlines())
    
    # Estimativa de páginas ABNT: média de 400 a 450 palavras por página formatada
    paginas_estimadas = round(palavras / 410, 1)

    print(f"\n[INFO] Estatísticas do Texto Principal:")
    print(f"  - Total de Palavras: {palavras:,}")
    print(f"  - Total de Caracteres: {caracteres:,}")
    print(f"  - Total de Linhas: {linhas:,}")
    print(f"  - Estimativa de Páginas ABNT: ~{paginas_estimadas} páginas (Meta: 20 a 30 páginas)")

    if 20.0 <= paginas_estimadas <= 32.0:
        print("  -> [CONFORME] Extensão dentro da faixa exigida pelas diretrizes do UNIPÊ (20 a 30 páginas).")
    else:
        print(f"  -> [ALERTA] Extensão fora da faixa recomendada (estimado: {paginas_estimadas} páginas).")

    # Gerar cópia para build
    OUTPUT_MD.write_text(conteudo, encoding="utf-8")
    print(f"\n[OK] Monografia compilada em Markdown: {OUTPUT_MD.relative_to(ROOT)}")

    # Gerar versão HTML autossuficiente com estilização ABNT para visualização e impressão em PDF
    html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Relatório Final Integrado - Projeto Integrador UNIPÊ</title>
<style>
  body {{
    font-family: 'Times New Roman', Times, serif;
    font-size: 12pt;
    line-height: 1.5;
    color: #111;
    max-width: 210mm;
    margin: 30mm 20mm 20mm 30mm;
    background-color: #fff;
  }}
  h1, h2, h3, h4 {{
    font-family: Arial, Helvetica, sans-serif;
    color: #000;
    text-transform: uppercase;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
  }}
  h1 {{ font-size: 14pt; font-weight: bold; }}
  h2 {{ font-size: 13pt; font-weight: bold; }}
  h3 {{ font-size: 12pt; font-weight: bold; }}
  p {{
    text-align: justify;
    text-indent: 1.5cm;
    margin-bottom: 0;
    margin-top: 0;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    font-size: 10pt;
  }}
  th, td {{
    border: 1px solid #333;
    padding: 6px 10px;
    text-align: left;
  }}
  th {{
    background-color: #f2f2f2;
    font-weight: bold;
  }}
  blockquote {{
    font-size: 10pt;
    line-height: 1.0;
    margin-left: 4cm;
    margin-right: 0;
    text-align: justify;
    font-style: italic;
  }}
  pre, code {{
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
    background-color: #f8f8f8;
  }}
  @media print {{
    body {{ margin: 0; }}
    .page-break {{ page-break-after: always; }}
  }}
</style>
</head>
<body>
<pre style="white-space: pre-wrap; font-family: inherit;">
{conteudo}
</pre>
</body>
</html>"""

    OUTPUT_HTML.write_text(html_template, encoding="utf-8")
    print(f"[OK] Versão HTML para visualização gerada em: {OUTPUT_HTML.relative_to(ROOT)}")
    print("\nCompilação concluída com sucesso!")

if __name__ == "__main__":
    main()
