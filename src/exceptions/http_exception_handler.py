import logging
from fastapi.responses import JSONResponse

from src.modules.dto.exception_dto import ExceptionDto


async def http_exception_handler(request, exc) -> JSONResponse:
    logging.warning(f"Handle error: {exc}")
    exception: ExceptionDto = ExceptionDto(code=exc.status_code, detail=exc.detail)
    return JSONResponse(status_code=exception.code, content=exception.model_dump(mode="json"))
