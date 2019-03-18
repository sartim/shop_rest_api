# Shop REST API

REST API using Django REST Framework for an online shop.

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

**Deploying API to Heroku**

    $ git init && git add .
    $ git commit -am "init"
    $ heroku create my-app
    $ git push heroku master

Remember to setup database settings on settings.py
