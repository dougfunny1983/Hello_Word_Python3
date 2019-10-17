print('''###########################
###Conversor de Moedas#####
###########################''')
print('←→'*30)
valor = float(input('Digite quanto voce tem em reais? R$ '))
dolar = 3.76
euro = 4.35
print(f'Dolar hoje: $ {dolar:.2f}')
print(f'Euro hoje: € {euro:.2f}')
print(f'Com R$ {valor:.2f}, voce consegue comprar $ {valor/dolar:.2f} e € {valor/euro:.2f}')
print('←→'*30)
