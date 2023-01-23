FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/django_app
RUN apk add graphviz ttf-freefont
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY . .