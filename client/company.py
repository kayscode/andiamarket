import requests

# get all clients
companies = requests.get('http://localhost:7070/companies')

# get one client
company_id = 9
company = requests.get(f'http://localhost:7070/companies/company/{company_id}')

# update existing client
updated_company = requests.put(f'http://localhost:7070/companies/company/{company_id}', {
    "name": "andia Bi consulting",
    "description": "some random description",
    "sigle": "AT global",
    "email": "service@andia.com"
})

store_company = requests.post(f'http://localhost:7070/companies/company', {
    "name": "andia technology",
    "description": "some random description",
    "sigle": "AT global",
    "email": "service@andia.com"
})

deleted_company = requests.delete(f'http://localhost:7070/companies/company/{company_id}')
