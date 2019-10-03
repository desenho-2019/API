FROM python:3.6.5
RUN pip3 install --upgrade pip
COPY requirements.txt /
WORKDIR /
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY app/ /app/
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
ENV FLASK_ENV=app.py
EXPOSE 5000