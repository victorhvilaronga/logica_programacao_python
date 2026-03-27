#exercício para criar um menu de compras simplificado. Eu implementei a mais, porém deve existir uma maneira de trazer os mesmos dados com menos linhas de código
x = 0
qtd = 0
opcao = 0
total = 0
qtd1total = 0
qtd2total = 0
qtd3total = 0
qtd4total = 0
qtd1 = 0
qtd2 = 0
qtd3 = 0
qtd4 = 0

while x <= 5:
    print("----- MENU PRINCIPAL ------")
    print("1 - Coxinha R$ 5,00")
    print("2 - Pastel R$ 7,00")
    print("3 - Café R$ 4,00")
    print("4 - Suco R$ 6,00")
    print("5 - Finalizar compra e pagar")
    opcao = int(input("Escolha a opção desejada: "))
    if opcao == 1:
        qtd1 = int(input("Qual a quantidade de coxinhas?: "))
        qtd1total += qtd1
        total += qtd1 * 5.00
        print(f'"Você comprou {qtd1} nesta compra e ao todo são {qtd1total}, total compra até o momento: {total}"')
    elif opcao == 2:
        qtd2 = int(input("Qual a quantidade de Pateis?: "))
        qtd2total += qtd2
        total += qtd2 * 7.00
        print(f'"Você comprou {qtd2} nesta compra e ao todo são {qtd2total}, total compra até o momento: {total}"')
    elif opcao == 3:
        qtd3 = int(input("Qual a quantidade de Café?: "))
        qtd3total += qtd3
        total += qtd3 * 4.00
        print(f'"Você comprou {qtd3} nesta compra e ao todo são {qtd3total}, total compra até o momento: {total}"')
    elif opcao == 4:
        qtd4 = int(input("Qual a quantidade de Suco?: "))
        qtd4total += qtd4
        total += qtd4 * 6.00
        print(f'"Você comprou {qtd4} nesta compra e ao todo são {qtd4total}, total compra até o momento: {total}"')
    else:
        print(f'"Você comprou {qtd1total} coxinha(s), {qtd2total} de Pastel(eis), {qtd3total} Café(s) e {qtd4total} de Suco(s), totalizando R${total}"')
        print("Compra finalizada")
        x = 6
        


