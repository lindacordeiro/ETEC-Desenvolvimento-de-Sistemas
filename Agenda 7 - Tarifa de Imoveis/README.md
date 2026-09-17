# Calculadora de taxa de tarifa de imóveis

Este projeto em Python foi criado para praticar o ciclo **Entrada → Processamento → Saída**. 
<br><br>
O programa solicita o **nome do imóvel**, e o **consumo de água em m3** e retorna a classificação de acordo com as seguintes regras de negócio:
<br><br>

## Condições dadas:
1. Se o tipo for "comercial", exibir:
> Tarifa comercial aplicada – consulte o plano corporativo.
2. Se o tipo for "apartamento" e o consumo for menor que 10 𝑚3 , exibir:
> Consumo econômico – excelente controle de água!
3. Se o tipo for "apartamento" ou for "casa" com consumo de até 25 𝑚3 , exibir:
> Consumo moderado – dentro do padrão residencial.
4. Em qualquer outro caso (consumo acima do limite residencial), exibir:
> Consumo excessivo – adote medidas de economia e verifique vazamentos.

--- 

## Fórmulas utilizadas
---
## Verificação de imóvel
Criei uma função para verificar qual tipo de imóvel o usuário digitou sendo por nome ou número a partir da lista que dei antes da entrada do dado.

```python
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
```

## Classificação de acordo com o imóvel e consumo
Criei uma sequência condicional seguindo as condições dadas de consumo para cada tipo de imóvel
```python
if imovel == 1:
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif imovel == 3 and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif (imovel == 2 or imovel == 3) and consumo <= 25:
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
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