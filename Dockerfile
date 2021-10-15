FROM python:3.9-slim-buster
ENV PYTHONBUFFERED=1
WORKDIR /django-backend
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . .