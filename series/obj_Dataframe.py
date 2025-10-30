import pandas as pd

dados_times = {'Time': ['Independiente','Boca Juniors','Peñarol', 'River Plate','Estudiantes de La Plata','São Paulo FC', 'Palmeiras','Grêmio','Santos FC'],
               'País': ['Argentina','Argentina','Uruguai','Argentina','Argentina','Brasil',"Brasil",'Brasil','Brasil'],
               'Titulo': [7,6,5,4,4,3,3,3,3]

}
df_times = pd.DataFrame(dados_times)

print("--- DataFrame de Times ---")
print(df_times)

media = df_times ['Titulo'].mean()
print(f'A media de Titulos é: {media: .2f}')

formato = df_times.describe()
print(formato)
