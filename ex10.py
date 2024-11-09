def ler_numeros():
    ''' ler sequencia de numeros terminada por zero(0) '''
    numeros = []
    while True:
        num = int(input("(0) Para finalizar \nDigite o numero: "))
        if (num == 0):
            break
        numeros.append(num)
    return numeros

def calcular_media(lista):
    ''' calcular a media dos numeros da lista '''
    soma = 0
    for num in lista:
        soma += num
    return soma / len(lista)

def filtra_maiores(lista, media):
    ''' percorre a lista e adicionar os numeros maiores ou igual a media em uma nova lista '''
    lista_filtrada = []
    for num in lista:
        if num >= media:
            lista_filtrada.append(num)
    return lista_filtrada


lista = ler_numeros()
media = calcular_media(lista)
lista_filtrada = filtra_maiores(lista, media)
print(lista_filtrada)