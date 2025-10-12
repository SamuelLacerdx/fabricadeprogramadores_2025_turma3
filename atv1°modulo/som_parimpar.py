# lista 

listpar = []
listimpar = []
listdigitado = []

# variavel

contador_par = 0
contador_impar = 0
sompar = 0 
somimpar = 0

# for

for i in range(1,11):
    num = float (input("Digite um numero: "))

# if 

    if num % 2 == 0:
        listdigitado.append(num)
        sompar += i
        contador_par += 1
        listpar.append(i)
    
    else: 
        somimpar += i
        contador_impar += 1
        listimpar.append(i)


    print("A lista tem os seguintes numeros: ", listdigitado)

    print("Os numeros pares são: ", listpar)

    print("Os numeros impares são: ", listimpar)

    print("A lista tem ",contador_par," numeros pares")

    print("A lista tem ",contador_impar," numeros impares")

    print("O resultado dos numeros pares é: ", sompar)

    print("O resultado dos numeros impares é: ", somimpar)