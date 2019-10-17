print('''####################
##Radar eletrônico##
####################''')
print('→←'*30)
vel = int(input('Digite sua velocidade em Km/h: '))
multa = vel * 7.00
if vel > 80:
    print(f'\033[31mVoce foi multado!!!')
    print(f'Sua velocidade foi {vel}Km/h e sua multa é o equivalente á R${multa:.2f}')
else:
    print('Dirija com cuidado.')
print('\033[m→←'*30)