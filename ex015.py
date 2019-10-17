print('''#####################
##Aluguel de Carros##
#####################''')
print("←→"*30)
dias = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos Km rodou o carro? KM '))
aludia = 60
kmdia = 0.15
cal = (dias*aludia) + (kmdia*km)
print(f'O valor total a pagar é R${cal:.2f}')
print('→←'*30)
