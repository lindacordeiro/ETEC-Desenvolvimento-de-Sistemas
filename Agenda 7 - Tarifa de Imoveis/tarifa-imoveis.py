def verifica_imovel(imovel)->int:
    imovel = imovel.lower().strip() #deixa o texto em minúsculo e remove espaços em branco no início e no fim

    match imovel:
        case "1" | "comercial":
            return 1
        case "2" | "casa":
            return 2
        case "3" | "apartamento":
            return 3
        case _:
            return 0

def classificacao(imovel,consumo)->int:

    if imovel == 1:
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    elif imovel == 3 and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    
    elif (imovel == 2 or imovel == 3) and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
 
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
    return 0

    
def main():
    print("Olá usuário!\nEsse programa classifica o perfil de consumo dos imóveis e emite alertas educativos!\n")
    print("Os tipos de imóvel esperados de resposta são:\n 1 - Comercial\n 2 - Casa\n 3 - Apartamento\n")

    imovel = 0 
    while imovel == 0:
        imovel = input(("Qual seu tipo de imóvel? "))
        imovel = verifica_imovel(imovel)
        if imovel == 0:
            print("Tipo de imóvel inválido!\n")

    consumo = float(input("Qual seu consumo mensal de água em metros cúbicos? "))
    classificacao(imovel,consumo)


main()