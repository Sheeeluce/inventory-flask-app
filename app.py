from flask import Flask, jsonify
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

if __name__ == "__main__":
    app.run(debug=True)