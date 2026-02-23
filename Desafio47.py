# todos os pares entre 1 e 50

# 2 maneiras

for i in range(2, 51, 2):
    print(i)
print('FIM')

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print('FIM')