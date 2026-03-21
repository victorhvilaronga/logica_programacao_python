print("Olá, mundo!")
print(2+3)
print("2+3")
print("2"+"3")
print(10*(5+7)//4)
print('aspas simples')

nota = 8.5
disciplina = 'Logica de programacao'

print(nota)
print(disciplina)

print('Disciplina:', disciplina, 'Nota:', nota)

a = 5 #atribuindo valor para a de 5
b = 7 #atribuindo valor para b de 7

resposta1 = 5 == 7
resposta2 = 5 != 7
print('5 é igual a 7!:', resposta1)
print('5 é diferente de 7!', resposta2)

frase = 'Fala dele'

print(frase)

print(frase[2])

s1 = 'Ola, tenho algo'
s1 = s1 + ' para te falar'

print(s1)

s2 = 'A' + '-' *10 + 'B'

print(s2)

fstring_teste = f'Voce tirou {nota} na disciplina {disciplina}'
print(fstring_teste)

print(s1[0:3])

tamanho = len(s1)
print(tamanho)

idade = input('Digite sua idade: ') #para converter em int basta int(input('Digite sua idade: '))
print('Sua idade é: ', idade)

x = int(input('Insira um número inteiro'))
y = int(input('Insira outro número inteiro'))
resposta = f'O resultado da soma entre {x} e {y} é {x+y}'
print(resposta)