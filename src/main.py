import logging
import uvicorn
from src.config import config
from src.routers import sender_router
from fastapi import FastAPI, HTTPException
from src.exceptions import http_exception_handler

from fastapi.responses import JSONResponse
from fastapi.openapi.utils import get_openapi


def configure_app(app: FastAPI) -> None:
    app.include_router(sender_router, prefix="/sender", tags=["Sender"])

    app.add_exception_handler(HTTPException, http_exception_handler)


if __name__ == "__main__":
    logging.basicConfig(level=config.MS_LOG_LEVEL,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        filename=config.MS_LOG_FILE)

    app: FastAPI = FastAPI(title="Mail Sender Service")
    configure_app(app)


    @app.get("/openapi.json", include_in_schema=False)
    async def get_openapi_endpoint():
        return JSONResponse(content=get_openapi(title="docs", version="0.1.0", routes=app.routes))


    uvicorn.run(app, host=config.MS_HOST, port=config.MS_PORT)
