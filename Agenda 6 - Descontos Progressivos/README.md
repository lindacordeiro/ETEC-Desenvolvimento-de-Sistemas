# Calculadora de descontos progressivos

Este projeto em **Python** foi criado para desenvolver um programa que implemente um sistema de desconto progressivo para uma loja online. <br>
O programa solicita o **valor total da compra** e realiza operações condicionais para calcular o desconto final dado ao cliente.<br>
## Condições:
> Se o valor total da compra for **menor** do que **R$ 200,00**, o cliente recebe um desconto de **5%**.
>
>Se o valor total da compra for **maior ou igual** a **R$ 200,00** e **menor** que **R$ 300,00**, o cliente recebe um desconto de **10%**.
>
>Se o valor total da compra for **maior ou igual** a **R$ 300,00**, o cliente recebe um desconto de **15%**.

## Fórmulas utilizadas:
```python
if valor_compra < 200:
    valor_final = valor_compra * 0.95 # aplicando 5% de desconto
    desconto = valor_compra * 0.05 #calcula valor em reais do desconto
    percentual = 5
elif valor_compra < 300: # abrange valores >= 200 e <300 pois o condicional já passou pelos valores menores que 200
    valor_final = valor_compra * 0.90 # aplicando 10% de desconto
    desconto = valor_compra * 0.10 #calcula valor em reais do desconto
    percentual = 10
else: # abrange todos os valores >= 300
    valor_final = valor_compra * 0.85 # aplicando 15% de desconto
    desconto = valor_compra * 0.15 #calcula valor em reais do desconto
    percentual = 15
```

<img 
    align="left" 
    alt="Python" 
    title="Python"
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" 
/>
<img 
    align="left" 
    alt="Git" 
    title="Git"
    width="30px" 
    style="padding-right: 10px;" 
    src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" 
/>