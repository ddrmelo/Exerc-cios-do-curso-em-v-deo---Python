# 50 centavos por km para viagens até 200km, e 45 centavos acima disso

km = float(input("Quantos km percorridos? "))

if km <= 200:
    total = km * 0.50
    print(f'Você está prestes a começar uma viagem de {km} km.\nA passagem custará R$ {total:.2f}')
else:
    total = km * 0.45
    print(f'Você está prestes a começar uma viagem de {km} km.\nA passagem custará R$ {total:.2f}')

