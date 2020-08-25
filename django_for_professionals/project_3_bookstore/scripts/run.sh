#!/bin/bash


# Bring down the previously running conatainer instance
docker-compose down

# Clean up dangling images
docker system prune -f

# Spin up the containers, the --build flag makes sure you're
# building again instead of using the cached layers
unset dcf

docker-compose -f $1 up -d --build

# fixing docker permission issues
sudo chown -c -R $USER:$USER .
