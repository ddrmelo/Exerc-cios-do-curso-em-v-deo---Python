# Expressão matemática e olhar se os parênteses estão corretos

r = input("Digite a expressão matemática: ")
lista1 = []
lista2 = []
for i in r:
    if i == '(':
        lista1.append(i)
    elif i == ')':
        lista2.append(i)

if len(lista1) == len(lista2):
    print(f'A expressão está correta!')
else:
    print(f'A expressão está errada!')

# Se eu utilizar alguma expressão do tipo a) + b(, dá como correta, mas está claramente errada