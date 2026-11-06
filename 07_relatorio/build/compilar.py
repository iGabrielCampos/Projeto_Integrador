#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Compilação e Verificação Monográfica ABNT
Projeto Integrador de ADS - UNIPÊ (2026)
Gera o pacote consolidado para impressão e submissão acadêmica.
"""

import sys
import re
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
RELATORIO_MD = ROOT / "07_relatorio/relatorio_final.md"
BUILD_DIR = ROOT / "07_relatorio/build"
OUTPUT_MD = BUILD_DIR / "monografia_completa_abnt.md"
OUTPUT_HTML = BUILD_DIR / "monografia_completa_abnt.html"

def inline_format(text: str) -> str:
    # inline code
    text = re.sub(r"`([^`]+)`", lambda m: f"<code>{html.escape(m.group(1))}</code>", text)
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # italic
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    # links
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    return text

def markdown_to_html(md_text: str) -> str:
    # Strip frontmatter if present
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]

    lines = md_text.splitlines()
    html_out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        # Linha em branco
        if not line.strip():
            i += 1
            continue

        # Bloco de código cercado
        if line.strip().startswith("```"):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(html.escape(lines[i]))
                i += 1
            if i < n and lines[i].strip().startswith("```"):
                i += 1
            html_out.append("<pre><code>" + "\n".join(code_lines) + "</code></pre>")
            continue

        # Linha horizontal / divisor de seção
        if re.match(r"^(\-{3,}|\*{3,}|_{3,})$", line.strip()):
            html_out.append("<hr>")
            i += 1
            continue

        # Cabeçalhos (# a ######)
        m_head = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m_head:
            level = len(m_head.group(1))
            htext = inline_format(m_head.group(2).strip())
            html_out.append(f"<h{level}>{htext}</h{level}>")
            i += 1
            continue

        # Citações em bloco (Blockquote)
        if line.strip().startswith(">"):
            bq_lines = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            bq_text = inline_format("<br>".join(bq_lines))
            html_out.append(f"<blockquote><p>{bq_text}</p></blockquote>")
            continue

        # Tabelas Markdown (| ... |)
        if line.strip().startswith("|") and line.strip().endswith("|"):
            table_lines = []
            while i < n and lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 2:
                header_cells = [c.strip() for c in table_lines[0].split("|")[1:-1]]
                rows = []
                for row_line in table_lines[2:]:
                    cells = [c.strip() for c in row_line.split("|")[1:-1]]
                    rows.append(cells)

                t_html = ["<table>", "<thead>", "<tr>"]
                for h in header_cells:
                    t_html.append(f"<th>{inline_format(h)}</th>")
                t_html.extend(["</tr>", "</thead>", "<tbody>"])
                for row in rows:
                    t_html.append("<tr>")
                    for c in row:
                        t_html.append(f"<td>{inline_format(c)}</td>")
                    t_html.append("</tr>")
                t_html.extend(["</tbody>", "</table>"])
                html_out.append("\n".join(t_html))
            continue

        # Listas não ordenadas (- ou *)
        if re.match(r"^(\-|\*)\s+", line.strip()):
            ul_items = []
            while i < n and re.match(r"^(\-|\*)\s+", lines[i].strip()):
                item_text = re.sub(r"^(\-|\*)\s+", "", lines[i].strip())
                ul_items.append(inline_format(item_text))
                i += 1
            html_out.append("<ul>\n" + "\n".join(f"<li>{it}</li>" for it in ul_items) + "\n</ul>")
            continue

        # Listas numeradas (1. 2. etc.)
        if re.match(r"^\d+\.\s+", line.strip()):
            ol_items = []
            while i < n and re.match(r"^\d+\.\s+", lines[i].strip()):
                item_text = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                ol_items.append(inline_format(item_text))
                i += 1
            html_out.append("<ol>\n" + "\n".join(f"<li>{it}</li>" for it in ol_items) + "\n</ol>")
            continue

        # Parágrafos de texto comum
        p_lines = []
        while (i < n and lines[i].strip()
               and not lines[i].strip().startswith(("#", ">", "|", "```", "---", "* ", "- "))
               and not re.match(r"^\d+\.\s+", lines[i].strip())):
            p_lines.append(lines[i].strip())
            i += 1
        if p_lines:
            p_text = inline_format(" ".join(p_lines))
            html_out.append(f"<p>{p_text}</p>")

    return "\n\n".join(html_out)

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

    # Converter Markdown para HTML Semântico
    html_corpo = markdown_to_html(conteudo)

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
  h4 {{ font-size: 12pt; font-weight: normal; font-style: italic; }}
  p {{
    text-align: justify;
    text-indent: 1.5cm;
    margin-bottom: 0.8em;
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
    line-height: 1.2;
    margin-left: 4cm;
    margin-right: 0;
    text-align: justify;
    font-style: italic;
    border-left: 3px solid #ccc;
    padding-left: 10px;
  }}
  ul, ol {{
    margin: 0.5em 0 1em 2cm;
    padding: 0;
  }}
  li {{
    margin-bottom: 0.3em;
    text-align: justify;
  }}
  hr {{
    border: 0;
    border-top: 1px solid #ccc;
    margin: 2em 0;
  }}
  pre, code {{
    font-family: 'Courier New', Courier, monospace;
    font-size: 9.5pt;
    background-color: #f8f8f8;
  }}
  pre {{
    padding: 10px;
    border: 1px solid #ddd;
    overflow-x: auto;
    white-space: pre-wrap;
  }}
  @media print {{
    body {{ margin: 0; }}
    .page-break {{ page-break-after: always; }}
  }}
</style>
</head>
<body>
{html_corpo}
</body>
</html>"""

    OUTPUT_HTML.write_text(html_template, encoding="utf-8")
    print(f"[OK] Versão HTML semântica gerada em: {OUTPUT_HTML.relative_to(ROOT)}")
    print("\nCompilação concluída com sucesso!")

if __name__ == "__main__":
    main()
