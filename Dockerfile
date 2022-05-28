FROM ubuntu:22.04
RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping
RUN apt-get install -y dnsutils
RUN apt-get install -y traceroute
RUN apt-get install -y whois

RUN mkdir /code
RUN mkdir /app
RUN mkdir /app/log

COPY ./requirements.txt /code
RUN pip3 install -r /code/requirements.txt --proxy http://192.168.1.3:7890
COPY ./Blueprints /code/Blueprints
COPY ./Logic /code/Logic
COPY ./static /code/static
COPY ./templates /code/templates
COPY ./app.py /code

EXPOSE 8080
WORKDIR /code
CMD ["python3", "app.py"]