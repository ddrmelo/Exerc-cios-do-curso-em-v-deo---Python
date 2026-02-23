# gerar 5 números aleatórios e colocar numa tupla
# mostrar os valores, quais são o maior e o menor

from random import randint
a1 = randint(1, 10)
a2 = randint(1, 10)
a3 = randint(1, 10)
a4 = randint(1, 10)
a5 = randint(1, 10)

sorteio = (a1, a2, a3, a4, a5)
# sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# Muito mais fácil
print(f'Os valores sorteados foram: ', end='')
for c in sorteio:
    print(c, end=' ')

print(f'\nO maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')

print(f'\nOU\n')
maior = menor = a1
for c in sorteio:
    if c > maior:
        maior = c
    if c < menor:
        menor = c
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
