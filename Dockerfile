FROM python:3.9.6-slim-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python","app.py"]
