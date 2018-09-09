"""4) Implemente uma função que recebe um número (n−ésimo termo) e retorne a série de Fibonacci até este n−ésimo termo."""
def Fibonacci(n):
    i, a, b = 0, 0, 1
    while i < n:
        print(b)
        a, b = b, a+b
        i+=1
Fibonacci(15) 