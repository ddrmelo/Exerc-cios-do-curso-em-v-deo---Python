# Ler vários elementos, e no final contar quantos foram, colocar em ordem decrescente
# e se o 5 está na lista e suas posições

lista = list()
tot = 0

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    tot += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-='*30)
print(f'Foram digitados um total de {tot} elementos')
lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista! Ele aparece {lista.count(5)} vez(es)'
          f' nas posições: ', end=' ')
    for posicao, valor in enumerate(lista):
        if valor == 5:
            print(f'{posicao}', end=' ')
    print()
else:
    print('O valor 5 não está na lista!')
