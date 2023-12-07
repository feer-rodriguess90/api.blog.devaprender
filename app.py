from requests.auth import HTTPBasicAuth
import requests

resultado = requests.get('http://localhost:5000/login',
                         auth=('fernanda', '123456'))
print(resultado.json())

#utlizar o token dentro das requisições
#autenticar as solicitações usando o modo requests 
resultado_autores = requests.get('http://localhost:5000/autores', headers={'x-access-token': resultado.json()['token']})
print(resultado_autores.json())