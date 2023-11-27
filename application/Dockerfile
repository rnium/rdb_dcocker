FROM python:3.8-slim-bullseye
WORKDIR /app
COPY ./sec_rdb/requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y gcc g++ libc6-dev make python3-dev libpcre3 libpcre3-dev && \
    pip install --upgrade pip setuptools && \
    pip install -r requirements.txt && \
    pip install uWSGI && \
    mkdir -p /run/uwsgi && \
    apt autoremove --allow-remove-essential -y gcc g++ libc6-dev make python3-dev

RUN pip install psycopg2-binary