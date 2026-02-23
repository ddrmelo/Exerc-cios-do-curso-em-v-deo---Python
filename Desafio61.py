# PA com o while

a1 = float(input("Digite o primeiro termo da PA: "))
r = float(input("Digite a razão da PA: "))

cont = 1
print(f'{a1}', end=' -> ')
while cont <= 9:
    an = a1 + r
    print(f'{an}', end=' -> ' )
    a1 = an
    cont += 1

print(f'Acabou')