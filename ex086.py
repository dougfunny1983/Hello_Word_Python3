print('''########################
##Matriz em Python##
########################''')
print('→←'*20)
print()
matriz = []
cont = 0
cont1 = 0
for z in range(9):
    matriz.append(int(input(f'Digite um valor para [{cont}, {cont1}]: ' )))
    cont1 += 1
    if cont1 == 3:
        cont += 1
        cont1 = 0

for a in range(0,3):
    print(f'[{matriz[a]:^10}]',end='')
print()
for a in range(3,6):
    print(f'[{matriz[a]:^10}]',end='')
print()
for a in range(6,9):
    print(f'[{matriz[a]:^10}]',end='')
print()