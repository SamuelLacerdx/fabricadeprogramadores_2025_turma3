# saldo
saldo = 1000
# variavel
while True:

    print("====CAIXA ELETRONICO====")
    print("1 - Saldo em conta")
    print("2 - Saque de dinheiro")
    print("0 - Encerrar o programa")

    opcao = input("Digite sua opção: ")

    #  saldo em conta 
    if opcao == '1':
        print('Seu Saldo é: ', saldo)

    # Sacar dinheiro

    elif opcao== '2':
        saque = float (input("Digite o valor de Saque: "))

        if saque > saldo:
            print('⚠️  ERRO: O saque não deve ser realizado, valor desejado maior do em conta')

        else: 
            saldo = saldo - saque
            print('Valor sacado foi de:', saque)
            print('Saldo restante:', saldo)

    # Encerrar o programa

    elif opcao =='0':
        print('Encerrando o programa')
        break


