FROM python:3.6.5
COPY * /app/
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt 
ENTRYPOINT ["python"]
CMD ["app.py"]
ENV FLASK_ENV="docker"
EXPOSE 5000