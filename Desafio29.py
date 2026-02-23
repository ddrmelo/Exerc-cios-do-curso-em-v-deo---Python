# Limite de velocidade. Maior que 80, multa de 7 reais por km excedido

vel = int(input("Qual a sua velocidade? "))

if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você levou uma multa de R${multa}')
