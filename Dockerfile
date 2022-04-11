FROM python:3.9-slim-bullseye

WORKDIR /code

ENV FLASK_APP=app.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
