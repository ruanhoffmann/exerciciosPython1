"""
3) Faça uma função para ajudar o professor Fachini a calcular as notas dos seus queridos alunos.
 A função deve receber como parâmetro as 3 notas de um estudante.
A função deve calcular a média alcançada pelo aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a seis;
    A mensagem "Reprovado", se a média for menor do que seis;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
def calculaMedia(nota1, nota2, nota3):
    media = float((nota1 + nota2 + nota3)/3)
    if media >= 6 and media != 10:
        print('APROVADO')
    if media < 6:
        print('REPROVADO')
    if media == 10:
        print('APROVADO COM DISTINCAO')

calculaMedia(10,10,2)
