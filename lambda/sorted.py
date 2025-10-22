jogadores = [
{'nome': 'Afonso', 'score': 1200, 'level': 15},
{'nome': 'Luanzin do Grau', 'score': 950, 'level': 12},
{'nome': 'Pedro da ZO', 'score': 200, 'level': 3},
{'nome': 'Samuelzin do X!', 'score': 1500, 'level': 18},
{'nome': 'alle do corte', 'score': 400, 'level': 5},
{'nome': 'Vitoria do Bahia', 'score': 388, 'level': 5},
{'nome': 'Xitzin x1 vem e não troca', 'score': 1000000, 'level': 5}
]


ranking = sorted(jogadores, key=lambda jogador:jogador['score'], reverse=True)
for jogador in ranking:
    print(jogador)