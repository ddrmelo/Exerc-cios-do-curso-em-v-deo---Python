#Faça o computador pensar em um número entre 0 e 5 e pedir pro usuário escolher.
# Dizer se o usuário venceu ou perdeu

from random import randint

pc = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
num = int(input("Em que número eu pensei? -> "))

if num == pc:
    print(f'Parabéns, você acertou o número. Você venceu!')
else:
    print(f'Venci!!!!! Meu número era o {pc}')
