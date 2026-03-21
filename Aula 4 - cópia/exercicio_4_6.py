# ------ FUNCOES ------
def valida_int(pergunta, min, max):
    """
    Esta função valida a escolha do menu inicial

    Args:
        pergunta str: Opcão descrita do menu
        min int: menor número de opção  
        max int: maior número de opção  

    Returns:
        Número da opção do menu correspondente

    """
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def existeArquivo(nomeArquivo):
    """
    Verifica que o arquivo já existe no projeto

    Args:
        nomeArquivo str: Nome do arquivo
    
    Returns:
        A conclusão se existe ou não
    
    Raises:
        Aviso de que o arquivo já existe
    """
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(nomeArquivo):
    """
    Esta função cria um arquivo inexistente

    Args:
        nomeArquivo str: Recebe o nome do arquivo
    
    Returns:
        Cria o arquivo novo

    Raises:
        Printa mensagem de erro ao criar arquivo.
    """
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criacao do arquivo')
    else:
        print(f'Arquivo {nomeArquivo} criado com sucesso! \n')

def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
    """
    Esta função escreve o nome do jogo e video game no arquivo .txt

    Args:
        nomeArquivo str: Nome do arquivo a ser alterado
        nomeJogo str: Nome do jogo
        nomeVideogame str: Nome do video game

    Returns:
        Escreve no arquivo sem apagar algo existente

    Raises:
        Falha ao abrir o arquivo 
"""
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo e salvar os dados. ')
    else:
        a.write(f'{nomeJogo}; {nomeVideogame}\n')
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    """
    Lista todos os dados gravados no arquivo

    Args:
        nomeArquivo str: Nome do arquivo a ser listado

    Returns:
        Nome do Jogo seguido de nome do Nome do video game, linha por linha
    
    Raises:
        Erro ao rbrir o arquivo
    """
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao abrir o arquivo.')
    else:
        for linha in a:
            linha = linha.strip()
            nomeJogo, nomeVideogame = linha.split(';')
            print(f'Nome do jogo: {nomeJogo} | Plataforma: {nomeVideogame}')
    finally:
        a.close()




#----------- PROGRAMA PRINCIPAL ------------------
arquivo = 'games.txt' #nao é um arquivo ainda, é só uma string chamada .txt
if existeArquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivado inexistente')
    criarArquivo(arquivo)



while True:
    print("Menu")
    print('1 - Cadastrar novo item')
    print('2 - Listar cadastrados')
    print('3 - Sair')

    op = valida_int('Escolha uma opção desejada: ', 1, 3)
    if (op == 1): #novo item
        print('Opção de cadastrar novo item selecionada \n')
        nomeJogo = str(input('Nome do jogo: '))
        nomeVideogame = str(input('Nome do video game: '))
        cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
    elif (op == 2): #listar cadastros
        print('Opção de lista selecionada. \n')
        listarArquivo(arquivo)
    elif (op == 3):
        print('Encerrando o programa ... ')
        break    
