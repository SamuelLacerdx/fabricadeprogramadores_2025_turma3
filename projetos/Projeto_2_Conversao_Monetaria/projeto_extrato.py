while True:
    print("""
        1. Adicionar Dolar para converter
        2. Convertere para Dolar
        3. Mostar Conversão
        """)
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input('Digite o valor a Converter:'))
    
        with open('vendas_dolar.txt','a') as arquivo:
            arquivo.write(str(valor) + '\n')

        print("Dolar armazenado")

    elif opcao == "2":
        print("Conversão Feita")

        with open('vendas_dolar.txt', 'r') as arquivo:

            for linha in arquivo:
                linha_limpa = float(linha.strip())
                valor_real = linha_limpa * 5
                # print(valor_real)
        
                with open('vendas_real.txt', 'a') as arquivo:
                
                    arquivo.write(str(valor_real) + '\n')

    elif opcao == '3':
        with open('vendas_real.txt', 'r') as arquivo:
            for linha in arquivo:
                linha_limpa = float(linha.strip())
                mostar = linha_limpa
                print(mostar)   