# DevMetrics API

API REST en **FastAPI** que expone métricas de repositorios de GitHub (stars, forks, issues) y calcula un score simple.

## Features
- FastAPI + OpenAPI/Swagger (`/docs`)
- Estructura limpia por capas (routers / schemas / services)
- Tests con Pytest
- CI con GitHub Actions
- Docker-ready (opcional)

## Run local
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
uvicorn app.main:app --reload