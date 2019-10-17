print('''#####################
##Contagem de pares##
#####################''')
print('→←'*30)
cont = 0
for i in range(0,51,2):
    cont += 1
    print(i,end=' * ')
print()
print(f'Existem {cont-1} numero pares de 0 até {cont*2-2}')
print('→←'*30)
