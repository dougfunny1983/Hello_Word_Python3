print('''#############
###Tabuada###
#############''')
print('←→'*30)
n = int(input('Digite o numero pra calcular sua tabuada: '))
for i in range(1,11):
    print(f'\033[36m{n} X {i} = {n*i}')
    print()
print('→←'*30)
