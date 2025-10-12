palavra = input("DIgite uma palavra")
vogais = "aeiouAEIOU"
contador = 0

for item in palavra:
    if item in vogais:
        contador = contador +1

print(contador)
