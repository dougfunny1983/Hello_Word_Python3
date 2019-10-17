print('''########################
##Lista composta e análise de dados##
########################''')
print('→←'*20)
print()
lista = [[],[]]
lPl = []
lPp = []

while True:
    nome = str(input('Digite o nome: ')).capitalize()
    peso = float(input(f'Digite o peso da {nome}: '))
    per = str(input('Quer continuar? ')).upper().split()[0]
    lista[0].append(nome)
    lista[1].append(peso)
    if per in 'N':
        break
print(lista)
maior = max(lista[1])
menor = min(lista[1])
print(f'Voce cadastrou {len(lista[0])} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de',end='')
for i, v in enumerate(lista[1]):
    if v == maior:
        print(lista[0][i], end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de',end='')
for i, v in enumerate(lista[1]):
    if v == menor:
        print(lista[0][i], end=' ')
print('→←'*20)
