print('''#######################
##Cálculo do Fatorial##
#######################''')
print('←→'*30)
numero = int(input('Digite um numero: '))
def factorial(x):
    cont = 1
    print(f'Fatorial de !{x}')
    for z in range(x,0,-1):
        print(f'{z} X ', end = '')
        cont = cont * z
    print(f'= {cont}')
    return cont
print(factorial(numero))
print('→←'*30)
