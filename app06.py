# Soma de Impares Consecutivos I

def main():
    x,y = entrada()
    soma = somaImpares(x,y)
    print(soma)

def entrada():
    x = int(input(""))
    y = int(input(""))
    return x,y

def somaImpares(x,y):
    acumulator = 0
    for i in range(y+1,x):
        if i % 2 != 0:
            acumulator += i
    return acumulator

main()
