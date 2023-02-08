FROM python:3.7-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/code

WORKDIR /code

USER root

RUN apt-get update

RUN apt-get install -y netcat

COPY requirements.txt ./

COPY entrypoint.sh ./

RUN chmod +x ./entrypoint.sh

RUN pip3 install -r requirements.txt

COPY . ./

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
