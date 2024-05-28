import requests,json

def busca_produtos(get):
    url_API = f'http://localhost:8080/api/{get}'
    
    response = requests.request("GET",url_API)
    if response.status_code == 200:
        resp = json.loads(response.text)
        print(resp)


get = 'product-entries'
busca_produtos(get)
