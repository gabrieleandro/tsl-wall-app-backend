#!/bin/bash
pip3 install --no-cache-dir -r requirements.txt

python3 manage.py migrate
python3 manage.py collectstatic --noinput

echo Starting TSL Wall App Server.
exec python3 manage.py runserver 0.0.0.0:8000