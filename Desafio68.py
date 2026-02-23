# par ou ímpar com o computador. Parar quando o jogador perder. Mostrar qtd de vitórias
from random import randint

vit = 0
print('=-'*30)
print(f'VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-' * 30)
    n = int(input(f'Diga um valor: '))
    pc = randint(0, 10)
    r = input("Par ou ímpar? [P/I] ").upper()
    resultado = n + pc
    print('-'*30)
    if (resultado) % 2 == 0:
        print(f'Você jogou {n} e o computador {pc}. total de {resultado} DEU PAR')
    else:
        print(f'Você jogou {n} e o computador {pc}. total de {resultado} DEU ÍMPAR')
    print('-' * 30)
    if r == 'P' and (resultado) % 2 == 0:
        vit += 1
        print('Você VENCEU!')
        print(f'Vamos jogar novamente...')
    elif r == 'I' and (resultado) % 2 != 0:
        vit += 1
        print('Você VENCEU!')
        print(f'Vamos jogar novamente...')
    else:
        print(f'Você PERDEU!')
        break
if vit == 1:
    print(f'GAME OVER! Você conseguiu vencer somente {vit} vez...')
else:
    print(f'GAME OVER! Você conseguiu vencer {vit} vezes seguidas!')