"""1) Implemente uma função que leia 5 números e retornew o maior número."""
def maiorDosCinco():
    numeros = []
    for n in range(0,5):
        numeros.append(int(input('Insira o numero ' +str(n)+':')))
    print('maior numero da lista: ',max(numeros))
maiorDosCinco()