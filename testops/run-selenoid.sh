#!/bin/bash

docker network create selenoid

cd "$(dirname $0)"

docker-compose up -d