# média de duas notas. Abaixo de 5 reprovado, abaixo de 7 recuperação, acima aprovado.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2) / 2
print(f'Sua média é {media}')
if media >= 7:
    print(f'Aprovado')
elif media >= 5:
    print(f'Recuperação')
else:
    print(f'Reprovado')
