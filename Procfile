release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn cafofo_api.wsgi --log-file -