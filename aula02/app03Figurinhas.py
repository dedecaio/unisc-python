from sys import setrecursionlimit

def main():
    setrecursionlimit(10000)
    n = input()
    n = int(n)
    while n > 3000 or n < 1:
        n = input()
        n = int(n)
    for _ in range(n):
        f1, f2 = entrada()
        calcula(f1,f2)


def entrada():
    f1, f2 = input().split(" ")
    f1 = int(f1)
    f2 = int(f2)
    while f1 < 1 or f1 > 1000 or f2 < 1 or f2 > 1000:
        f1, f2 = input().split(" ")
        f1 = int(f1)
        f2 = int(f2)
    return f1, f2

def calcula(f1,f2):
    listaF1 = mdc(f1, 1, [])
    listaF2 = mdc(f2, 1, [])
    comuns = list(set(listaF1).intersection(listaF2))
    print(max(comuns))

def mdc(f, i, divisores):
    if i <= f:
        if f % i == 0:
            divisores.append(i)
        divisores = mdc(f,i+1,divisores)

    return divisores
main()