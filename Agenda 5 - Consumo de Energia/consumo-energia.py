def main():
    nome_aparelho = input("Qual o nome do aparelho? ")
    potencia = float(input("Qual a potencia do aparelho em Watts (W)? "))
    tempo = float(input("Qual o tempo medio de uso diario em horas desse aparelho? "))
    consumoMensal = (potencia * tempo * 30) / 1000
    custo = consumoMensal * 0.75 #considerando 0.75 como um custo medio de consumo por kWh

    print("Aparelho: ", nome_aparelho)
    print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
    print(f"Considerando R$0,75 o valor do kWh o gasto mensal estimado e {custo:.2f} Reais")

main()