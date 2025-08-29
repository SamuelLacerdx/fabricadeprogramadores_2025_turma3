from classes_ex_01 import Marinhos
from classes_ex_04 import Pessoa
from classes_ex_03 import Pessoa
from herança_ex_01 import Personagem

objeto1 = Personagem("John Marston", 1873, "a tiros injustamente", "Americano", "espingarda")
objeto2 = Pessoa("Isabela", "09/09/1999", "999.999.999-99", "Tiago", "Fernanda", "9999-9999", "Rua I, 9", "F", 26, 1.68)
objeto3 = Marinhos(1.2, ["Marrom", "Verde"], "Algas e pequenos peixes", "Cheloniidae", "Tartaruga-verde")

def comunicar(falar):
    print(f"Tentando comunicação com {falar}")
    falar.nome()

print("-"*50)
comunicar(objeto1)
print("_"*50)
comunicar(objeto2)
print("-"*50)
comunicar(objeto3)