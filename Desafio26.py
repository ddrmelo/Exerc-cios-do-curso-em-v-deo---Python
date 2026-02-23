# ler uma frase qualquer e dizer quantas vezes aparece a letra a, em que posição
#a letra aparece primeiro, e em que posição pela última vez

frase = input("Digite uma frase: ").strip().upper()

print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("A")}')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind("A")}')
