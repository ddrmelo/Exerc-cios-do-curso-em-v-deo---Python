# Ler o peso de 5 pessoas, e dizer qual foi o maior e o menor peso lido

n1 = float(input("Digite o peso da 1º pessoa: "))
maior = menor = n1

for i in range(2, 6):
    n2 = float(input(f"Digite o peso da {i}º pessoa: "))
    if n2 > maior:
        maior = n2
    if n2 < menor:
        menor = n2

print(f'\nO maior peso lido foi de {maior}'
      f'\nO menor peso lido foi de {menor}')
