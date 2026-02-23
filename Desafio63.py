# Sequencia de fibonacci com os n primeiros termos

a1 = 0
a2 = 1

cont = 3
print(f'{a1} -> {a2}', end=' -> ')

while cont <= 10:
    a3 = a1 + a2
    print(a3, end=' -> ')
    a1 = a2
    a2 = a3
    cont += 1
print(f'Fim')