print('''################
##Tabuada v3.0##
################''')
print('→←'*30)
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-='*10)
    for z in range(11):
        print(f'{n} X {z:>2} = {n*z}')
    print('-='*10)
print('fim da tabuada')
