from flask import Flask, jsonify, abort
from flask import render_template
from flask import request
import json

app = Flask(__name__)

recipies = [
    {
        "name":"fried eggs",
     "ingridients": "eggs, butter, fire",
     "recipy": "just crush eggs",
    "id":1
     },

    {
        "name":"cake",
     "ingridients": "a lot of cake staff",
     "recipy": "just crush it together and put in the store",
     "id":2
     }
]

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello/', methods=['POST', 'GET'])
def hello():
    name=input(['your name'])
    recip=input(['your favorite recipy'])
    if recip == 'fried eggs':
        return jsonify({'recipy':recipies[0]})
    elif recip == 'cake':
        return jsonify({'recipy': recipies[1]})
    else:
        return name + " you want too much"


@app.route('/pers/api/v1/list/<int:res_id>', methods=['GET'])
def list_recipy_by_id(res_id):
    recipy = filter(lambda t: t['id']== res_id, recipies)
    if recipy == 0:
        abort(404)
    return jsonify({'recipy':recipies[0]})

@app.route('/pers/api/v1/list/', methods=['GET'])
def list_recipy_all():
    return jsonify({'recipy':recipies})

if __name__ == '__main__':
    app.run(port=8882)
