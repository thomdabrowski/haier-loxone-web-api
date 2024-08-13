FROM python:3.12.5-slim-bookworm

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get -y update && apt-get -y install git
RUN pip install -r /code/requirements.txt

COPY app-fast.py .

EXPOSE 80

CMD ["fastapi", "run", "app-fast.py", "--port", "80"]
