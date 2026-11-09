from colorama import Fore, Style, init

init(autoreset=True) # Inicializa o Colorama

niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]


def definir_cor(nivel):

    match nivel:
        case 1:
            return Fore.RED
        case 2:
            return Fore.YELLOW
        case 3:
            return Fore.GREEN
        case 4:
            return Fore.CYAN
        case 5:
            return Fore.BLUE
        case _:
            return Fore.WHITE


#Função responsável por exibir a situação do reservatório
def exibir_situacao(nivel):

    if nivel < 1 or nivel > 5:
        print(Fore.WHITE + "Nível inválido!" + Style.RESET_ALL)
        return

    cor = definir_cor(nivel)
    situacao = niveis[nivel - 1]

    print(cor + f"Nível {nivel}: {situacao}" + Style.RESET_ALL)


# Simulação do monitoramento do reservatório
print("----- MONITORAMENTO DO RESERVATÓRIO -----\n")

niveis_atuais = [1, 2, 3, 4, 5]

for nivel in niveis_atuais:
    exibir_situacao(nivel)
