"""5) Toda vez que um homem traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
Escreva uma função que recebe como parâmetro o peso (peso de peixes) e calcule o excesso.
Retorne a quantidade de quilos além do limite e o valor da multa que ele deverá pagar."""

def calculaMultaPeixes(pesoDosPeixes):
        excedente = int(pesoDosPeixes - 50)
        if excedente > 0:
            multa = int(excedente * 4)
            return print('Multa:'+ str(multa) +' R$ \nPeso extra:' + str(excedente)+ ' KG')
        else:
            return print('Como o seu peso foi de '+ str(pesoDosPeixes) + ' KG não deve pagar multa.')
        

calculaMultaPeixes(30)    
calculaMultaPeixes(70)