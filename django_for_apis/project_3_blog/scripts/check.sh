#!/bin/bash

curl http://localhost:8000/apis/v1/?format=json
echo
echo
curl http://localhost:8000/apis/v1/1/ # check single blog detail
