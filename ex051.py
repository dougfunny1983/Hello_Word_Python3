print('''#########################
##Progressão Aritmética##
#########################''')
print('Versão com o cálculo de Gaus...')
print('→←'*30)
n = int(input('Digite o enêsimo termo: '))
sn = (1 + n) * (n / 2)
print(sn)
print('→←'*30)
print('versão com 10 termos pré determinados...')
print('→←'*30)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
enesimo = primeiro + (10-1) * razao
for r in range(primeiro, enesimo + razao, razao):
    print(f'{r} → ',end='')
print('Acabou')
print('→←'*30)
