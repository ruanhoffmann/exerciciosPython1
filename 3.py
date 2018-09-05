"""3) Implemente uma função que peça a temperatura em graus Farenheit, transforme e retorne a temperatura em graus Celsius."""
def FarenheitCelsius():
    f = float(input('Insira o valor em Farenheit: '))
    c = (5 * (f-32) / 9)
    return print(c)

FarenheitCelsius()