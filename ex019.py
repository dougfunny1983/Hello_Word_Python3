print('''##############################
##Sorteando um item na lista##
##############################''')
print('←→'*30)
import random
lista = []
for f in range (1, 5):
    lista.append(str(input(f'Digite o nome do {f}º aluno: ')))
print()
print(f'O aluno sorteado é {random.choice(lista)}:')
print('→←'*30)
