# Se formar um triângulo, mostrar se é equilátero, isosceles ou escaleno

a = int(input("Primeiro lado: "))
b = int(input("Segundo lado: "))
c = int(input("Terceiro lado: "))

if a < b + c and b < a + c and c < a + b:
    print(f'Os números {a}, {b} e {c} formam um triângulo')
    if a == b == c:
        print(f'E o triângulo é equilátero')
    elif a != b != c != c != a:
        print(f'O triângulo é escaleno')
    else:
        print(f'O triângulo é isósceles')
else:
    print(f'Os números {a}, {b} e {c} não formam um triângulo')
