def fatorial (num):
    """
    Calcula o fatorial de um número inteiro não negativo

    Args:
        num (int): Número inteiro >= 0.
    
    Returns:
        int: Fatorial de num.
    
    Raises:
        ValueError: Se "num" for negativo.
    """
    resp = 1
    if num == 0:
        return resp

    for i in range (1, num + 1, 1):
        resp *= i
        print(f"i={i} resp={resp}")
    return resp

def check_num_positivo (num):
    """
    Esta função valida um número digitado se é maior que zero, se menor solicita ao usuário novo input até que seja validado

    Args:
        num (int): Número inteiro
    
    Returns:
        int: Número inteiro maior que zero

    """
    while num < 0:
        num = int(input("Número inválido, digite um número positivo: "))
    else:
        return num


x = int(input("Entre com um valor inteiro e positivo: "))
x = check_num_positivo(x)
print(fatorial(x))

