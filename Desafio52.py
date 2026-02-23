# Ler um inteiro, e dizer se ele é primo

n = int(input("Digite um número: "))
tot = 0

for i in range(1, n+1):
    if n % i == 0:
        tot += 1

if tot == 2:
    print(f'O número {n} é primo')
else:
    print(f'O número {n} não é primo')
