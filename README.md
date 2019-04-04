# Django Shop API

[![Open Source Love](https://img.shields.io/badge/language-python-green.svg)](https://github.com/sartim/flask_shop_api)
[![Build Status](https://travis-ci.com/sartim/django_shop_api.svg?branch=master)](https://travis-ci.com/sartim/django_shop_api)

REST API which exposes endpoints both for an online shop and a CMS admin. It's developed using Django framework & Django REST framework dependency. The database configuration for the app relies on PostgreSQL.

##### (Optional)
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    
##### Install requirements
    $ pip install -r requirments.txt

##### Add dotenv to project root

You should create a .env file on the project root using the following format:

When using PostgreSQL DB_URL

    ENV={PROD/DEV/STAGE}
    DB_HOST={DB_HOST}
    DB_NAME={DB_NAME}
    DB_USER={DB_USER}
    DB_PASSWORD={DB_PASSWORD}
    DB_PORT={DB_PORT}
    SECRET={SECRET}

When using sqlite for test

    ENV=TEST
    SECRET={SECRET}
       
##### Run server
There are multiple options of running the server

###### For development
    $ ./manage.py runserver
    
###### Using heroku cli
    $ heroku local web
    
###### Using gunicorn
    $ gunicorn app.wsgi --log-file -

###### Building & running on docker
    $ docker build -t django-shop-api:latest .
    
**Deploying API to Heroku**

    $ git init && git add .
    $ git commit -am "init"
    $ heroku create my-app
    $ git push heroku master

Remember to setup database settings on settings.py
