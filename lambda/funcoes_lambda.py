# cubo
cubo = lambda x: x**3

print(cubo(3))

# delta
delta = lambda a,b,c: b**2-4*a*c

print(delta(1, 12, -13))

# quadrados
numeros = [1,2,3,4,5,6,7,8,9]
quadrado = lambda x: x * x
quadrados = list(map(quadrado,numeros))
print(quadrados)

# nomes 

nomes = ["Boa", "Luffy","Zoey","Rumi","Seon Gi-hun", "Afonso", "Lazarento", "Luan", "Epaminondas", "Elvis Cezar", "Aristotales"]
nomes_longos = list(filter(lambda nomes: len(nomes) > 4,nomes))
print(nomes_longos)