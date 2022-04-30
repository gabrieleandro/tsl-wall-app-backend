# TSL Wall App | Back-End

A TSL - Hiring Assignment project built with [Django](https://www.djangoproject.com/).

Wall App is an application that allows users to register, login, and write on a wall.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment variables](#environment-variables)
- [Usage](#usage)
- [Testing](#testing)
- [Requirements](#requirements)
- [API documentation](#api-documentation)

## Prerequisites

- [Python 3.8 or higher](https://www.python.org/downloads/)

# Installation

Create a virtual environment.

```bash
mkvirtualenv wallapp-env
mkvirtualenv -p python3.8 wallapp-env
workon wallapp-env
```

Clone this repo and install the requirements.

```bash
git clone git@github.com:gabrieleandro/tsl-wall-app-backend.git
cd tsl-wall-app-backend
pip install  -r requirements.txt
python3 manage.py migrate
```

# Environment variables
Copy our .env.example file (included in this repo) or create a .env file with 

```env
DEBUG=
SECRET_KEY=
ALLOWED_HOSTS=

GUNICORN_WORKERS=
GUNICORN_LOG_LEVEL=
GUNICORN_TIMEOUT=

CORS_ORIGIN_WHITELIST=

DEFAULT_FROM_EMAIL=
EMAIL_BACKEND=
SENDGRID_API_KEY=
```

SECRET_KEY: You can generate a key, [here](https://djecrety.ir/).

## Observations
The welcome email will be printed on the console.

The default EMAIL_BACKEND is using django.core.mail.backends.console.EmailBackend. 

Instead of sending out real emails the console backend just writes the emails that would be sent to the standard output [more info](https://docs.djangoproject.com/en/4.0/topics/email/#console-backend).

### In order to send emails using Sendgrid:
Create an API Key in Sendgrid, [here](https://app.sendgrid.com/settings/api_keys).
And set the EMAIL_BACKEND to 
```bash
EMAIL_BACKEND=sendgrid_backend.SendgridBackend
```

# Usage

Run the server using the following command:

```bash
python3 manage.py runserver
```

or

```bash
gunicorn backend.wsgi
```

Now you can access at http://localhost:8000/

# Testing

```bash
python3 manage.py test
```
# Requirements

- [Django REST framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html)
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)

### Optional

- [django-sendgrid-v5](https://github.com/sklarsa/django-sendgrid-v5)

# API Documentation

[Redoc](https://github.com/Redocly/redoc) is an open-source tool for generating documentation from OpenAPI (fka Swagger) definitions.

You can access the API documentation in your http://localhost:8000/redoc/
