from flask import Flask, jsonify, request
from inventory import inventory


app = Flask(__name__)

@app.route("/")
def home():
    return "Inventory Management API"

@app.route("/items/<int:item_id>")
def get_items(item_id):

    for item in inventory:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

@app.route("/items", methods = ["POST"])
def add_item():
    data = request.get_json()
    new_item = {
        "id": len(inventory) + 1,
        "barcode": data["barcode"],
        "product_name": data["product_name"],
        "brand": data["brand"],
        "ingredients": data["ingredients"],
        "quantity": data["quantity"],
        "price": data["price"]
    }

    inventory.append(new_item)

    return jsonify(new_item), 201

if __name__ == "__main__":
    app.run(debug=True)