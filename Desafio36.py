#Aprovar empréstimo de uma casa. Perguntar salário, valor da casa, quantos anos vai pagar
# Prestação não pode passar de 30% do salário. Se passar, negar empréstimo
from time import sleep
valorCasa = float(input("Qual o valor da casa? R$"))
salario = float(input("E quanto você recebe? R$"))
tempo = int(input("E em quantos anos deseja pagar? "))

print('-=-'*30)
print(f'{"Analisando o seu pedido...":^60}')
print('-=-'*30)
sleep(3)

prestacao = valorCasa / (tempo*12)
porcentagem = salario*0.3
print(f'''Para pagar uma casa de R${valorCasa} em {tempo} anos, a prestação
será de R${prestacao:.2f}''')

if prestacao > porcentagem:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo PERMITIDO')
