def main():
    n = int(input(""))
    
    x = entrada(n)
    menor = min(x)
    posicaoMenor = x.index(menor)
    print(f'Menor valor: {menor}')
    print(f'Posicao: {posicaoMenor}')

def entrada(n):
    value = input()
    x = [int(x) for x in value.split(" ") if x.lstrip('-').isdigit()]
    return x

main()
