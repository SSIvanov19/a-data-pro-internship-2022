# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt &&\
    python -m spacy download mk_core_news_md &&\
    python manage.py migrate &&\
    python manage.py collectstatic --no-input
COPY . /code/
