with open('vendas_dia.txt', 'r') as arquivo:
    total_soma = sum(float(linha.strip()) for linha in arquivo)
print(f'A soma total é: R$ {total_soma:.2f}')

