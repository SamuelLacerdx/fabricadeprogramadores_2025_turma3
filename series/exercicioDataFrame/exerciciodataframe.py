import pandas as pd
import openpyxl 
receitas = pd.read_excel('lista-de-bases.xlsx')

media = df_times ['Titulo'].mean()
print(f'A media de Titulos é: {media: .2f}')

formato = df_times.describe()
print(formato)