print('''########################
##Maior e Menor valores na Lista##
########################''')
print('→←'*20)
print()
maior = 0
menor = 0
lista = list()
for z in range(5):
    lista.append(int(input(f'Digite um valor para a posição {z}: ')))
    if z == 0:
        maior = menor = lista[z]
    else:
        if lista[z] > maior:
            maior = lista[z]
        if lista[z] < menor:
            menor = lista[z]
print(f'Os numeros digitado foram: {lista}')
'''print(f'O maior foi o {maior} digitados na posição '
      f'{lista.index(maior)}... {lista.index(maior,lista.index(maior) + 1)}...')
print(f'O menor foi o {menor} digitados na posição '
      f'{lista.index(menor)}... {lista.index(menor, lista.index(menor) + 1)}...')
print('→←'*30)'''

print(f'O maior foi o {maior} digitados na posição ',end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor foi o {menor} digitados na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()
print('→←'*30)
