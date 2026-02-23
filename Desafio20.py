# mostrar a ordem sorteada entre 4 alunos em ordem

from random import shuffle

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação será:\n{lista}')
# t = 1
# for i in lista:
#     print(f'O {t}º escolhido foi {i}')
#     t += 1
