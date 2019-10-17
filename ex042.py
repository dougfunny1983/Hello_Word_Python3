print('''#############################
##Analisando Triângulo v2.0##
#############################''')
print('→←'*30)
seg1 = float(input('Digite o primeiro seguimento: '))
seg2 = float(input('Digite o segundo seguimento: '))
seg3 = float(input('Digite o terceiro seguimento: '))
print()
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1  and seg3 + seg1 > seg2:
    print(f'Considerando as retas {seg1}, {seg2} e {seg3}:')
    print()
    print('\033[1;32mTEMOS UM TRIÂNGULO!!!')
    if seg1 == seg2 == seg3:
        print()
        print('Este triangulo é um TRIANGULO EQUILÁTERO!!!')
    elif seg1 != seg2 != seg3 != seg1:
        print()
        print('Este triangulo é um TRIANGULO ESCALENO!!!')
    else:
        print()
        print('Este triangulo é um TRIANGULO ISÓSCELES!!!')
else:
    print(f'Considerando as retas {seg1}, {seg2} e {seg3}:')
    print()
    print('\033[1;31mNÃO TEMOS UM TRIÂNGULO!!!')
print()
print('\033[m→←'*30)