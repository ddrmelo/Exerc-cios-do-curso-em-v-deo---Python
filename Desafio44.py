# preço e condição
# a vista ou cheque: 10% desconto
# 2x pvalor cheio
# 3x 20% acréscimo

print('=========== LOJAS GUANABARA ===========')
valor = float(input("Preço das compras: R$"))
pagamento = int(input("""FORMAS DE PAGAMENTO
[ 1 ] À vista
[ 2 ] À vista crédito
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais
Qual é a opção? """))

if pagamento == 1:
    print(f'Sua compra de R${valor:.2f} vai custar R${valor*0.9:.2f} no final.')
elif pagamento == 2:
    print(f'Sua compra irá custar R$ {valor:.2f}')
elif pagamento == 3:
    print(f'Sua compra de R${valor:.2f} será parcelada em 2x de R${valor/2:.2f}, sem juros.')
else:
    parcelas = int(input('Quantas parcelas? '))
    novoValor = valor*1.2
    print(f'Sua compra será parcelada em {parcelas}x de {novoValor/parcelas:.2f}, COM JUROS.')
    print(f'Sua compra de R${valor:.2f} vai custar R${novoValor:.2f} no final.')