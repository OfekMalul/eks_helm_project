FROM python:3.9.6-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9090

ENV BACKGROUND_COLOR=blue

CMD python app.py
