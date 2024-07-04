FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY reflex_survey ./reflex_survey
COPY rxconfig ./rxconfig

CMD reflex db migrate && reflex run --env prod --backend-only
