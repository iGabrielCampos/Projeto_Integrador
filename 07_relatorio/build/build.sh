#!/bin/bash
set -e

echo "=== Executando build da monografia do Projeto Integrador ==="
python3 07_relatorio/build/compilar.py

if command -v google-chrome &> /dev/null; then
    echo "[INFO] Compilando PDF oficial ABNT via Google Chrome headless..."
    google-chrome --headless --disable-gpu --no-sandbox --print-to-pdf=07_relatorio/build/monografia_completa_abnt.pdf 07_relatorio/build/monografia_completa_abnt.html
    echo "[OK] PDF gerado com sucesso em: 07_relatorio/build/monografia_completa_abnt.pdf"
fi

echo "=== Build finalizado com sucesso ==="
