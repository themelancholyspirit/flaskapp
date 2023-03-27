from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

users = [
    {
        'name': 'Guga',
        'age': 21,
        'occupation': 'Computer Science'
    },
    {
        'name': 'David',
        'age': 21,
        'occupation': 'Medicine'
    }
]


@app.get('/')
def hello_world():
    return 'Hello, World'

@app.get('/users')
def get_users():
    return jsonify(users)

def create_app():
    return app