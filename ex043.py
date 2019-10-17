print('''############################
##Índice de Massa Corporal##
############################''')
print('→←'*30)
peso = float(input('Digite seu peso: [KG] → '))
altura = float(input('Digite sua atura: [Metros] → '))
imc = peso / altura ** 2
if imc <= 18.5:
    cond = 'Abaixo do Peso. ATENÇÃO!!!'
elif imc <= 25:
    cond = 'Peso Ideal. PARABÉNS!!!☻'
elif imc <= 30:
    cond = 'Sobrepeso. CUIDADO!!!'
elif imc <= 40:
    cond = 'Obesidade. PROCURE UM MÉDICO!!!'
else:
    cond = 'Obesidade Mórbida. VOCÊ CORRE SERIOS RISCOS DE SAÚDE!!!'
print(f'Seu IMC: {imc:.1f}')
print(f'Sua condição é: {cond}')
print('→←'*30)