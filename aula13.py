
nome = input('Digite seu nome: ')
altura1 = input('Altura: ')
altura = float(altura1)
peso1 = input('Digite seu Peso: ')
peso = int(peso1)
imc = peso / (altura * altura)

"f-strings"
linha_1 = f'{nome} tem {altura:} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

print()
print('========================')
print()
print(nome)
print(nome, 'tem ', altura, 'de altura.')
print('E pesa ', peso, 'quilos e seu IMC é ', imc)


