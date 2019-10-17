print('''########################
##Maior e menor valores em Tupla##
########################''')
print('→←'*30)
from random import randint
a = (randint(0,99), randint(0,99), randint(0,99),
     randint(0,99), randint(0,99))
b =sorted(a)
menor = b[0]
maior = b[4]
print('Os valores sorteados foram ',end="→ ")
for z in a:
    print(z,end=" ")

print(f'\nO maior valor é o {maior}')
print(f'O menor valor é o {menor}')
print('→←'*30)



