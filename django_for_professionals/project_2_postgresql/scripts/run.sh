#!/bin/bash

# Spin up the containers, the --build flag makes sure you're
# building again instead of using the cached layers
docker-compose up -d --build

# Run migrations
docker-compose exec web python manage.py migrate
# docker-compose exec web python manage.py \
# createsuperuser --username ubuntu --email 'ubuntu@gmail.com' --noinput
