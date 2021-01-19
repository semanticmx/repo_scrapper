Repo Scrapper
=============

Github repository scrapper

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django


:License: GPLv3


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

Run this command to collect information about a given github username::


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
