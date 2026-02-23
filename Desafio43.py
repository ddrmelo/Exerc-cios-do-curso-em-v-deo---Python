# IMC. abaixo de 18.5 -> abaixo do peso
# até 25 -> Peso ideal
# até 30 sobrepeso
# até 40 obesidade
# acima obesidade mórbida

peso = float(input("Qual o seu peso? "))
alt = float(input("Qual a sua altura? "))

imc = peso / (pow(alt,2))
print(f'Seu IMC vale {imc:.2f}')
if imc < 18.5:
    print(f'Abaixo do peso')
elif imc <= 25:
    print(f'Peso ideal')
elif imc <= 30:
    print(f'Sobrepeso')
elif imc <= 40:
    print(f'Obesidade')
else:
    print(f'Obesidade mórbida')