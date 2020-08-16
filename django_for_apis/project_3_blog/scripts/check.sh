#!/bin/bash

curl http://localhost:8000/apis/v1/?format=json
echo
echo
curl http://localhost:8000/apis/v1/1/ # check single blog detail
echo
echo
curl http://localhost:8000/apis/v1/rest-auth/login
echo
echo
curl http://localhost:8000/apis/v1/rest-auth/logout
echo
echo
curl http://localhost:8000/apis/v1/rest-auth/password/reset
echo
echo
curl http://localhost:8000/apis/v1/rest-auth/password/reset/confirm
echo
echo
curl http://localhost:8000/apis/v1/users/
