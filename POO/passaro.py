class Passaro():

    def __init__(self, tamanho, cores, espécie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo

    def cantar(self):
        return print(f"sou um {self.espécie} cantando uma bela camção")
    
    def voar(self):
        return print("batendo asas e; voando...")
    
passaro1 = Passaro(0.14, ["Marrom", "Branco", "Cinza"], "Pardal", "M")
passaro1.cantar()