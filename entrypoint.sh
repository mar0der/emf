#!/bin/sh
flask db upgrade
python seed.py
exec flask run --host=0.0.0.0