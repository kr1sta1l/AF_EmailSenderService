from .base_dto import BaseDto


class MailRequestDto(BaseDto):
    subject: str
    body: str
    recipient: str
