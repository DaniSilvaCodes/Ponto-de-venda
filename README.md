# Ponto de Venda (PDV)

## O que o código faz

O programa foi criado para implementar um sistema simples de Ponto de Venda (PDV) em Python. Ele permite registrar várias compras, aplicar descontos de acordo com a idade do cliente e o valor da compra, armazenar os valores finais em uma lista e, ao terminar, apresentar um resumo com a quantidade de compras, o total bruto, o total de descontos e o valor final a pagar.

## Como funciona

1. O programa apresenta um menu com a opção de realizar uma compra ou finalizar.
2. Ao escolher realizar uma compra, solicita o valor da compra e a idade do cliente.
3. Verifica se o valor informado é maior que zero e se a idade está dentro do intervalo permitido.
4. Se o cliente tiver 65 anos ou mais, aplica um desconto de 20% sobre o valor original.
5. Depois do primeiro desconto, verifica se o valor restante é maior que R$ 100,00. Se for, aplica mais 10% sobre esse valor já descontado.
6. Soma o valor original ao total bruto e acumula o valor dos descontos concedidos.
7. Guarda o valor final da compra na lista `lista_compras`.
8. Quando o usuário finaliza, percorre a lista e soma os valores finais, mostrando a quantidade de compras, o total bruto, o total de descontos e o valor final.
9. Quando o programa é finalizado, também é gerado um arquivo txt com o nome de "historico.txt", onde mostra todo o histórico do cliente naquele dia

## Como executar

Abra o terminal na pasta `nivel_1` e execute:

```bash
python pdv.py
```

## Tabela de casos de teste

| Nº | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---:|---:|---:|---:|---:|---:|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |
