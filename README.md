# Simple Chatbot


## Build
we can build this app two ways
 - by individual components
 - docker 


### Standard build method

follow these steps
 - Ensure you have node>11 and python3.7

#### Data store
```bash
npm install -g npm 
npm install -g json-server
json-server --watch db.json
```
use a different terminal beyond this point
follow backend build instructions
#### Backend
 - `be/README.md`

follow frontend build instructions
#### Frontend
 - `fe/README.md`



### Docker build method
 - we need docker up and running
 - chmod +x build-and-run.sh
 - ./build-and-run.sh
 - docker build takes a while
 - browse to localhost:8080
