#!/bin/bash

cd /home/app \
&& PYTHONDONTWRITEBYTECODE=1 \
export FLASK_APP=src.main:app && \
export FLASK_ENV=development && \
flask run --host=0.0.0.0
