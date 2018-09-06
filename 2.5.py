"""

5) Implemente uma função para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
A função deverá receber o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
Formato da saída:

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00  
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00
"""
def calculaSalario(valorHora,totalHoras):
    salarioBruto = int(valorHora*totalHoras)
    if salarioBruto <= 900:
        ir = 0
        pctg = '0%'
    elif salarioBruto <= 1500 and salarioBruto > 900:
        ir = int(salarioBruto * 0.05)
        pctg = '5%'
    elif salarioBruto <= 2500 and salarioBruto > 1500:
        ir = int(salarioBruto * 0.1)
        pctg = '10%'
    else:
        ir = int(salarioBruto * 0.2)
        pctg = '20%'
    fgts = int(salarioBruto * 0.11)
    inss = int(salarioBruto * 0.1)
    sindicato = int(salarioBruto * 0.03)
    salarioLiquido = int(salarioBruto - ir - inss - sindicato)
    print('Salario Bruto : ' + str(salarioBruto) +
          '\nIR('+pctg+') :' + str(ir) +
          '\nINSS(10%):' + str(inss) +
          '\nFGTS(11%):' + str(fgts) +
          '\nSindicato(5%):' + str(sindicato) +
          '\nSalario Liquido:' + str(salarioLiquido))
calculaSalario(5, 220)
