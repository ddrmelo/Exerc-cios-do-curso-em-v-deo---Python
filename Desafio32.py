#Dizer se um ano é bissexto

ano = int(input("Digite o ano: "))
if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
    print("Bissexto")
