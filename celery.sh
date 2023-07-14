#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery --app=tasks:celery worker -l DEBUG 

elif [[ "${1}" == "beat" ]]; then 
  celery --app=tasks:celery beat -l DEBUG

elif [[ "${1}" == "flower" ]]; then
  celery --app=tasks:celery flower
fi