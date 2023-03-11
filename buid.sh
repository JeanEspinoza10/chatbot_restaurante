#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install -r requirements.txt
flask db init
flask db migrate -m "Comentario"
flask db upgrade
flask seed run