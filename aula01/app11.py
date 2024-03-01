# Idade em Dias

def main():
    value = entrada()
    calcula(value)


def entrada(): return int(input())


def calcula(value):
    ano = int(value/365)
    mes = int((value%365)/30)
    dia = int(((value%365)%30))
    print(f'{ano} ano(s)')
    print(f'{mes} mes(es)')
    print(f'{dia} dia(s)')

main()