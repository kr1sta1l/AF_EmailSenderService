from fastapi import APIRouter, HTTPException
from src.modules.dto.exception_dto import ExceptionDto

router = APIRouter()


@router.get("/health", responses={200: {"description": "OK",
                                        "model": ExceptionDto}},
            response_model=ExceptionDto)
async def health_check():
    return ExceptionDto(code=200, detail="OK")
