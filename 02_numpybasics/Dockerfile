FROM ubuntu:20.04
LABEL AUTHOR="haneun:<eungoam12@gmail.com>"

ADD pip.conf /root/.pip/pip.conf

RUN apt-get update &&\
  apt-get install -y python3-pip python3-dev &&\
  apt-get clean &&\
  pip3 install --upgrade pip

RUN pip3 install numpy jupyterlab matplotlib


CMD ["python3"]
