# NÚMEROS ÍMPARES
def main():
    x = entrada()
    printImpares(x)
    

def entrada():
    value = int(input())
    while value < 1 or value > 1000: 
        value = int(input("Erro! Valor inválido! Tente novamente: "))
    return value

def printImpares(x):
    for i in range(x+1):
        if i % 2 != 0:
            print(i)

main()