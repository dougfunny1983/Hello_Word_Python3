print('''########################
##Dividindo valores em várias listas##
########################''')
print('→←'*20)
print()
lista = []
listaPares = []
listaImpares = []
pergunta = ''
while pergunta in 'S':
    x = int(input('Digite um valor: '))
    lista.append(x)
    if x % 2 == 0:
        listaPares.append(x)
    else:
        listaImpares.append(x)
    pergunta = str(input('Quer continuar? ')).upper().split()[0]
print()
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {listaPares}')
print(f'A lista de impares é: {listaImpares}')
print('→←'*20)