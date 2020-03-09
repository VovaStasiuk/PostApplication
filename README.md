# Test Project
Application for creating post, register user, liked post

## Configurations

Create venv:
```sh
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cp .blog/local_settings.py.example .blog/local_settings.py # Need insert api your Api key for hunter and clearbit
```

Django:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
$ run auto_bot.py
```
For check result auto_bot.py need create super user and login in django-admin panel
