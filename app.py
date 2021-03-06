from flask import Flask, jsonify, request, render_template
from flasgger import Swagger, swag_from

app = Flask(__name__)

stores = [
    {
        'name': 'My wonderful store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


# POST /store data: {name:}
@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string: name>
@app.route("/store/<string:name>")
def get_store(name):
    # iterate over stores
    # If the store name matched, return that one
    # If none matches return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


# GET /store
@app.route("/store")
def get_stores():
    return jsonify({'stores': stores})


# POST store/<string: name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=['POST'])
def create_items_in_store(name):
    request_data = request.get_json()
    new_item = {
        'name': request_data['name'],
        'price': request_data['price']
    }
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store sot found'})


if __name__ == "__main__":
    app.run(port=5000)
