# Mostrar os 10 termos da PA, mas o usuário pode pedir mais termos. Se digitar 0, sair

a1 = int(input('Primeiro termo: '))
r = int(input("Digite a razao: "))

cont = tot = 1
t = 1
while t != 0:
    an = a1 + (cont-1)*r
    print(f'{an}', end=' ')
    cont += 1
    tot += 1
    if tot >= 10:
        print()
        t = int(input("Quantos termos a mais? "))
        tot -= t
