# contagem de 10 a 0, com um fim, com intervalos de 1s
from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print(f'FIM!!!!!')