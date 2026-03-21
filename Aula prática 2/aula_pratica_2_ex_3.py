km_rodado = float(input('Insira aqui os KM rodados com o carro e aperte enter: '))
dias_alugado = int(input('Insira aqui os dias de aluguel do carro e aperte enter: '))

valor_total_aluguel = km_rodado * 0.15 + dias_alugado * 60

print(f'Voce percorreu {km_rodado} kilmetros e usou por {dias_alugado} dias')
print(f'O valor final a ser pago pelo aluguel do carro é: R$ {valor_total_aluguel}')