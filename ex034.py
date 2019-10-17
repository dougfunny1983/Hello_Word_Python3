print('''######################
##Aumentos múltiplos##
######################''')
print('←→'*30)
salario = float(input('Digite seu salário: R$ '))
if salario <= 1250.00:
    print(f'Seu salário atual é R${salario:.2f}')
    print(f'Seu salário com 15% de aumento, agora é R${salario + (salario * 15 / 100):.2f}')
else:
    print(f'Seu salário atual é R${salario:.2f}')
    print(f'Seu salário com 10% de aumento, agora é R${salario + (salario * 10 / 100):.2f}')
