print('Escolha do menu abaixo que tipo consumidor você é ')
print('1. Residencial')
print('2. Comercial')
print('3. Industrial')
opcao = int(input('Digite: '))
kw = float(input('Agora que sabemos que tipo de consumidor você é, informe o kW consumidos no último mês: '))

if ((opcao == 1) and (kw <= 500)):
        print(f'Seu gasto foi de: {kw * 0.40}')
elif ((opcao == 1) and (kw > 500)):
        print(f'Seu gasto foi de: {kw * 0.65}')
elif ((opcao == 2) and (kw <= 1000)):
        print(f'Seu gasto foi de: {kw * 0.55}')
elif ((opcao == 2) and (kw > 1000)):
        print(f'Seu gasto foi de: {kw * 0.60}')
elif ((opcao == 3) and (kw <= 5000)):
        print(f'Seu gasto foi de: {kw * 0.55}')
elif ((opcao == 3) and (kw > 5000)):
        print(f'Seu gasto foi de: {kw * 0.60}')        
