# Perguntar quantos jogos de 6 números serão sorteados, entre 1 e 60
# Colocar em uma lista composta. Colocar um timer. Não pode repetir números dentro do mesmo
# jogo

from random import randint
from time import sleep

print('-'*50)
print(f'{"JOGOS DA MEGASENA":^50}')
print('-'*50)

jogos = []
temp = []
cont = 0
n = int(input('Quantos jogos quer que eu sorteie? '))
while cont < n:
    # Criação dos jogos com 6 números
    while True:
        k = randint(1, 60)
        if k not in temp:
            temp.append(k)
        if len(temp) == 6:
            break
    cont += 1
    jogos.append(temp[:])
    temp.clear()

for i in range(n):
    jogos[i].sort()

print(f'-='*5, f'SORTEANDO {n} JOGOS', '-='*5)
for posicao, valor in enumerate(jogos):
    print(f'Jogo {posicao + 1}: {valor}')
    sleep(1)
print(f'-='*5, f' < BOA SORTE > ', '-='*5)
# Concluído com sucesso!