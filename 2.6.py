'''
6) Implemente uma função que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem formar um triângulo ou não.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''
def tipoDeTriangulo():
    lado1 = int(input('Lado 1:\n'))
    lado2 = int(input('Lado 2:\n'))
    lado3 = int(input('Lado 3:\n'))
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        print('Não é possivel formar um triangulo')
    else:
        if lado1 == lado2 and lado1 == lado3:
            print('Trinagulo equilatero')
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            print ('Triangulo escaleno')
        else:
            print('Triangulo isoceles')

tipoDeTriangulo()