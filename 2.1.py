"""
1) Faça uma função que verifique se uma letra passada como parâmetro é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""
def mascOuFem(letra):
    letra = letra.upper()
    if letra == 'F':
        print('Feminino')
    elif letra == 'M':
        print('Masculino')
    else:
        print('Sexo invalido')
letra = 'f'
mascOuFem(letra)
