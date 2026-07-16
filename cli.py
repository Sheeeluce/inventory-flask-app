import requests

BASE_URL = "http://127.0.0.1:5000"

def view_inventory():
    response = requests.get(f"{BASE_URL}/items")
    items = response.json()
    for item in items:
        print(item)

def view_one_item():
    item_id = input("Enter Item ID: ")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    print(response.json())

def add_item():
    barcode = input("Barcode: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))

    data = {
        "barcode": barcode,
        "quantity": quantity,
        "price": price
    }

    response = requests.post(f"{BASE_URL}/items", json=data)
    print(response.json())

def update_item():
    item_id = input("Item ID: ")
    quantity = int(input("New Quantity: "))
    price = float(input("New price: "))

    data = {
        "quantity": quantity,
        "price": price
    }

    response = requests.patch(f"{BASE_URL}/items/{item_id}", json=data)
    print(response.json())

def delete_item():
    item_id = input("Item ID: ")
    response = requests.delete(f"{BASE_URL}/items/{item_id}")

    if response.status_code == 204:
        print("Item deleted successfully.")
    else:
        print(response.json())

while True:
    print("\nInventory Management")
    print("1. View Inventory")
    print("2. View One Item")
    print("3. Add Item")
    print("4. Update Item")
    print("5. Delete Item")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        view_one_item()
    elif choice == "3":
        add_item()
    elif choice == "4":
        update_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        break
    else: print("Invalid option")