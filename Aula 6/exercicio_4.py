import datetime
cadastros = {'nome':[], 'ano_nasc':[], 'sexo':[]}
idades = []
sexo_fem = []
ano_atual = int(datetime.date.today().year)
qtd_cadastros = 0

while True:
    print('-' * 10, 'MENU DE CADASTROS', '-' * 10 )
    print('\n1 - Cadastrar paciente. \n' '2 - Sair \n')
    opcao = int(input('Digite a opcao desejada: '))
    if opcao == 1:
        for i in range(3):
            nome = input('Digite o nome: ')
            ano_nasc = input('Digite o ano de nascimento: ')
            sexo = input('Digite o sexo: ')
            cadastros['nome'].append(nome)
            cadastros['ano_nasc'].append(ano_nasc)
            cadastros['sexo'].append(sexo)
            idades.append(ano_atual - int(ano_nasc))
            if sexo == 'F' and ((ano_atual - int(ano_nasc)) < 30):
                sexo_fem.append(1)
            qtd_cadastros += 1
    else:
        print(f'Quantidade de cadastros: {qtd_cadastros}')
        print(cadastros)
        print(f'Média de idades: {(sum(idades) / len(idades))}')
        print(f'A lista possui {sexo_fem.count(1)} mulheres cadastradas com menos de 30 anos')
        print('Programa encerrado...')
        break