class marinhos():

    def __init__(self, tamanho, cores, alimentacao, genero, especie):
        self.tamanho = tamanho 
        self.corres = cores 
        self.alimenatacao = alimentacao
        self.genero = genero
        self.especie = especie

    def largura (self):
        return print(f"tenho {self.tamanho} de tamanho")
    
    def alimento (self):
        return print(f"eu como: {self.alimenatacao}")
    
    def especi (self):
        return print(f"minha especie é a {self.especie}")
    
    def sexo (self):
        return print(f"o genero da minha especie é a {self.genero}")

animal = marinhos(10.0, ["Azul", "Branco", "Cinza"],"Baleias (principalmente carcaças)", "carcharias", "Carcharodon")
animal.especi()
