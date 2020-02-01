#!/bin/bash
set -e
npm install npm@latest -g
json-server db.json --host "0.0.0.0" --port 3000 &
yarn --cwd ./fe/ install && yarn --cwd ./fe/ serve &
env FLASK_APP=be/app.py flask run --host "0.0.0.0" --port 5000
