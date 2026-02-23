# Salário maior que 1250, 10% de aumento. Inferior, 15%

salario = float(input("Quanto você ganha atualmente? R$"))
if salario <= 1250:
    salario = salario*1.15
else:
    salario = salario*1.10

print(f'Seu novo salário é de R${salario:.2f}')
