# soma de todos os números ímpares, múltiplos de 3, entre 1 e 500
s = 0
for i in range (501):
    if i % 2 != 0 and i % 3 == 0:
        s = s + i
        print(f'Soma parcial: {s}')

print(f'A soma de todos os ímpares múltiplos de 3 vale {s}')
