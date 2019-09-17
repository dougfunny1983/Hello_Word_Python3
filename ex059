print('''#############################
##Criando um Menu de Opções##
#############################''')
print('→←'*30)
maior = menor = 0
while True:
    n1 = int(input('Digite o primeiro numero → '))
    n2 = int(input('Digite o segundo numero → '))
    opcao =int(input('Escolha um opção parar:\n'
                     '# 1 para Adição\n'
                     '# 2 para subtração\n'
                      '# 3 para divisao\n'
                      '# 4 para multiplicacao\n'
                      '# 5 para maior número\n'
                      '# 6 para menor numero\n'
                      '# 7 para novos números\n'
                      '# 0 para sair → '))
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    print(f'Voce escolheu a opção: {opcao}')
    if opcao >= 0 and opcao < 8:
        if opcao == 1:
            print(f'{n1} + {n2} = {n1+n2}')
        elif opcao == 2:
            print(f'{n1} - {n2} = {n1-n2}')
        elif opcao == 3:
            print(f'{n1} ÷ {n2} = {n1/n2}')
        elif opcao == 4:
            print(f'{n1} X {n2} = {n1*n2}')
        elif opcao == 5:
            print(f'entre o {n1} e o {n2} o maior é {maior}')
        elif opcao == 6:
            print(f'Entre o {n1} e o {n2} o menor é {menor}')
        elif opcao == 7:
            print('Escolha novos numeros.')
        elif opcao == 0:
            print('Finalizando o programa')
            print('Volte sempre!!!')
            break
    else:
        print('Opção incorreta. Escolha entre 0 e 7')
print('→←'*30)
