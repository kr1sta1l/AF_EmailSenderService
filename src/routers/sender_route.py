import logging
from src.mail_sender import mail_sender
from fastapi import APIRouter, HTTPException
from src.modules.dto import MailRequestDto, MailResponseDto, ExceptionDto

router: APIRouter = APIRouter()


@router.post("/send_message", response_model=MailResponseDto,
             responses={200: {"description": "Mail sent successfully", "model": MailResponseDto},
                        500: {"description": "Internal server error", "model": ExceptionDto}})
async def send_message_handler(mail_request: MailRequestDto):
    logging.warning(mail_request)
    try:
        mail_sender.send_mail(mail_request.recipient, mail_request.subject, mail_request.body)
        return MailResponseDto(recipient=mail_request.recipient)
    except ValueError as e:
        logging.error(f"send_mail exception {e}")
        raise HTTPException(status_code=500, detail=f"{e}")
