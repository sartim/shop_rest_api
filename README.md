# Shop REST API

REST API using Django REST Framework for an online shop.

###### (Optional)
    $ virtualenv -p python3 venv
    $ source venv/bin/activate

    $ pip install -r requirments.txt
    $ ./manage.py runserver

**Deploying API to Heroku**

    $ git init && git add .
    $ git commit -am "init"
    $ heroku create my-app
    $ git push heroku master

Remember to setup database settings on settings.py
