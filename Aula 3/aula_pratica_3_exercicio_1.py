print('Bem vindo a sua calculadora particular!')
num1 = int(input('Digite um número inteiro para realizar operações: '))
num2 = int(input('Digite um outro número inteiro para realizar as operações: '))

print(f'Os números são: {num1} e {num2}')
print('Menu de operações')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
opcao = int(input('Qual a operação que deseja realizar?: '))

if (opcao == 1):
    print(f' A soma de {num1} e {num2} é: {num1+num2}')
elif (opcao == 2):
    print(num1-num2)
elif (opcao == 3):
    print(num1*num2)
elif (opcao == 4):
    print(num1//num2)
else:
    print('Opcão não existe')