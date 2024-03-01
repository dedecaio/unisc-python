def main():
    horas,velocidadeMedia = entrada()
    distancia = calculaDistancia(horas, velocidadeMedia)
    print(f'{distancia/12:.3f}')    

def entrada():
    horas = int(input())
    velocidadeMedia = int(input())

    return horas, velocidadeMedia


def calculaDistancia(horas, velocidadeMedia):
    return horas * velocidadeMedia

main()