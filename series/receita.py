import pandas as pd

receitas = pd.read_csv('receitas.csv')

print(receitas)

media = receitas ['Custo'].mean()
print(f'A media de custos é: {media: .2f}')

formato = receitas.describe()
print(formato)