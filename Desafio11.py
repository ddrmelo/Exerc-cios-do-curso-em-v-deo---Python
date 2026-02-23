# LArgura e altura de uma parede, e quantos litros de tinta utilizará, sabendo que uma litro pinta 2 m²

l = float(input("Qual a largura da parede? "))
a = float(input("E a altura? "))

area = a*l
t = area/2

print(f'Serão necessários {t}L de tinta para pintar sua parede')
