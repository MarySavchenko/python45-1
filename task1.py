product = input()

shop = {
    'milk': 10,
    'butter': 20,
    'tomato': 30,
}

print(shop.get(product, -1))
