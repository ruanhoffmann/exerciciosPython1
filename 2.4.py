"""4) Escreva uma função que recebe como parâmetro um dicionário onde
a chave é o nome de um estudante e o valor uma lista com as 3 notas dele.
Este dicionário pode conter 0, 1 ou mais estudantes.
Utilize a função escrita na questão anterior para calcular a média 
para cada estudante e mostre no seguinte formato:

Estudante 1: Média X
Estudante 2: Média X
...
"""
from functools import reduce
estudantes = {
    'victor': [10,9,3],
    'pedro': [10,10,10],
    'risa': [10,1,8]
}

def media(estudante):
    for nome, nota in estudante.items():
        print('Nome:',nome,' Media: ', reduce(lambda x, y: x + y, nota) / len(nota))


media(estudantes)
