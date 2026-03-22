#Jokempo contra a maquina
#FUNÇÕES

def jogar (opcao, opcao_maquina):
    if opcao == 1:
        print(f'Você escolheu {opcao} - Pedra')
        opcao_maquina = random.randint(1,3)
        if opcao_maquina == 1:
            print(f'Maquina: Pedra! - Empate!')
            empates.append(1)
        elif opcao_maquina == 2:
            print(f'Máquina: Papel. - Você Perdeu!')
            derrotas.append(1)
        else:
            print(f'Máquina - Tesoura! - Você Ganhou!')
            vitorias.append(1)
    elif opcao == 2:
        print(f'Você escolheu {opcao} - Papel')
        opcao_maquina = random.randint(1,3)
        if opcao_maquina == 1:
            print(f'Maquina: Pedra! - Você Ganhou!')
            vitorias.append(1)
        elif opcao_maquina == 2:
            print(f'Máquina: Papel. - Empate!')
            empates.append(1)
        else:
            print(f'Máquina - Tesoura! - Você perdeu!')
            derrotas.append(1)
    elif opcao == 3:
        print(f'Você escolheu {opcao} - Tesoura')
        opcao_maquina = random.randint(1,3)
        if opcao_maquina == 1:
            print(f'Maquina: Pedra! - Você perdeu!')
            derrotas.append(1)
        elif opcao_maquina == 2:
            print(f'Máquina: Papel. - Você ganhou!')
            vitorias.append(1)
        else:
            print(f'Máquina - Tesoura! - Empate!')
            empates.append(1)
        
import random

print('-' * 10, 'Bem vindo ao Jovempô', '-' * 10)

vitorias = []
derrotas = []
empates = []

while True:
    print('\n1 - Pedra' '\n2 - Papel \n' '3 - Tesoura' '\n 4 - Sair')
    opcao = int(input('Digite a opção:'))
    if opcao == 1 or opcao == 2 or opcao == 3:
        opcao_maquina = random.randint(1,3)
        jogar(opcao, opcao_maquina)
    else:
        print(f'Vitorias: {vitorias.count(1)}, Derrotas: {derrotas.count(1)}, Empates: {empates.count(1)}')
        print('Encerrando jogo...')
        break



    