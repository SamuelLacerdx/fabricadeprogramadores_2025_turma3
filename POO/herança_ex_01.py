class Personagem():
    def __init__(self, nome, nascimento, morte ,nacionalidade, habilidade  ):
        
        self.nome = nome
        self.nascimento = nascimento
        self.morte = morte
        self.nacionalidade = nacionalidade
        self.habilidade = habilidade

    def nomee (self):
        return print(f"Ola, tudo bem? meu nome é {self.nome}")
    
    def idadee (self):
        return print(f"Nasci no ano de {self.nascimento}")
    
    def morreu (self):
        return print (f"infelizmente eu morri de {self.morte}")
    
    def nacionalida (self):
        return print (f"eu sou {self.nacionalidade}")
    
    def habilidoso (self):
        return print (f"eu sou muito habilidoso com {self.habilidade}")

personagem1 = Personagem ("Arthur Morgan", 1863, "tuberculose", "Americano", "revolver" )
personagem1.habilidoso()