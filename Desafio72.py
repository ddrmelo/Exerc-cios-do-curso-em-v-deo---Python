# perguntar qual número por extenso de 0 a 20. Repetir se digitar fora do intervalo

tupnum = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
          'treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input("Digite um número entre 0 e 20: "))
while True:
    if num < 0 or num > 20:
        num = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    else:
        break

print(f'Você digitou o número {tupnum[num]}')
