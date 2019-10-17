print('''##############################
## Gerenciador de Pagamentos##
##############################''')
print('→←'*30)
preco = float(input('Preço normal: R$ '))
a_vista = preco - (preco * 10 / 100)
cartao = preco - (preco*5/100)
cartao_3x = preco + (preco*20/100)
while True:
    escolha = int(input('Qual é a forma de pagamento?\n1 → á vista'
                        '\n2 → cartão a vista'
                        '\n3 → cartão em 2 vezes'
                        '\n4 → cartão em 3 vezes'
                        '\n0 → pra encerrar o programa: '))
    if escolha == 1:
        print()
        print(f'Você pagará a vista o valor de R${a_vista:.2f}.')
        print()
    elif escolha == 2:
        print()
        print(f'Voce pagará no cartão a vista o valor de R${cartao:.2f}.')
        print()
    elif escolha == 3:
        print()
        print(f'Você pagara a prazo em 2 vezes no cartão o total de R${preco:.2f}.\n'
              f'Totalizando 2 prestações de R${preco/2:.2f} cada.')
        print()
    elif escolha == 4:
        print()
        print(f'Você pagará a prazo em 3 vezes no cartão o total de R${cartao_3x:.2f},\n'
              f'Totalizando 3 prestaçoes de R${cartao_3x/3:.2f} cada.')
        print()
    elif escolha > 4:
        print()
        print('Escolha inválida. Tente de novo. Escolha 1, 2, 3 ou 4. "0" para encerra o programa.')
        print()
    else:
        print()
        print('Programa encerrado...')
        print()
        break
print('→←'*30)
