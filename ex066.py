print('''#########################
##Maior e Menor valores##
#########################''')
print('→←'*30)
maior = menor = cont = soma = 0
res = ''
while True:
    n = int(input('Digite um numero: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior  = n
        else:
            menor = n

    res = str(input('Quer continuar: '))
    if res in 'Nn':
        break
print(f'A soma dos valores totais é : {soma}')
print(f'A média dos valores é {soma / cont:.2f}')
print(f'o maior numero é o {maior} e o menor é o {menor}')
print('→←'*30)
