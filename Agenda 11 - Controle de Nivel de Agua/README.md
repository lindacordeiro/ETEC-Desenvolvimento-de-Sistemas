# Controle de nível de água

Esse é um sistema simples de monitoramento de um reservatório de água. <br>

Esse sistema será executado no terminal e tem como objetivo exibir mensagens de alerta com cores diferentes, conforme o nível de água do reservatório. <br>

Para tornar a visualização mais clara, será utilizada a biblioteca colorama, permitindo destacar cada situação com uma cor específica. <br>

## Condições:
## 💧 Níveis do Reservatório

| Nível | Situação | Cor |
|:---:|---|:---:|
| **Nível 1** | Muito baixo (crítico) | <span style="color:#e74c3c">🔴 Vermelho</span> |
| **Nível 2** | Baixo | <span style="color:#f1c40f">🟡 Amarelo</span> |
| **Nível 3** | Médio | <span style="color:#2ecc71">🟢 Verde</span> |
| **Nível 4** | Alto | <span style="color:#00bcd4">🔵 Ciano</span> |
| **Nível 5** | Muito alto (alerta) | <span style="color:#3498db">🔵 Azul</span> |