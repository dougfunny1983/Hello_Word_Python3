print('''################################
##Conversor de Bases Numéricas##
################################''')
print('→←'*30)
base = int(input('Digite um numero inteiro: '))
pergunta = int(input(f'Digite o numero correspondente pra trasforma o numero inteiro {base} em...'
                     f'\n[1 → Octal]'
                     f'\n[2 → Binário]'
                     f'\n[3 → Hexadecimal]: '))
print('-='*30)
if pergunta == 1:
    print(f'O número {base} em Octal será {oct(base)[2:]}')
elif pergunta == 2:
    print(f'O numero {base} em Binário será {bin(base)[2:]}')
elif pergunta == 3:
    print(f'O numero {base} em Hexadecimal será {hex(base)[2:]}')
print('→←'*30)
