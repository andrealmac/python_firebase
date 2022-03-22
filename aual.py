#Criar o projeto no Firebase
#https://console.firebase.google.com/

#Criar o Database
#Estrutura de arvore

#Interacao com o Database (REST API)
import requests
import json

link = 'https://meuprojetofirebase-6f28d-default-rtdb.firebaseio.com/'

# #Criar uma venda (POST)
# dados = {'cliente':'Andre',
#          'preco':150,
#          'produto':'teclado'} #Dicionario python
# requisicao = requests.post(f'{link}/Vendas/.json', data=json.dumps(dados))#transformar os dados em json -> json.dumps(dados)
# print(requisicao)#code 200 e q deu certo e 400 e erro
# print(requisicao.text)

# #Criar um novo produto (POST)
# dados = {'nome':'teclado',
#          'preco':150,
#          'quantidade':200} #Dicionario python
# requisicao = requests.post(f'{link}/Produtos/.json', data=json.dumps(dados))#transformar os dados em json -> json.dumps(dados)
# print(requisicao)#code 200 e q deu certo e 400 e erro
# print(requisicao.text)

#Editar a venda (PATCH)
# dados = {'cliente':'Augusto'}
# requisicao = requests.patch(f'{link}/Vendas/-MymvGbJuXOTjDbUWOB6/.json', data=json.dumps(dados))
# print(requisicao)
# print(requisicao.text)

#Pegar uma venda especifica ou todas as vendas (GET)
#requisicao = requests.get(f'{link}/.json')
requisicao = requests.get(f'{link}/Vendas/.json')
print(requisicao)
dic_requisicao = requisicao.json()#transformando em json
#print(dic_requisicao)
#print(dic_requisicao['Produtos'])
id_Andre = None
for id_venda in dic_requisicao:
    cliente = dic_requisicao[id_venda]['cliente']
    if cliente == "Andre":
        print(id_venda)
        id_Andre = id_venda

#Deletar uma venda (DELETE)
requisicao = requests.delete(f'{link}/Vendas/{id_Andre}/.json')
print(requisicao)
print(requisicao.text)