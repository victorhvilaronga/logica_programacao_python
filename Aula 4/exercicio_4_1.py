#escreva um algoritmo que calcule a média dos números pares de 1 até 100, implemente com for

#Neste código, sabendo que o intervalo é de 1 a 100, e sabendo que o primeiro numero par é 2, podemos assumir que ira comecar no 2.
#----------------
soma = 0
qtd = 0
media = 0
for i in range (2,101,2):
    qtd += 1
    soma += i
media = soma / qtd
print(media)

#Porém, se for em algo que nao sabemos o primeiro numero par, por exemplo em dados provenientes do usuario, teriamos que colocar um teste.
# --------------------
soma = 0
qtd = 0
media = 0
for i in range (1,101,1): #aqui comecamos trocando a condicao para andar de 1 em 1 e comecar no 0
    if (i % 2 == 0): #aqui fazemos o teste do iterador divido por 2 sendo 0 o resto, garantindo numero par
        qtd += 1
        soma += i
media = soma / qtd
print(media)