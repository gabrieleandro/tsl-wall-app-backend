#!/bin/bash
pip3 install --no-cache-dir -r requirements.txt

python3 manage.py migrate # Apply database migrations
python3 manage.py collectstatic --noinput # Collect static files

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn backend.wsgi:application \
    --name backend \
    --bind 0.0.0.0:8000 \
    --workers $GUNICORN_WORKERS \
    --log-level=$GUNICORN_LOG_LEVEL \
    --timeout $GUNICORN_TIMEOUT \
    --log-file=- \
    --access-logfile=- \
    "$@"
