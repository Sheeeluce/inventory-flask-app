from flask import Flask, jsonify, request
from inventory import inventory
from api import get_product


app = Flask(__name__)

@app.route("/")
def home():
    return "Inventory Management API"

@app.route("/items")
def get_all_items():
    return jsonify(inventory)

@app.route("/items/<int:item_id>")
def get_items(item_id):

    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods = ["POST"])
def add_item():
    data = request.get_json()
    product = get_product(data["barcode"])
    new_item = {
        "id": len(inventory) + 1,
        "barcode": product["barcode"],
        "product_name": product["product_name"],
        "brand": product["brand"],
        "ingredients": product["ingredients"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

@app.route("/items/<int:item_id>", methods=["PATCH"])
def update_item(item_id):
    data = request.get_json()
    for item in inventory:
        if item["id"] == item_id:
            if "barcode" in data:
                item["barcode"] = data["barcode"]

            if "product_name" in data:
                item["product_name"] = data["product_name"]
            
            if "brand" in data:
                item["brand"] = data["brand"]

            if "ingredients" in data:
                item["ingredients"] = data["ingredients"]

            if "quantity" in data:
                item["quantity"] = data["quantity"]

            if "price" in data:
                item["price"] = data["price"]

            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            return "", 204
    return jsonify({"error": "Item not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)