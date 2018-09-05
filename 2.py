"""2) Implemente uma função que recebe o raio de um círculo, calcule e retorna sua área."""

import math
def areaCirculo(raioDoCirculo):
    areaDoCirculo = math.pi * pow(raioDoCirculo,2)
    print(areaDoCirculo)
    pass
raioDoCirculo = float(input('Insira o valor do raio:'))
areaCirculo(raioDoCirculo)