def entrar_numero_inferior():
    ''' entrar com o numero de intervalo inferior '''
    while True:
        try:
            num = int(input("Digite o intervalo inferior: "))
            if (num > 0):
                break
        except:
            print("Erro: Valor inválido")
    return num

def entrar_numero_superior(num_inferior):
    ''' entrar com o numero de intervalo superior '''
    while True:
        try:
            num = int(input("Digite o intervalo superior: "))
            if (num > 0 and num > num_inferior):
                break
            else:
                print("Erro: O valor não pode ser inferior ao valor informado anteriomente")
        except:
            print("Erro: Valor inválido")
    return num

def lista_numeros(inferior, superior):
    ''' criar a lista com os numeros '''
    numeros = []
    for i in range(inferior, superior+1):
        numeros.append(i)
    return numeros

def filtra_primos(numeros):
    ''' Filtar apenas os numeros primos '''
    primos = []
    for num in numeros:
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primos.append(num)
    return primos

inferior = entrar_numero_inferior()
superior = entrar_numero_superior(inferior)
numeros = lista_numeros(inferior, superior)
primos = filtra_primos(numeros)
print(primos)

