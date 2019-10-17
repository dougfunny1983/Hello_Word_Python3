print('''#########################
## Analisador de Textos##
#########################''')
print('→←'*30)
texto = str(input('Digite um nome: ')).title()
print(f'Voce se chama → {texto}')
print(f'Seu nome em maíuculo → {texto.upper()}')
print(f'Seu nome em minúsculo → {texto.lower()}')
a = texto.split()
b = ''.join(a)
print(f'Seu nome contém {len(b)} letras ao total.')
print(f'Seu primeiro nome comtém {len(a[0])} letras')
print('→←'*30)
