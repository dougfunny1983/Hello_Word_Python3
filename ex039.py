print('''#######################
##Alistamento Militar##
#######################''')
from datetime import date
print('→←'*30)
ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
alista = atual - ano
print(f'Você hoje tem {alista} anos de idade, portanto...')
if alista == 18:
    print(f'Você deve se alsitar imediatamente!!! '
          f'Apresente-se na circunscrição mais próxima.')
elif alista < 18:
    print(f'Faltam {18-alista} pra voce se alistar.')
else:
    print(f'Você passou {alista-18} anos do alistamento Militar.')
    print('Voce está inregular no momento. Apresse!!!')
print('→←'*30)
