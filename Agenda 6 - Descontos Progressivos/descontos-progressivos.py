def main():
    valor_compra = float(input("Digite o valor da compra: "))
    print("______________________________________________")

    if valor_compra < 200:
        valor_final = valor_compra * 0.95
        desconto = valor_compra * 0.05
        percentual = 5
    elif valor_compra < 300:
        valor_final = valor_compra * 0.90
        desconto = valor_compra * 0.10
        percentual = 10
    else:
        valor_final = valor_compra * 0.85
        desconto = valor_compra * 0.15
        percentual = 15

    print(f"Para o valor da compra de R${valor_compra:.2f} o percentual de desconto aplicado foi de {percentual}%")
    print(f"O desconto aplicado foi de R${desconto:.2f}")
    print(f"O valor com desconto e R${valor_final:.2f}")
    
main()