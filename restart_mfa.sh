#!/bin/bash

docker-compose stop -t 0 mfa2 && docker-compose rm -f mfa2 && docker-compose up -d mfa2
