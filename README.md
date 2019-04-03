# Django Shop API

REST API which exposes endpoints both for an online shop and a CMS admin. It's developed using Django framework & Django REST framework dependency. The database configuration for the app relies on PostgreSQL.

##### (Optional)
    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    
##### Install requirements
    $ pip install -r requirments.txt
    
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
