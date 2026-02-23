# Digitar vários valores e cadastrar numa lista. Se o número já estiver adicionado, não
# O colocar novamente. Exibir os números em ordem crescente.

lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso!")
    else:
        print(F'Valor duplicado! Não vou adicionar...')

    r = ' '
    while r not in 'SN':
        r = input("Quer continuar? [S/N] ").strip().upper()[0]
    if r == 'N':
        break

print(f'-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')
