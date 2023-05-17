import requests

"""
    before running all the request one by one, make sure that for request that need parameter,
    have already exist in the database
"""
# get all clients
clients = requests.get('http://localhost:7070/clients')

# get one client
client_id = 9
client = requests.get(f'http://localhost:7070/clients/client/{client_id}')

# update existing client
updated_client = requests.put(f'http://localhost:7070/clients/client/{client_id}', {
    "first_name": "samy",
    "middle_name": "handerson",
    "last_name": "bajikile",
    "phone_number": "90902424",
    "email": "harrykesler@gmail.com"
})

store_client = requests.post(f'http://localhost:7070/clients/client', {
    "first_name": "harry",
    "middle_name": "kesler",
    "last_name": "bajikile",
    "phone_number": "90902424",
    "email": "harrykesler@gmail.com"
})

# before running this request make sure that the client_id have a correct id
deleted_client = requests.delete(f'http://localhost:7070/clients/client/{client_id}')
