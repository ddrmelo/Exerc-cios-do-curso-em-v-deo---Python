# fatorial de um número

fat = int(input("Fatorial de: "))
y = fat
x = fat - 1
if fat < 0:
    print(f'Não existe fatorial de número negativo!')
else:
    if 0 <= fat <= 1:
        fat = 1
    else:
        while x != 1:
            fat = fat*x
            x -= 1
print(f'O fatorial de {y} é {fat}')

fat = int(input("Fatorial de: "))

for i in range(fat-1, 0, -1):
    fat = fat*i

print(f'O fatorial vale {fat}')