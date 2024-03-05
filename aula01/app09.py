def main():
    n = int(input(""))
    
    x = entrada(n)
    while x == None:
        x = entrada(n)

    menor = min(x)
    posicaoMenor = x.index(menor)
    print(f'Menor valor: {menor}')
    print(f'Posicao: {posicaoMenor}')

def entrada(n):
    value = input()
    try:
        x = [int(y) for y in value.split(" ",n-1)]
        return x
    except ValueError as e:
        print(f'ERRO! Você digitou uma quantidade de números maior que {n}')
        return None

main()
