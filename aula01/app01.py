def calculaMediaIdade(idadeTotal:int ,numeroEntrevistados: int):
    return idadeTotal/numeroEntrevistados
    

def entrevista():
    contadorIOS = 0
    contadorAndroid = 0
    acumuladorIdade = 0;


    numeroEntrevistados = int(input("Quantas pessoas vamos entrevistar? "))

    for i in range (numeroEntrevistados):
        idade = int(input("Qual a sua idade? "))
        os = input("Qual seu sistema operacional mobile? (Android|IOS) ")

        acumuladorIdade+=idade

        if os == "Android":
            contadorAndroid+=1
        elif os == "IOS":
            contadorIOS+=1
        else:
            print("Sistema não reconhecido");
        print("\n")

    
    print("\nNúmero de sistemas IOS: ",contadorIOS)
    print("\nNúmero de sistemas androids: ", (contadorAndroid))
    print(f'\nMédia da idade da turma: {calculaMediaIdade(acumuladorIdade, numeroEntrevistados):,.2f}')


entrevista()
