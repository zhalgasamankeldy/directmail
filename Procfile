web: gunicorn config.wsgi:application
worker: celery worker --app=directmail.taskapp --loglevel=info
