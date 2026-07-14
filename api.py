import requests
def get_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v3/product/{barcode}"

    headers = {
        "User-Agent": "InventoryMAnagementSystem/1.0 (student@example.com)"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    data = response.json()
    product = data.get("product", {})
    return {
        "barcode": barcode,
        "product_name": product.get("product_name"),
        "brand": product.get("brands"),
        "ingredients": product.get("ingredients_text")
    }

if __name__ == "__main__":
    product = get_product("3017620422003")
    print(product)