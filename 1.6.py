"""6) Implemente uma função que recebe quanto você ganha por hora
e o número de horas trabalhadas no mês. 
Calcule e mostre (com print) o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
"""
def calculaSalario(valorHora,totalHoras):
    salarioBruto = int(valorHora*totalHoras)
    ir = int(salarioBruto * 0.11)
    inss = int(salarioBruto * 0.08)
    sindicato = int(salarioBruto * 0.05)
    salarioLiquido = int(salarioBruto - ir - inss - sindicato)
    print('Salario Bruto : ' + str(salarioBruto) +
          '\nIR(11%) :' + str(ir) +
          '\nINSS(8%):' + str(inss) +
          '\nSindicato(5%):' + str(sindicato) +
          '\nSalario Liquido:' + str(salarioLiquido))
calculaSalario(8, 220)
