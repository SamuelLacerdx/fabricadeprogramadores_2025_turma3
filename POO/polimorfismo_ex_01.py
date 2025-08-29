from herança_ex_01 import Personagem

personagen = [

    Personagem("Arthur Morgan", 1899, "tuberculose e baleado", "Americano", "revólver"),

    Personagem("John Marston", 1911, "a tiros injustamente", "Americano", "espingarda"),

    Personagem("Dutch van der Linde", 1899, "suicídio (possível)", "Americano", "revólver"),

    Personagem("Bill Williamson", 1906, "a tiros", "Americano", "espingarda"),

    Personagem("Micah Bell", 1907, "a tiros", "Americano", "revólver"),

    Personagem("Sadie Adler", 1907, "sobreviveu (não morreu)", "Americano", "rifle"),

    Personagem("Hosea Matthews", 1899, "velhice e doença", "Americano", "rifle")

]


for p in personagen:
    p.morreu()