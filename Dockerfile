FROM python:3.10.13-slim

WORKDIR /opt/hackathon-lib

RUN python -m venv .venv

COPY requirements.txt .
COPY .env .

RUN . .venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

ENV PYTHONUNBUFFERED 1

CMD ["./.venv/bin/python", "src/init.py"]

