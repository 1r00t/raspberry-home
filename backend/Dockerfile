FROM python:3.8-alpine
WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV SPEEDTEST_CMD python /code/speedtest_job.py

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN crond -f -l 8
COPY . .

CMD ["flask", "run"]
