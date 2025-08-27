from herança_ex_01 import Personagem

class Personagem2(Personagem):

    def morreu(self):
        print(f"eu morri de {self.morreu}")

personagem2 = Personagem ("John Marston", 1873, "a tiros injustamente", "Americano", "espingarda" )
personagem2.morreu()