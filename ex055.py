print('''##############################
##Maior e menor da sequência##
##############################''')
print('→←'*30)
peso = []
for c in range(1,6):
    peso.append(float(input(f'Digite o {c}º peso → Kg ')))
peso.sort()
print(f'O maior peso lido foi: {peso[4]} Kg')
print(f'o menor peso lido foi: {peso[0]} Kg')
print('→←'*30)
