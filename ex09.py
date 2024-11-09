def ler_numeros():
    ''' ler sequencia de numeros terminada por zero(0) '''
    numeros = []
    while True:
        num = int(input("(0) Para finalizar \nDigite o numero: "))
        if (num == 0):
            break
        numeros.append(num)
    return numeros

numeros = ler_numeros()
numeros_invertidos = sorted(numeros, reverse=True)
print(numeros_invertidos)