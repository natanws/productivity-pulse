FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./backend/requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./backend /app/
