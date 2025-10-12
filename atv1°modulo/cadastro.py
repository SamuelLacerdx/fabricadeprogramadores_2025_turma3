# lista
listCategoria = []
listNome = []
listIdade = []

# variavel
while True:

    nome = input('Digite seu Nome:')
    idade = float(input('Digite sua Idade'))
   

    if idade >= 18:
        categoria = input('Selecione a Categoria Desejada\nA, B, AB:')
        listNome.append(nome)
        listIdade.append(idade)
    
    else: print ('menor de idade')
    
# categoria

    if categoria == ('A'):
        listCategoria.append(categoria)

    elif categoria == ('B'):
        listCategoria.append(categoria)

    elif categoria == ('AB'):
        listCategoria.append(categoria)

    else: 
        print('Erro de Dados')
    
# continuar

    continuar = input('Deseja cadastrar outro aluno? (s/n):')
    if continuar != 's':
        break
    
print('Cadastros:')

for lista in listNome, listIdade, listCategoria:
    print(lista)
