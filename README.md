# Django Shop API

[![Language](https://img.shields.io/badge/language-python-green.svg)](https://github.com/sartim/django_shop_api)
![Build Status](https://github.com/sartim/django_shop_api/workflows/Master%20Workflow/badge.svg)


REST API developed using Django & Django REST framework. It also uses channels for the socket API

##### (Optional)
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    
##### Install requirements
    $ pip install -r requirements.txt

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
    
###### Using gunicorn
    $ gunicorn app.wsgi --log-file -

###### Building & running on docker
    $ docker build -t django-shop-api:latest .
