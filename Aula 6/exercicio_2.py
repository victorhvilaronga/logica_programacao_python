#Conta as vogais e as imprime em cada palavras de uma tupla
tupla_teste = ('abacaxi','mamao','laranja','banana','melancia','melao','morango','manga','tomate','pessego')

for palavra in tupla_teste:
    print(f'\nPalavra: {palavra.upper()}. Vogais: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

