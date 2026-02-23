# jokenpo

from random import randint

pc = randint(1, 3)
if pc == 1:
    comp = 'papel'
elif pc == 2:
    comp = 'tesoura'
else:
    comp = 'pedra'

jogador = input("JO - KEN - PO!!! -> ").lower()

if jogador == 'papel':
    if comp =='pedra':
        print(f'O jogador venceu! {jogador} vence {comp}')
    elif comp == 'tesoura':
        print(f'O computador venceu! {comp} vence {jogador}')
    else:
        print(f'EMPATE! Ambos jogaram {comp}')
elif jogador == 'pedra':
    if comp =='tesoura':
        print(f'O jogador venceu! {jogador} vence {comp}')
    elif comp == 'papel':
        print(f'O computador venceu! {comp} vence {jogador}')
    else:
        print(f'EMPATE! Ambos jogaram {comp}')
else:
    if comp =='papel':
        print(f'O jogador venceu! {jogador} vence {comp}')
    elif comp == 'pedra':
        print(f'O computador venceu! {comp} vence {jogador}')
    else:
        print(f'EMPATE! Ambos jogaram {comp}')
