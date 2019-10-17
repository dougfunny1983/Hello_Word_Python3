print('''################################
##Tratando vários valores v2.0##
################################''')
print('→←'*30)
soma = cont = 0
while True:
    n = int(input('Digite um numero ([999] para parar): '))
    if n != 999:
        soma += n
        cont += 1
    else:
        print(f'Foram digitados {cont} numeros')
        break
print(f'A soma total é {soma}')
print('←→'*30)
