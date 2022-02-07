release: python manage.py migrate
web: gunicorn Codeshare.wsgi --log-gile=-
heroku config:set DISABLE_COLLECTSTATIC=1