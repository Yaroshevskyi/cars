Cars test application.
More information in docs.

This application use:
- djangorestframework
- postgresql database

Requirements:
- git
- docker
- docker compose

For use application:

    $ git clone https://github.com/Yaroshevskyi/cars.git

    $ cd cars/

Open .env file and create changes with your preferences.
After that run

    $ docker-compose up -d --build
    $ docker-compose exec web python manage.py makemigrations
    $ docker-compose exec web python manage.py migrate
    $ docker-compose exec web python manage.py test
After that all migrations and tests will be running.

The application is ready to use.