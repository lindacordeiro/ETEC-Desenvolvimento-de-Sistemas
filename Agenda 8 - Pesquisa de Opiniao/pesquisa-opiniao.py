def main():
    print("Esse programa foi criado para pesquisa de opinião sobre o grau de satisfacao dos usuários da empresa de marketing TudoWeb!\n")
    idades = []*50
    nomes = []*50
    opiniao = []*50
    excelente = 0
    ruim = 0
    
    for i in range(0,50):
        nomes.append(input("Qual seu nome? "))
        idades.append(int(input("Qual sua idade? ")))
        opiniao.append(input("""Dentre as seguintes opcoes, qual nota você dá ao atendimento prestado pela empresa de marketing TudoWeb?\n
        1 - EXCELENTE\n
        2 - BOM\n
        3 - RUIM\n"""))

        if (opiniao[i]== 1 or opiniao[i].upper() =="EXCELENTE"):
            excelente+1

        if (opiniao[i]== 3 or opiniao[i].upper() =="RUIM"):
            ruim+1

    print("A quantidade de clientes que avaliaram o atendimento como EXCELENTE foi ", excelente)
    print("A quantidade de clientes que avaliaram o atendimento como RUIM foi ", ruim)
            
()