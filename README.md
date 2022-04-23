# TSL Wall App - Backed

A TSL - Hiring Assignments project.

## Table of Contents

- [Installation](#installation)
- [Environment variables](#environment-variables)
- [Usage](#usage)
- [Test](#test)
- [Requirements](#requirements)

## Installation
Clone this repo and install the requirements.

```bash
git clone git@github.com:gabrieleandro/tsl-wall-app-backend.git
cd tsl-wall-app-backend
pip install  -r requirements.txt
python3 manage.py migrate
```

## Environment variables
Create a .env file with

```env
POSTGRES_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=

DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=

SENDGRID_API_KEY=
```

SECRET_KEY: You can generate a key, [here](https://djecrety.ir/).

SENDGRID_API_KEY: Create an API Key in Sendgrid, [here](https://app.sendgrid.com/settings/api_keys) .

## Usage

Run the server using the following command:

```bash
python3 manage.py runserver
```

Visit localhost:8000/api/check to see the running api.

## Test

```bash
python3 manage.py test
```
## Requirements

- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

### Optional

- [django-sendgrid-v5](https://github.com/sklarsa/django-sendgrid-v5)