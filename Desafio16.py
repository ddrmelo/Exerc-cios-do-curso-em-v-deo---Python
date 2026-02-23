# Ler um número real e mostrar sua parte inteira: 6.1235454545 → 6
# Ver se o truncar significa pegar a parte inteira do número → Exatamente
from math import trunc
x = float(input("Digite um número qualquer: "))

y = trunc(x)

print(f'O número digitado foi {x} e sua porção inteira vale {y}')
