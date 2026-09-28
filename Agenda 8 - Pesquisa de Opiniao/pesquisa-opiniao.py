def coleta_pesquisa_opiniao(n):
    idades = []*n    #multiplicando um vetor pela quantidade de indices que iremos utilizar
    nomes = []*n
    opiniao = []*n

    for i in range(0,n):

        verifica_dado = False
        while verifica_dado == False:
            nome = input("Qual seu nome? ")

            if not any(caractere.isdigit() for caractere in nome):  #verifica se há números na sequência de caracteres digitada
                nomes[i] = nome
                verifica_dado = True

            else:
                print("O nome contém valor número!\n")

        verifica_dado = False
        while verifica_dado == False:
            idade = input("Qual sua idade? ")

            try: #quero verificar se o valor digitado é um número inteiro, acredito que com o try except seja o melhor metodo)
                idade = int(idade)
                
                idades[i] = idade
                verifica_dado = True

            except ValueError:
                print("O valor digitado não é um número inteiro!")

        opiniao.append(input("""Dentre as seguintes opcoes, qual nota você dá ao atendimento prestado pela empresa de marketing TudoWeb?\n
        1 - EXCELENTE\n
        2 - BOM\n
        3 - RUIM\n"""))

        if (opiniao[i]== 1 or opiniao[i].upper() =="EXCELENTE"):
            excelente+1

        if (opiniao[i]== 3 or opiniao[i].upper() =="RUIM"):
            ruim+1

        return excelente,ruim


def main():
    print("Esse programa foi criado para pesquisa de opinião sobre o grau de satisfacao dos usuários da empresa de marketing TudoWeb!\n")

    excelente = 0
    ruim = 0

    excelente,ruim = coleta_pesquisa_opiniao(3)
    print("A quantidade de clientes que avaliaram o atendimento como EXCELENTE foi ", excelente)
    print("A quantidade de clientes que avaliaram o atendimento como RUIM foi ", ruim)
            
()