# Ler 6 números inteiros, e somar apenas os que forem par

sp = tot = 0

for i in range(6):
    n = int(input(f"Digite o {i+1}º número: "))
    if n % 2 == 0:
        sp = sp + n
        tot += 1

print(f'Foram digitados {tot} números pares, e sua soma vale {sp}')
