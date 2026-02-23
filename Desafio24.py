# digitar o nome de uma cidade, e dizer se ela começa com a palavra santo

cidade = input("Qual o nome da cidade que você mora? ").upper().strip().split()

if cidade[0] == 'SANTO':
    print(f'Sua cidade começa com a palavra Santo')
else:
    print("Quen quen")
