from flask import Flask, jsonify
from inventory import inventory


app = Flask(__name__)

@app.route("/")
def home():
    return "Inventory Management API"

@app.route("/items")
def get_items():
    return jsonify(inventory)

if __name__ == "__main__":
    app.run(debug=True)