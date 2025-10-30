import pandas as pd

mundias = pd.Series([1992, 1993, 2005])
print('Anos em que o São Paulo foi campeão mundial de futebol:')
print(mundias)

brasileiro = pd.Series ([1977, 1986, 1991, 2006, 2007, 2008])
print('Anos em que o São Paulo foi campeão Brasileiro:')
print(mundias)

mundias = pd.Series([1992, 1993, 2005])
print('Anos em que o São Paulo foi campeão da libertadores:')
print(mundias)

rebaixamentos_palmeiras = pd.Series([2002, 2012])
print('Anos em que o Palmeiras foi Rebaixado:')
print(rebaixamentos_palmeiras)

rebaixamentos_corinthiasn = pd.Series([2007])
print('Anos em que o Corinthians foi Rebaixado:')
print(rebaixamentos_corinthiasn)

print ("Mundial do Palmeiras Não Encontado")
