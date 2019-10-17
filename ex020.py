################################
##Sorteando uma ordem na lista##
################################
print('←→'*30)
from random import shuffle
lista = []
for f in range (1, 5):
    lista.append(str(input(f'Digite o nome do {f}º aluno: ')))
shuffle(lista)
print()
print(f'Os alunos sorteados foram:')
print()
for g, z in enumerate(lista):
    print(f'{g+1}ª aluno → {z.title()}')
print('→←'*30)
