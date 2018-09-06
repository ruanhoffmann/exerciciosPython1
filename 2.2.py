"""
2) Faça uma função que verifique se uma letra passada como parâmetro é vogal ou consoante."""


def vogalOuConsoante(letra):
    vogais = 'aeiou'
    if letra.lower() not in vogais:
        return print('consoante')
    return print('vogal')

letra1 = 'a'
letra2 = 'b'
vogalOuConsoante(letra1)
vogalOuConsoante(letra2)