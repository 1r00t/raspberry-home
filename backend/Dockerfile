FROM python:3.8-alpine
WORKDIR /code

ENV FLASK_APP /code/app.py
ENV FLASK_RUN_HOST 0.0.0.0

ENV PYTHONUNBUFFERED=1

ENV SPEEDTEST_CSV_FILE /code/connection_log.csv

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "flask", "run" ]
