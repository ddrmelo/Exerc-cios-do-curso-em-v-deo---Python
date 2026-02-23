# Ler o primeiro termo e a razão aritmética, e mostrar os 10 primeiros valores
print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
a1 = int(input("Primeiro termo da progressão: "))
r = int(input("Razão da progressão: "))

print(a1, end='-> ')
for i in range(9):
   a2 = (a1 + r)
   a1 = a2
   print(a2, end='-> ')
print('ACABOU')