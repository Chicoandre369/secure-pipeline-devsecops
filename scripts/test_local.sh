#!/bin/bash
set -e
echo "== 1. Tests =="
python -m pytest tests/ -q
echo "== 2. Build =="
docker build -t secure-demo:local .
echo "== 3. Trivy local (si esta instalado) =="
if command -v trivy >/dev/null; then trivy image --severity CRITICAL --exit-code 1 secure-demo:local; else echo "Trivy no instalado"; fi
echo "== OK =="
