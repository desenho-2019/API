FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /API/
WORKDIR /API/
ADD requirements.txt /API/
RUN pip3 install -r requirements.txt
ADD . /API/
