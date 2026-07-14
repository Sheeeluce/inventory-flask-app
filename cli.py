import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/items")
    items = response.json()
    for item in items:
        print(item)

while True:
    print("\nInventory Management")
    print("1. View Inventory")
    print("2. Exit")

    choice = input("Choose: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        break
    else: print("Invalid option")