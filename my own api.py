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

#@app.route('/hello/', methods=['POST', 'GET'])
#def hello():
#    name=input(['your name'])
#    recip=input(['your favorite recipy'])
#    if recip == 'fried eggs':
#        return jsonify({'recipy':recipies[0]})
#    elif recip == 'cake':
#        return jsonify({'recipy': recipies[1]})
#   else:
#        return name + " you want too much"

@app.route('/hello/', methods=['POST', 'GET'])
def hello():
    name = input(['your name'])
    recip = input(['your favorite recipy'])
    recipy = [recipy for recipy in recipies
              if recipy['name'] == recip]
    if len(recipy) == 0:
        return name + " you want too much"
    elif recipy != None:
        return jsonify(recipy)
#    else:
#        return name + " you want too much"

@app.route('/api/v1/add_recipy', methods=['POST'])
def add_recipy():
    if not request.json or not 'recipy' in request.json:
        abort(400)
    recipy= {

        "name" : request.json['name2'],
        "ingridients": request.json['ingridients2'],
        "recipy": request.json['recipy2'],
        "id": request.json['id2']
    }
    recipies.append(recipy)
    return jsonify({'recipy': recipy}), 201


#@app.route('/pers/api/v1/list/<int:res_id>', methods=['GET'])
#def list_recipy_by_id(res_id):
#    for recipy in recipies:
#        if recipy['id'] == res_id:
#            x = res_id - 1
#            return jsonify({'recipy': recipies[x]})
#        else:
#            abort(404)

@app.route('/pers/api/v1/list/<int:res_id>', methods=['GET'])
def list_recipy_by_id(res_id):
    recipy = [recipy for recipy in recipies
        if recipy['id'] == res_id]
    if len(recipy) == 0:
        abort(404)
    elif recipy != None:
        return jsonify(recipy)
    else:
        abort(404)





@app.route('/pers/api/v1/list/', methods=['GET'])
def list_recipy_all():
    return jsonify({'recipy':recipies})

if __name__ == '__main__':
    app.run(port=8882)
