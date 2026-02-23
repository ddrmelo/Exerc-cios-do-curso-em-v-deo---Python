# Ler o ano de 7 pessoas, e dizer quantas são maiores de idade e quantas não são.
# Considerar a maioridade 21 anos...
from datetime import date
ano = date.today().year

maior = menor = 0
for i in range(7):
    nascimento = int(input(f"Digite o ano de nascimento da {i+1}º pessoa: "))
    if ano - nascimento >= 21:
        maior += 1
    else:
        menor += 1

print(f'\nAo todo tivemos {maior} pessoas maiores de idade\nE também tivemos {menor} pessoas menores de idade')
