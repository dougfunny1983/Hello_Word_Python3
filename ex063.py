print('''###############################
##Sequência de Fibonacci v1.0##
###############################''')
print('→←'*30)
termos = int(input('Quantos termos deseja mostrar? '))
t1 = cont = 0
t2 = 1
t3 = 0
print(f'{t1} → {t2}',end=' → ')
condicao = termos - 3
while cont <= condicao:
    t3 = t1 + t2
    print(f'{t3}',end=' → ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
print('→←')
