#!/bin/bash
set -e

echo "=== Executando build da monografia do Projeto Integrador ==="
python3 07_relatorio/build/compilar.py
echo "=== Build finalizado com sucesso ==="
