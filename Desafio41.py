# Até 9: mirim, 14 infantil, 19 junior, 20 senior, acima master
from datetime import date

ano = int(input('Ano de nascimento: '))
atual = date.today().year

idade = atual - ano
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print(f'Classificação: INFANTIL')
elif idade <= 19:
    print(f'Classificação: JUNIOR')
elif idade <= 20:
    print(f'Classificação: SENIOR')
else:
    print(f'Classificação: MASTER')
