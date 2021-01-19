Repo Scrapper
=============

This project scraps data from GitHub repositories and users via a django management command.

It also exposes scrapped data via a RESTful API.

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3


Installation
------------

Clone the repository::

    $ git clone git@github.com:semanticmx/repo_scrapper.git
    $ cd repo_scrapper

Local Development
-----------------

Pre-requisites for Local Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We used Docker, so before continuing please be sure you have installed the following software:

1. `Docker <https://docs.docker.com/install/#supported-platforms>`_
2. `Docker Compose <https://docs.docker.com/compose/install/>`_

Local Development
^^^^^^^^^^^^^^^^^

Build your containers using the following command::

    $ docker-compose -f local.yml build

Now start django server using::

    $ docker-compose -f local.yml up

If you need to rebuild your container just do::

    $ docker-compose -f local.yml up -d --build

Running Django commands
^^^^^^^^^^^^^^^^^^^^^^^

You can run django management commands from the container, here are some commonly used commands::

    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser


Using The Service
-----------------

Scrap user data
^^^^^^^^^^^^^^^

The scrapping script will take an initial github username as parameter.

Based on that, it will retrieve all its public repositories.

It will also query its followers and it will use that information to scrap more repositories.

We do this recursively, so for every new follower we found we query the follower followers and so on.

In order to avoid an infinite loop, we use MAX_RECURSION_DEPTH environment variable, by default set to 3.

This means we can go down up to three levels of "follower followers" looking for new repositories info.

If you need to collect more information you can set MAX_RECURSION_DEPTH to a higher value.

Once you are comfortable setting the environment variable value, run this command::


    $ docker-compose -f local.yml run --rm django python manage.py scrap_for_username --username <github-username>

Query scrapped data
^^^^^^^^^^^^^^^^^^^

You can now query the scrapped data using cUrl, postman or a similar client.

If you're using Postman you can download the collection from
this `link <https://www.getpostman.com/collections/f89ed195e63d82301f71>`_

Or just load the postman collection and environment from etc/postman folder in this repository.

Available endpoints
^^^^^^^^^^^^^^^^^^^

1. GET /api/repositories/
2. GET /api/repositories/<github_id>/
3. GET /api/users/
4. GET /api/users/<github_id>/
5. GET /api/repositories/?name=<repository_name>
6. GET /api/repositories/?language=<repository_language>

Testing
-------

pytest
^^^^^^^^^^^^^^^

To run pytest please execute the following command::

    $ docker-compose -f local.yml run --rm django pytest

