from math import sqrt
print('''##############################
#Dobro, Triplo, Raiz Quadrada#
##############################''')
print('-='*30)
n = int(input('Digite um numero: '))
dobro = n*2
triplo = n*3
raiz = sqrt(n)
print(f'O dobro de {n} é {dobro}!')
print(f'O triplo de {n} é {triplo}')
print(f'A raiz de {n} é {raiz:.2f}')
