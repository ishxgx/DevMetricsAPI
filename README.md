# DevMetrics API

DevMetrics API es una API REST desarrollada con FastAPI que permite analizar repositorios públicos de GitHub y obtener métricas relevantes como estrellas, forks, issues abiertas y una puntuación calculada en base a esos datos.

El objetivo del proyecto es demostrar buenas prácticas de desarrollo backend, arquitectura limpia, testing y automatización mediante integración continua.

## Qué hace esta API

La API consulta directamente la GitHub API oficial y devuelve:

Estrellas del repositorio
Forks
Issues abiertas
Un score calculado en base a una fórmula personalizada

Incluye además un endpoint de health check para validaciones básicas del servicio.

## Endpoints disponibles

Health check
GET /health

Devuelve el estado del servicio.

Métricas de repositorio
GET /metrics/{owner}/{repo}

Ejemplo de uso:

curl [http://127.0.0.1:8000/metrics/tiangolo/fastapi](http://127.0.0.1:8000/metrics/tiangolo/fastapi)

La respuesta contiene:

repo
stars
forks
open_issues
score

## Arquitectura del proyecto

El proyecto está estructurado por capas para mantener una separación clara de responsabilidades.

La carpeta app contiene:

core para configuración
routers para los endpoints
schemas para los modelos de datos con Pydantic
services para la integración con la API de GitHub
main como punto de entrada de la aplicación

Además incluye una carpeta tests con pruebas automatizadas y configuración de CI mediante GitHub Actions.

## Testing

El proyecto está cubierto con tests usando Pytest.

Las llamadas externas a GitHub están mockeadas en los tests para evitar dependencias de red y problemas de rate limit.

Para ejecutar los tests:

pytest

## Cómo ejecutarlo en local

Crear entorno virtual:

python -m venv .venv

Activar entorno en Git Bash:

source .venv/Scripts/activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar la aplicación:

uvicorn app.main:app --reload

La documentación automática de Swagger está disponible en:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Fórmula de cálculo del score

La puntuación se calcula combinando estrellas, forks e issues abiertas. Las estrellas y forks aumentan el score mientras que las issues abiertas lo reducen. El resultado final se normaliza entre 0 y 100.

## Integración continua

El repositorio incluye un workflow de GitHub Actions que ejecuta automáticamente los tests en cada push o pull request. Esto asegura que cualquier cambio mantenga la estabilidad del proyecto.

## Qué demuestra este proyecto

Diseño de APIs con FastAPI
Estructura modular y mantenible
Consumo de APIs externas
Testing automatizado
Buenas prácticas de backend
Integración continua
Organización profesional de repositorio

## Posibles mejoras futuras

Autenticación con token de GitHub para evitar limitaciones de rate
Capa de caché para optimizar rendimiento
Despliegue en producción
Ampliar métricas analizadas
Sistema de ranking o histórico de puntuación

## Autor

IShxgx