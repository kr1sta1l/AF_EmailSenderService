from .base_dto import BaseDto


class ExceptionDto(BaseDto):
    code: int
    detail: str
