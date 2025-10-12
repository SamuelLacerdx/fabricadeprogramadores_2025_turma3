# IMC

# Abaixo do peso: IMC menor que 18,5
# Peso ideal: IMC entre 18,5 e 24,9
# Sobrepeso: IMC entre 25 e 29,9
# Obesidade: IMC igual ou maior que 30 

altura = float(input())
peso = float(input())

resultado = altura * altura
total = peso / resultado

if total <= 18.50:
    print("Abaixo do peso")

elif total <= 18.50 or 24.90:
    print("Peso ideal")

elif total <= 25 or 29.90:
    print("Sobrepeso")

elif total >= 30:
    print("Obesidade")
