# Tasty Todos!

Implementation of the Backbone.js Todo's application using Django and Tastypie.

## Changes

Uses [backbone-tastypie](https://github.com/PaulUithol/backbone-tastypie) to hook backbone up with Tastypie.

The Todo model and TodoList in todos.js had the following line added:

    urlRoot: 'api/v1/todo/',

The rest is identical to the [Todos](http://backbonejs.org/examples/todos/) example!

## Quick Setup with virtualenv

`cd` in to your new project directory.

    # create and activate your virtual environment
    virtualenv env
    source env/bin/activate

    # clone this project and move to the directory
    git clone https://github.com/owensbla/tasty_todos.git tasty_todos
    cd tasty_todos

    # install requirements
    pip install -r requirements.txt

    # sync the database
    python manage.py syncdb --noinput

    # run the server!
    python manage.py runserver

Open up your network tab and watch the API requests roll!