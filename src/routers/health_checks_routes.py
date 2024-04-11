from src.config import config
from fastapi_healthchecks.checks.http import HttpCheck
from fastapi_healthchecks.checks.postgres import PostgreSqlCheck
from fastapi_healthchecks.api.router import HealthcheckRouter, Probe

readiness_router = HealthcheckRouter(
    Probe(
        name="readiness",
        checks=[
            HttpCheck(url=f"http://{config.MS_HOST}:{config.MS_PORT}/health")
        ],
    )
)

liveness_router = HealthcheckRouter(
    Probe(
        name="liveness",
        checks=[
            HttpCheck(url=f"http://{config.MS_HOST}:{config.MS_PORT}/health")
        ],
    )
)
