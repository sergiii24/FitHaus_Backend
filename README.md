# FitHaus_Backend

FitHaus_Backend provides information and support its Android application.

This repository is the back end. It uses Django and Django REST Framework. There is a separate repository for FitHaus Android application.
 ## Requirements

- Python 3.9.2: https://www.python.org/
- SQL Database: For instance: 
    - PostgreSQL 13.3: https://www.postgresql.org/
- Package installer for Python. For instance:
    - pip 21.1.2: https://pypi.org/project/pip/
    
### Other requirements

- Docker & Docker Compose

### First time set up

*The following instructions assume you are on a Ubuntu Linux system.*

Clone this repository to a directory and use the `requirements.txt` file to set up your Python 3.x
virtual environment.

Create a database in PostgreSQL and amend the `DATABASES` setting in `fithaus.setting.py` to reflect the
required database access details, then use Django management commands to set up the database and
load test users from the fixture:

    python manage.py migrate --run-syncdb

For development, the backend should now run with the Django `runserver` command:

    python manage.py runserver 0.0.0.0:8000

Then you can view the site in a browser at:

    http://127.0.0.1:8000

### Run with Docker

To build and run the API with Docker, execute this command:

`docker-compose up --build`
