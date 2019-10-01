FROM python:3.6.5
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"]
CMD ["app.py"]
ENV FLASK_ENV="docker"
EXPOSE 5000