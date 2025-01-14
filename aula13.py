nome = 'Gustavo Fragata'
altura = 1.78
peso = 76
imc = peso / (altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura' # f-string, maniera mais facil de formatar strings para não ter que escrever muitos prints
print(linha_1)

linha_2 = f'pesa, {peso} ,quilos e seu IMC é'
print(linha_2)

linha_3 = f'{imc:.2f}'
print(linha_3)
#f = formatação, f-string

# print(nome, "tem", altura, "de altura,")
# print("pesa", peso ,"quilos e seu IMC é")
# print(imc)
