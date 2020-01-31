from nikolaik/python-nodejs
copy db.json /usr/src/app/
workdir /usr/src/app/fe
copy fe/ ./
run npm install -g npm
run npm install -g json-server
EXPOSE 3000
EXPOSE 8080

workdir /usr/src/app
copy be/ ./be
run pip install --no-cache-dir -r be/requirements.txt
EXPOSE 5000
copy launch-services.sh ./
run chmod +x ./launch-services.sh
CMD ./launch-services.sh
