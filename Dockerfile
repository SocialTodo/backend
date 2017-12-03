FROM python:latest

# Put stdin,stdout, and stderr in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Download docker image requirements
RUN apt-get update
RUN apt-get install -y swig libssl-dev dpkg-dev netcat

RUN mkdir /server
WORKDIR /server
COPY . /server/

RUN python3 -m pip install -U pip
RUN python3 -m pip install -Ur requirements.txt

CMD python3 ./manage.py runserver 0.0.0.0:1337