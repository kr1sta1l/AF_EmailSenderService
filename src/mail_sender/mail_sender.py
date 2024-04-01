import logging
from social_spam import Mail
from src.config import config


class MailSender:
    def __init__(self, smtp_email: str, smtp_password: str):
        self.email = smtp_email
        self.password = smtp_password
        self.mail = Mail()

    def send_mail(self, recipient, subject, body):
        logging.info(f"Sending mail to {recipient}. Subject: {subject}. Body: {body}")
        self.mail.connect_mail(self.email, self.password)
        try:
            self.mail.set_message(subject, body)
        except Exception as e:
            logging.warning(f"Can't set message({recipient}, {subject}, {body}): {e}")
            raise ValueError(f"Error while setting the message: {e}")
        try:
            self.mail.send_message(recipient)
        except Exception as e:
            logging.warning(f"Can't send message({recipient}, {subject}, {body}): {e}")
            raise ValueError(f"Error while sending the message: {e}")


mail_sender = MailSender(config.MAIL_USER, config.MAIL_PASSWORD)
