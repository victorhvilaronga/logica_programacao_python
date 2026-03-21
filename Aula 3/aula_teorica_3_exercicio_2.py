print('Olá! Bem vindo à nossa loja!')
print('Abaixo, selecione o produto que seja comprar (digite o número e aperte enter): ')
print('1. Maçã')
print('2. Laranja')
print('3. Banana')

fruta = int(input('Opção número: '))

if (fruta !=  1 and fruta != 2 and fruta != 3):
    print('Produto inexistente.')
    quit()
else:
    print(' ')

quantidade = int(input('Agora, digite a quantidade em unidades: '))

maca = float(2.30)
laranja = float(3.60)
banana = float(1.85)

if (fruta == 1):
    fruta = maca * quantidade
    print('O valor total da compra de maçãs (unitário: R$', maca, ') ' 'é: R$', fruta)
elif (fruta == 2):
    fruta = laranja * quantidade
    print('O valor total da compra é:  R$', fruta)
else:
    fruta = banana * quantidade
    print('O valor total da compra é: R$', fruta)
       



