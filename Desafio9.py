# Tabuada de um número

x = int(input("Tabuada de qual número? "))
print('-'*20)
for i in range(11):
    print(f'{i:>5} x {x} = {x*i}')
print('-'*20)