print('Bem vindo a nossa loja online!')
preco = float(input('Digite o preço do produto e aperte enter: '))
descontopercent = float(input('Digite o desconto a ser aplicado e aperte enter: '))
valordesconto = preco * (descontopercent/100)
valor_final = preco - (preco * (descontopercent/100)) 


print(f'o valor do produto é de {preco} e o valor do desconto é de {descontopercent}%')
print(f'Seu produto agora custa: R$ {valor_final} E voce teve um desconto de:  R$ {valordesconto}')