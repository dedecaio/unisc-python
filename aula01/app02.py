# Entrada das medidas da garagem e do terreno do imóvel.
def entradaMedidas():
    larguraGaragem = float (input("Entre com a largura da garagem em metros: "))
    profundidadeGaragem = float (input("Entre com a profundidade da garagem em metros: "))
    larguraTerreno = float (input("Entre com a largura do terreno em metros: "))
    profundidadeTerreno = float (input("Entre com a profundidade do terreno em metros: "))
    return larguraGaragem, profundidadeGaragem, larguraTerreno, profundidadeTerreno

# Entrada da localização do imóvel.
def zonaLocalizacao():
    return validarZona()


def validarZona():
    zona = input("Entre com a zona de localização [Sul=S, Norte=N, Leste=L, Oeste=O]: ")
    while zona not in ['S', 'N', 'L', 'O']:
        zona = input("Zona Incorreta!Entre com a zona de localização [Sul=S, Norte=N, Leste=L, Oeste=O]: ")
    return zona

# Cálculo do percentual de ocupação da garagem em relação ao terreno.
def calculoOcupacao():
    larguraGaragem, profundidadeGaragem, larguraTerreno, profundidadeTerreno = entradaMedidas()  # Chamada da função
    areaGaragem = larguraGaragem * profundidadeGaragem                            # Cálculo da área da garagem.
    areaTerreno = larguraTerreno * profundidadeTerreno                            # Cálculo da área do terreno.
    percentualOcupacao = (areaGaragem  * 100) / areaTerreno                       # Percentual de ocupação da garagem em relação ao terreno.
    print("Percentual de ocupação: {}".format(percentualOcupacao))
    return percentualOcupacao

# Verifica regra de ocupação conforme o plano diretor e apresenta uma mensagem.
def planoDiretor():
    percentual = calculoOcupacao()                                                # Chamada da função calculoOcupacao()
    zona = zonaLocalizacao()                                                      # Chamada da função zonaLocalizacao()
    if zona == "N" and percentual <= 25:
        print("Projeto atende norma de zoneamento do plano diretor")
    elif zona == "L" or zona == "O" and percentual <= 30:
        print("Projeto atende norma de zoneamento do plano diretor")
    elif zona == "S" and percentual <= 40:
        print("Projeto atende norma de zoneamento do plano diretor")
    else:
        print("Revisar medidas, projeto não atende norma de zoneamento do plano diretor")

planoDiretor()                                                                  # Chamada à função principal.