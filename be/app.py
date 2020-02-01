from flask import Flask, request, make_response
from flask_cors import CORS
from store import Store

app = Flask(__name__)
CORS(app)
store = Store()


def get_data():
    data = store.get()
    return make_response({"data": data})


@app.route('/', methods=['GET'])
def get():
    data = get_data()
    return data


@app.route('/', methods=['POST'])
def post():
    message = request.json["data"]
    store.put(message)
    return get_data()

