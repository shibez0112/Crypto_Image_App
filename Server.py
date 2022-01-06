# server.py

from flask import Flask, jsonify
from RSA import get_keys

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/register', methods=['GET'])
# def get_RSA_key():
#     RSA_key = get_keys()
#     public_key = RSA_key[0]
#     secret_key = RSA_key[1]
#     print(public_key)
#     print(secret_key)
#     return str(public_key)
#def register():



if __name__ == '__main__':
    app.run(debug=True)
