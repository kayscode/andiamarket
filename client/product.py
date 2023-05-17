import requests

# get all clients
products = requests.get('http://localhost:7070/products')

# get one client
product_id = 9
product = requests.get(f'http://localhost:7070/products/product/{product_id}')

# update existing client
updated_product = requests.put(f'http://localhost:7070/products/product/{product_id}', {
    "name": "chips simba",
    "description": "some random description",
    "price": 45.5,
})

store_product = requests.post(f'http://localhost:7070/products/product', {
    "name": "chips simba",
    "description": "some random description",
    "price": 45.5,
})

deleted_product = requests.delete(f'http://localhost:7070/products/product/{product_id}')
