# syntax=docker/dockerfile:1

FROM python:3.12.2-slim

ENV PORT 5000
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get -y update
RUN apt-get -y install git
RUN pip3 install -r requirements.txt


COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]