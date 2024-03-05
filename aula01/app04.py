# MÚLTIPLOS
def main():
    v1, v2 = entrada()
    multiplo(v1,v2)

def entrada():
    values = input("")
    v1, v2 = values.split(" ")
    return int(v1), int(v2)

def multiplo(v1,v2):
    if v2 % v1 == 0 or v2 % v1 == 0: 
        print("Sao Multiplos")
    else: 
        print("Nao sao Multiplos")

main()