# Funções
from math import pow

def main():
    n = int(input())
    for _ in range(n):
        x,y = entrada()
        print(f'{calcula(x,y)} ganhou')

def entrada():
    x,y = input().split(" ")
    x = int(x)
    y = int(y)
    while x < 1 or x > 100 or y < 1 or y > 100:
        x,y = input().split(" ")
        x = int(x)
        y = int(y)

    return x,y


def calcula(x,y):
    funcR = pow(3*x,2) + pow(y,2)
    funcB = 2*pow(x,2) + pow(5*y,2)
    funcC = -100*x + pow(y,3)
    if funcR > funcC and funcR > funcB:
        return "Rafael"
    elif funcB > funcR and funcB > funcC:
        return "Beto"
    elif funcC > funcR and funcC > funcB:
        return "Carlos"

main()