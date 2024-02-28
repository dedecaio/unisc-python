def main():
    total = 0
    pA,pB,pC = 2,3,5
    a = float(entrada() * pA)
    b = float(entrada() * pB)
    c = float(entrada() * pC)

    total = a+b+c
    pesoTotal = pA+pB+pC

    media = calculaMedia(total, pesoTotal)

    imprimeMedia(media)

def entrada():
    num =  float(input(" "))
    while num < 0 or num > 10:
        num = float(input("Erro: Nota maior ou menor que 10. Digite novamente: "))
    return num

def calculaMedia(total, pesoTotal):
    return total/pesoTotal
def imprimeMedia(media):
    print(f'MEDIA = {media:.1f}')

main()