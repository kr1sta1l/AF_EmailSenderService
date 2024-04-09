import logging
import smtplib
from src.config import config
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MailSender:
    def __init__(self, smtp_email: str, smtp_password: str):
        self.email = smtp_email
        self.password = smtp_password
        logging.info("Creating server...")
        self.server = smtplib.SMTP_SSL(config.MAIL_SERVER, config.MAIL_PORT)  # Использовать SMTP_SSL
        logging.info("Server Creater")

    def send_mail(self, recipient, subject, body):
        logging.info(f"Sending mail to {recipient}. Subject: {subject}. Body: {body}")
        message = MIMEMultipart()
        message.attach(MIMEText(body, 'plain', 'utf-8'))
        message['Subject'] = Header(subject, 'utf-8')
        try:
            logging.info("Connecting to the server...")
            self.server.connect(config.MAIL_SERVER, config.MAIL_PORT)
            logging.info("Server created. Logging in...")
            self.server.login(self.email, self.password)
            logging.info("Logged in. Sending message...")
            self.server.sendmail(self.email, recipient, message.as_string())
            logging.info("Message sent. Quitting...")
            self.server.quit()
            logging.info("Server quit.")
        except Exception as e:
            logging.warning(f"Can't send message({recipient}, {subject}, {body}): {e}")
            raise ValueError(f"Error while sending the message: {e}")


mail_sender = MailSender(config.MAIL_USER, config.MAIL_PASSWORD)
