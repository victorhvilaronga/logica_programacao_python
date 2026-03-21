#Exercício da aula teórica, elabore um sistema para pedir notas de materias, depois calcular a média e exibir se o aluno foi aprovado ou nao
print('Olá Professor! Bem vindo ao sistema de notas da escola Uninter.')
nome = (input('Digite o nome completo do primeiro aluno: '))
matematica = float(input('Digite a nota da disciplina de matemática: '))
portugues = float(input('Digite a nota da disciplina de português: '))
ingles = float(input('Digita a nota da disciplina de inglês: '))
media = float(matematica + portugues + ingles) / 3

if ( media  >= 6 ): # Aqui poderia ter sido colocado um teste booleano de verdadeiro ou falso if (matematica >= 7 and portugues >= 7 and ingles >= 7), porém nao teriamos uma variável para exibir a media e armazenar aquele dado para manipular depois. Essa outra opção seria mais para exemplo do uso de boolan da aula.

    print('Aluno: ------', nome, '------')
    print('--------- MÉDIA 6 ---------')
    print('-------------- NOTAS --------------')
    print('Matemática: ', matematica)
    print('Português: ', portugues)
    print('Inglês: ', ingles)
    print('Aprovado com média ', f'{media:.2}')
else:
    print('Aluno: ------', nome, '------')
    print('--------- MÉDIA 6 ---------')
    print('---------- NOTAS -----------')
    print('Matemática: ', matematica)
    print('Português: ', portugues)
    print('Inglês: ', ingles)
    print('Aluno reprovado com média ', f'{media:.2}')