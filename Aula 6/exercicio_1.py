#Verifica nota maxima, e testa varias funções com lista

notas = [9,7,7,10,10,10,3,9,6,6,2]
print(notas.count(7))
print(max(notas))
print(notas.count(max(notas)))
print(f'A maior nota da lista é: {max(notas)} e ela aparece {notas.count(max(notas))} vezes')
notas.sort()
print(notas)
sum(notas)