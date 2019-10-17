print('''#################
##Par ou Ímpar?##
#################''')
print('→←'*30)
print()
num = int(input('Digite um numero: '))
print()
if num % 2 == 0:
    print('\033[36mSeu numero é par.')
else:
    print('\033[35mSeu numero é impar.')
print('\033[m')
print('→←'*30)
