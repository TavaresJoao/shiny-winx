FROM python:3.8

# Atualizando APT
RUN apt-get -y update
RUN apt-get install -y tzdata

# Define o timezone do container
ENV TZ America/Sao_Paulo

RUN python -m pip install --upgrade pip

RUN mkdir /webapp
WORKDIR /webapp

COPY requirements.txt /webapp
COPY stella/ /webapp/stella
RUN pip install -r requirements.txt