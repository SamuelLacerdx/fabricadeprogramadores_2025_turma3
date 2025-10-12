while True:
    fruta = input('digite a fruta: ')
    with open('fruta.txt','a') as arquivo:
        arquivo.write('Fruta' +  fruta +'\n')

    continuar = input('Deseja cadastrar outra Fruta? (s/n):')

    if continuar != 's':
        with open('fruta.txt','r') as arquivo:
            teste=arquivo.read()
            print(teste)

        break

    else:
        continue