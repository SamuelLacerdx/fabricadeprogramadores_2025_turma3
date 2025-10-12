while True:
    email = input('Digite o e-mail: ')
    nome = input('digite o Nome: ')
    with open('cadastro.txt','a') as arquivo:
        arquivo.write('Nome' +  nome + '|' + 'Email'+ email + '\n') 

    continuar = input('Deseja cadastrar outro aluno? (s/n):')
    if continuar != 's':
        with open('cadastro.txt','r') as arquivo:
           teste=arquivo.read()
           print(teste)

        break

    else:
     continue
