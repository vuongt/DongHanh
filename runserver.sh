#!/bin/bash
python manage.py migrate
python manage.py init-university
python manage.py runserver