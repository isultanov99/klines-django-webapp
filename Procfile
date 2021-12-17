web: gunicorn klines.wsgi --bind 0.0.0.0:$PORT
python src/manage.py collectstatic --noinput
python src/manage.py migrate