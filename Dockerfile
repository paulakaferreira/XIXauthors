FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /docker_dir
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY . .