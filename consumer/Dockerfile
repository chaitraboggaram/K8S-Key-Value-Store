FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install nano
RUN apt install inetutils-ping
RUN apt-get install -y redis-tools
RUN pip install redis-cli
RUN pip install -r requirements.txt