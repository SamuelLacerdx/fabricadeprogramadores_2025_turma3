import json

# dados_json = '{"nome": "Ana", "idade":25, "cidade":"São Paulo"}'

# dados_python = json.loads(dados_json)

# print(dados_python["nome"])
# print(dados_python["idade"])


pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie','felineIQ':None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
