# Tracker-Api
Tracker APIs in django, postgresql and django rest framework

# Setup Project
    $ mkvirtualenv abc -p /usr/bin/python3.5
    $ pip install -r requirements.txt

# Heroku Deployment
    $ heroku config:set DISABLE_COLLECTSTATIC=0 -a <heroku-app-name>
    $ heroku run python manage.py makemigrations -a <heroku-app-name>
    $ heroku run python manage.py migrate -a <heroku-app-name>
    $ heroku run python manage.py createsuperuser -a <heroku-app-name>
