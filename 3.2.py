"""2) Implemente uma função que leia 5 números e retorna a soma e a média dos números."""
from statistics import mean
def somaEmedia():
    numeros = []
    for n in range(0,5):
        numeros.append(int(input('Insira o numero:')))
    print('Soma dos numeros:' + str(sum(numeros)))
    print('Media dos numeros:'+ str(mean(numeros)))    
somaEmedia()