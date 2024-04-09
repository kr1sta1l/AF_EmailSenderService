FROM python:3.10
LABEL authors="kr1sta1l"

COPY src/ /app/src/
COPY requirements.txt /app/src/requirements.txt

WORKDIR /app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r src/requirements.txt



ENTRYPOINT ["python", "src/main.py"]

# to build the image:
# docker build -t mail_sender_service .

# to run the image:
# docker run --name mail_sender_service -d -p 8030:8000 mail_sender_service


