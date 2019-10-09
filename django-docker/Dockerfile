FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /API/django-docker
WORKDIR /API/django-docker
ADD requirements.txt /API/django-docker
RUN pip install -r requirements.txt
ADD . /API/django-docker
