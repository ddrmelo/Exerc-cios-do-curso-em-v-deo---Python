# Caixa eletronico. Valor sacado em notas de 20, 20, 10, 1
# Quantas cédulas serão entregues

print('='*20)
print(f'{"BANCO CEV":^20}')
print('='*20)
ced50 = ced20 = ced10 = ced1 = 0
while True:
    ced = int(input("Qual valor você quer sacar? R$"))
    ced50 = ced//50
    ced20 = (ced%50)//20
    ced10 = (ced%50)%20//10
    ced1 = (ced%50)%20%10
    if ced50 > 0:
        print(f'Total de {ced50} cédulas de R$50')
    if ced20 > 0:
        print(f'Total de {ced20} cédulas de R$20')
    if ced10 > 0:
        print(f'Total de {ced10} cédulas de R$10')
    if ced1 > 0:
        print(f'Total de {ced1} cédulas de R$1')
    print('='*60)
    break

print(F'Volte sempre ao BANCO CEV! Tenha um bom dia!')
