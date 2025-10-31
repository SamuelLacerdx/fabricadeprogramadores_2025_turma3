import csv 

num = 0

try:
    with open('OCORRENCIAS_2025.csv', newline='') as exemplo_arquivo:
        exemplo_leitor = csv.reader(exemplo_arquivo)
        
        for linha in exemplo_leitor:
            if "Espingarda" in linha[0]: 
                num += 1

    print("O arquivo contém", num, "registros de espingardas")

except FileNotFoundError:
    print("Arquivo não encontrado.")