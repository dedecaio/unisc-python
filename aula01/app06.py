# Crescente e Decrescente
def main():
    v = 0
    while v != "":
        x,y = entrada()
        v = verifica(x,y)
        print(v)


def entrada():
    value = input("")
    x,y = value.split(" ")
    return int(x), int(y)

def verifica(x,y):
    if x < y: return "Crescente"
    elif x > y: return "Decrescente"
    else: return ""

main()