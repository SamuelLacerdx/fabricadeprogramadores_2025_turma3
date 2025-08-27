from classes_ex_03 import Pessoa

pessoas = [
    Pessoa("Ana", "01/01/2000", "111.111.111-11", "Carlos", "Maria", "9999-1111", "Rua A, 1", "F", 25, 1.65),
    Pessoa("Bruno", "02/02/1995", "222.222.222-22", "José", "Paula", "9999-2222", "Rua B, 2", "M", 30, 1.80),
    Pessoa("Carla", "03/03/2010", "333.333.333-33", "Ricardo", "Sandra", "9999-3333", "Rua C, 3", "F", 15, 1.55),
    Pessoa("Diego", "04/04/1988", "444.444.444-44", "Paulo", "Rita", "9999-4444", "Rua D, 4", "M", 37, 1.75),
    Pessoa("Elaine", "05/05/2005", "555.555.555-55", "Roberto", "Lúcia", "9999-5555", "Rua E, 5", "F", 20, 1.60),
    Pessoa("Felipe", "06/06/1990", "666.666.666-66", "Daniel", "Patrícia", "9999-6666", "Rua F, 6", "M", 35, 1.78),
    Pessoa("Gabriela", "07/07/1998", "777.777.777-77", "Eduardo", "Helena", "9999-7777", "Rua G, 7", "F", 27, 1.70),
    Pessoa("Henrique", "08/08/2002", "888.888.888-88", "Marcos", "Clara", "9999-8888", "Rua H, 8", "M", 23, 1.85),
    Pessoa("Isabela", "09/09/1999", "999.999.999-99", "Tiago", "Fernanda", "9999-9999", "Rua I, 9", "F", 26, 1.68),
    Pessoa("João", "10/10/1985", "000.000.000-00", "Sérgio", "Márcia", "9999-0000", "Rua J, 10", "M", 40, 1.82)
]

for pessoa in pessoas:
    pessoa.apresentar() 
    pessoa._contato()
   
