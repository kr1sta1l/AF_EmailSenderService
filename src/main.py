import logging
from src.config import config

logging.basicConfig(level=config.MS_LOG_LEVEL,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    filename=config.MS_LOG_FILE)

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi
from src.exceptions import http_exception_handler
from src.routers import sender_router, technical_router
from src.routers.health_checks_routes import readiness_router, liveness_router


def configure_app(app: FastAPI) -> None:
    app.include_router(sender_router, prefix="/sender", tags=["Sender"])

    app.add_exception_handler(HTTPException, http_exception_handler)

    app.include_router(technical_router.router, tags=["Technical"])
    app.include_router(readiness_router, prefix="/health")
    app.include_router(liveness_router, prefix="/health")


if __name__ == "__main__":
    app: FastAPI = FastAPI(title="Mail Sender Service")
    configure_app(app)


    @app.get("/openapi.json", include_in_schema=False)
    async def get_openapi_endpoint():
        return JSONResponse(content=get_openapi(title="docs", version="0.1.0", routes=app.routes))


    uvicorn.run(app, host=config.MS_HOST, port=config.MS_PORT)
