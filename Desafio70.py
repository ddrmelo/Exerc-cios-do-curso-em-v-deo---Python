# nome e preço de produtos. Quer continuar?
# total da compra, quantos itens > 1000, nome produto mais barato

print(f'-'*50)
print(f'{"LOJA SUPER BARATÃO":>30}')
print(f'-'*50)

total = qtd1000 = cont = barato = 0
nomeBarato = ''
while True:
    nome = input("Nome do produto: ")
    valor = float(input("Valor do produto: R$"))
    cont += 1
    if cont == 1:
        barato = valor
        nomeBarato = nome
    if valor < barato:
        barato = valor
        nomeBarato = nome
    if valor > 1000:
        qtd1000 += 1
    total += valor

    r = ''
    while r not in 'SN':
        r = input("Quer continuar? [S/N]").upper()
    if r == 'N':
        break

print(f'-'*8, 'FIM DO PROGRAMA', '-'*8)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtd1000} valores custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomeBarato} que custa R${barato:.2f}')

