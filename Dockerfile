############################################################
# Dockerfile for base Flask-bootstrap Application 
# based on ubuntu:latest
############################################################

FROM python

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /project/requirements.txt

RUN pip3 install -r /project/requirements.txt

COPY /app /project

WORKDIR /project

CMD [ "python3", "server.py" ]