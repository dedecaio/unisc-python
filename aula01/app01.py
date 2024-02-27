def entrevista():
    contadorIOS = 0
    contadorAndroid = 0
    acumuladorIdade = 0;


    numeroEntrevistados = int(input("Quantas pessoas vamos entrevistar? "))

    for i in range (numeroEntrevistados):
        idade = validaIdade();
        os = verificaOS();
        acumuladorIdade+=idade

        if os == "IOS":
            contadorIOS += 1
        else:
            contadorAndroid += 1  
        print("")

    
    print("\nNúmero de sistemas IOS: ",contadorIOS)
    print("\nNúmero de sistemas androids: ", (contadorAndroid))
    print(f'\nMédia da idade da turma: {calculaMediaIdade(acumuladorIdade, numeroEntrevistados):,.2f}')

def calculaMediaIdade(idadeTotal:int ,numeroEntrevistados: int):
    return idadeTotal/numeroEntrevistados
    
def verificaOS():
    os = input("Qual seu sistema operacional mobile? (Android | IOS) ")
    while os not in ["Android", "IOS"]:
        os = input("SO inválido! Digite SO [IOS | Android]: ")     
    return os;

def validaIdade():
    idade = int(input("Qual a sua idade? "))
    while idade < 0 or idade > 130:
        idade = int(input("Idade inválida!! Qual a sua idade? "))

    return idade

entrevista()
