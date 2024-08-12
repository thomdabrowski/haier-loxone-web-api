# syntax=docker/dockerfile:1

FROM python:3.12.2-slim

ENV PORT 5000
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get -y install git
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install -y curl
ENV FLASK_DEBUG=1


EXPOSE 5000

COPY app.py .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]