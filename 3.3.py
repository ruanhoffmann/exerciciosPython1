"""3) Implemente uma função que recebe dois números e imprima na tela apenas os números ímpares entre eles."""
def imprimiImpares(num, num2):
    if num % 2 != 0:
        print('Numero impar:'+str(num))
    else:
        print('Numero par:'+str(num))
    if num2 % 2 != 0:
        print('Numero impar:'+str(num2))
    else:
        print('Numero par:'+str(num2))
imprimiImpares(3,4)