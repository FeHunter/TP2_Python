FIM = 0

def entrar_numeros():
    ''' faz a leitura de numeros inteiros positivos '''
    while True:
        entrada = int(input("Digite o numero: "))
        if (entrada >= 0):    
            break
    return entrada

def ler_sequencia():
    ''' faz leitura da sequencia de numeros para contagem '''
    lista = []
    entrada = entrar_numeros()
    while entrada != FIM:
        lista.append(entrada)
        entrada = entrar_numeros()
    return lista

def calcular_fatorial(valor):
    ''' faz o calcular fatorial do numero informado '''
    if (valor <= 1):
        return 1
    return valor * calcular_fatorial(valor - 1)

def fatorial_sequencia(lista):
    ''' usar o for para percorrer a lista de numeros e faz a chamada do calcular fatorial '''
    for valor in lista:
        fatorial = calcular_fatorial(valor)
        print(f"O fatorial do {valor} é {fatorial}")


sequencia = ler_sequencia()
fatorial_sequencia(sequencia)