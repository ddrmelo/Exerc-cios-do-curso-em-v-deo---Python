# Nome e duas notas de vários alunos. No final, mostrar um boletim contendo a média
# e o programa ainda vai perguntar para mostrar as notas de cada aluno individualmente.
# 999 interrompe
from time import sleep

completa = []
temp = []

while True:
    nome = (input('Nome: '))
    notas = (float(input('Nota 1: ')), float(input('Nota 2: ')))
    media = (notas[0] + notas[1]) / 2
    temp.append(nome)
    temp.append(notas)
    temp.append(media)

    completa.append(temp[:])
    temp.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print(completa)
print('-='*30)
print(f'No. NOME         MÉDIA')
print(f'-'*30)
for i in range(len(completa)):
    print(f'{i} {completa[i][0]:>8} {completa[i][2]:>12}', end=' ')
    print()
# Formatação concluída!
# Falta agora mostrar os dados do aluno
while True:
    print('-' * 30)
    n = int(input('Mostrar notas de qual aluno? (999 interrome): '))
    if n == 999:
        break
    for i in completa[n]:
        print(f'As notas de {completa[n][0]} são {completa[n][1]}')
        break
    print('-'*30)
print(f'FINALIZANDO...')
sleep(0.5)
print('<<< VOLTE SEMPRE >>>')
