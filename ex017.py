from math import sqrt, pow
print('''########################
##Catetos e Hipotenusa##
########################''')
print('→←'*30)
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hipo = pow(co, 2) + pow(ca, 2)
res = sqrt(hipo)
print(f'O valor da Hipotenusa é {res:.2f}')
print('←→'*30)
