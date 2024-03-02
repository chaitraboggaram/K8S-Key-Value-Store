FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install nano
RUN apt install inetutils-ping
RUN pip install -r requirements.txt
CMD ["python", "huey_consumer.py", "main.huey", "--workers", "4"]