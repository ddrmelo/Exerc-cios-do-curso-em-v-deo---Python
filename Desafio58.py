# computador pensa de 1 até 10, e o jogo só para quando o jogador acertar.
# mostrar quantos palpites foram necessários
from random import randint

pc = randint(1, 10)

n = tot = 0
while n != pc:
    n = int(input("Escolha do jogador: "))
    tot += 1
    if n == pc:
        print(f'Parabéns, você acertou! Eu também escolhi o {n}!')
    else:
        print(f'Erroooooooooooooooooooooooooooooooooooooooooooooou!')

print(f'Você precisou de {tot} tentativas para descobrir o número!')