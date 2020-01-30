## Chatbot Backend

#### Prerequisites
```
 cd be
 python3 -m venv venv
 source venv/bin/activate
 pip install --upgrade pip
 pip install -r requirements.txt
 env FLASK_APP=app.py flask run
```

#### Verify
upon executing previous commands, 
you should see the following 
```
 * Serving Flask app "app.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

use a different terminal beyond this point

#### Endpoints

 - /
   - posts messages into bot
   - example:
```	
     curl --request POST \
	  --url http://localhost:5000/ \
	  --header 'Content-Type: application/json' \
	  --data '{"data": "ｲんﾉ丂　ﾉ丂　ﾑ　ﾶ乇丂丂ﾑム乇"}'
```

 - /
   - retrieves messages from bot
   - example:
     - http://127.0.0.1:5000/

#### Unit Testing   
 - run test.py 
 ```
    python3 -m unittest test.py 
 ```
 