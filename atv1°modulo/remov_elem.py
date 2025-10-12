# Exercício 10

# Dada a lista [10, 20, 30, 40, 50]:
# 1. Adicione 60 no final.
# 2. Insira 15 na posição 1.
# 3. Remova o elemento 30.
# 4. Remova o último elemento e guarde-o em uma variável.

lista = [10, 20, 30, 40, 50]
lista.append(60)
print(lista)

lista.insert(1,15)
print(lista)

del lista[2]

teste = lista.pop (5)
print(lista)

print(lista,teste)
