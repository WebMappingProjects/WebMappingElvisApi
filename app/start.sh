#!/bin/sh

if [ "$DATABASE" = "SIG_GEOSPATIAL_DB" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 1
    done

    echo "PostgreSQL started"
fi

echo "=========== make migrations accounts ==========="
python manage.py makemigrations accounts

echo "========================makemigrations ========================"
python manage.py makemigrations buildings 


# echo "=========== make migrations webmapping ==========="
# python manage.py makemigrations webmapping

echo "================= migrate ====================================="
echo "================ accounts ====================================="
python manage.py migrate accounts 
echo "================ buildings ====================================="
python manage.py migrate buildings --check
echo "==============================================================="
python manage.py migrate --check
echo "done ."
# echo "==============================================================="
echo "================= collect static files ========================"
 python manage.py collectstatic --noinput
# echo "done ."

echo "=================running app==================================="
export DJANGO_SETTINGS_MODULE=app.settings
#daphne  --http-timeout 6000 -b 0.0.0.0 -p 8000  app.asgi:application 
python manage.py runserver  0.0.0.0:8000 
