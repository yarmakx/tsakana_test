from flask import Flask, jsonify, request
from service import ProductService, ClientService, BillService
from models import Schema

import json

app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods'] = "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/productos", methods=["GET", "POST"])
def productos():
    if request.method == 'GET':
        # list products
        return jsonify(ProductService().list())
    else:
        # register product
        return jsonify(ProductService().create(request.get_json()))


@app.route("/productos/<item_id>", methods=["PUT", "DELETE"])
def productos_item(item_id):
    if request.method == 'PUT':
        # edit
        return jsonify(ProductService().update(item_id, request.get_json()))
    else:
        # deactivate
        return jsonify(ProductService().delete(item_id))

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    if request.method == 'GET':
        # list products
        return jsonify(ClientService().list())
    else:
        # register product
        return jsonify(ClientService().create(request.get_json()))


@app.route("/clientes/<item_id>", methods=["PUT", "DELETE"])
def clientes_item(item_id):
    if request.method == 'PUT':
        # edit
        return jsonify(ProductService().update(item_id, request.get_json()))
    else:
        # delete
        return jsonify(ProductService().delete(item_id))


@app.route("/facturas", methods=["GET", "POST"])
def facturas():
    if request.method == 'GET':
        # list invoices
        return jsonify(BillService().list())
    else:
        # register invoices
        return jsonify(BillService().create(request.get_json()))


@app.route("/facturas/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(BillService().update(item_id, request.get_json()))


if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True, host='0.0.0.0', port=8888)            # run the flask app