#!/bin/sh

echo "Waiting for MongoDB..."

while ! nc -z mongo-db 27017; do
  sleep 0.1
done

echo "MongoDB Started"

python manage.py run -h 0.0.0.0
