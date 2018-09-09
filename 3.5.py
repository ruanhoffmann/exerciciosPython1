"""5) Escreva uma função que calcule o fatorial de um número inteiro passado como parâmetro. Ex.: 5!=5.4.3.2.1=120
if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) * n
"""

def fatorial(parametro):
    if parametro == 0:
        return 0
    if parametro == 1:
        return 1
    if parametro > 1:
        return fatorial(parametro - 1) * parametro
print(str(fatorial(5)))