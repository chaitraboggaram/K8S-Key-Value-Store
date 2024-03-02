FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN apt-get update
RUN apt-get install -y curl
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--port=8000", "--host=0.0.0.0"]