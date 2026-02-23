# Ler nome e peso de várias pessoas guardando numa lista
# a) total cadastrado, b) Listagem com as mais pesadas, c) Lista com as mais leves

tot =  0 # Não era necessário. O tamanho da lista retornaria o total de pessoas cadastradas
listagem = []
oficial = []
pesado = leve = 0


while True:
    listagem.append(input("Digite o nome do pessoa: "))
    listagem.append(float(input('Digite o peso: ')))
    if tot == 0:
        pesado = leve = listagem[1]
    else:
        if listagem[1] > pesado:
            pesado = listagem[1]
        if listagem[1] < leve:
            leve = listagem[1]

    tot += 1
    oficial.append(listagem[:])
    listagem.clear()
    # print(f'Pesado: {pesado}, Leve: {leve}')
    r = ' '
    while r not in 'SN':
        r = input("Quer continuar? [S/N] ").strip().upper()[0]
    if r == 'N':
        break

print('-='*30)
print(f'Ao todo, você cadastrou {tot} pessoas.')
# print(f'Lista oficial: {oficial}')
print(f'O maior peso foi de {pesado} kg. Peso pretencente a: ', end='')

for i in range(len(oficial)):
    if oficial[i][1] == pesado:
        print(f'[{oficial[i][0]}] ', end='')
print(f'\nO menor peso foi de {leve} kg. Peso pertencente a: ', end='')

for i in range(len(oficial)):
    if oficial[i][1] == leve:
        print(f'[{oficial[i][0]}] ', end='')


