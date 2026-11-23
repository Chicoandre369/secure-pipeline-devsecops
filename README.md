# Secure Pipeline - DevSecOps CI/CD

Pipeline DevSecOps que bloquea secretos, codigo inseguro y vulnerabilidades CRITICAL antes de desplegar a Google Cloud Run.

## Arquitectura
PR / Push a main
  - 1. Gitleaks (secretos)
  - 2. Semgrep (SAST) -> SARIF a GitHub Security
  - 3. Trivy FS + Imagen (bloquea en CRITICAL)
  - 4. SBOM con Syft (CycloneDX)
Si todo pasa -> Deploy a Cloud Run con Workload Identity (sin llaves JSON)

## Como reproducir en 5 minutos
```bash
git clone <tu-repo>
cd secure-pipeline-devsecops
python -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
pytest tests/ -q
docker build -t secure-demo:local .
docker run -p 8080:8080 secure-demo:local
curl http://localhost:8080/health
```

## Como probar que bloquea (demo para entrevista)
1. Crea una rama demo-bloqueo
2. Agrega un secreto FALSO, ej: api_key = "AKIAFAKE1234567890"
3. Abre PR -> Gitleaks debe fallar y bloquear el merge
4. Revierte, abre PR limpio -> Pipeline en verde -> Deploy

## Seguridad
- Sin secretos reales, ni siquiera para probar
- Imagen no-root, multi-stage
- GCP con Workload Identity Federation, nunca JSON keys
- Politica en security-policy.md

## Alcance etico
Solo contra tu propio repo y tu propio proyecto GCP de lab. No escanees repos ajenos.

## Roadmap
- [x] MVP: Gitleaks + Trivy
- [x] V1: Semgrep + SBOM
- [ ] V2: Firma de imagenes (cosign), escaneo de IaC
