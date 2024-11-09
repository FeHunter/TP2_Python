def menor_numero(lista):
    ''' retorna o valor minimo da lista '''
    return min(lista)

def maior_numero(lista):
    ''' retorna o valor maximo da lista '''
    return max(lista)

def somar_numeros(lista):
    ''' retorna a soma dos numeros da lsita '''
    soma = 0
    for num in lista:
        soma += num
    return soma

def media_numeros(soma, lista):
    ''' calcular a media dos numeros da lista '''
    return soma / len(lista)


lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
menor = menor_numero(lista)
maior = maior_numero(lista)
soma = somar_numeros(lista)
media = media_numeros(soma, lista)
print(f"Menor número: {menor} \nMaior número: {maior} \nSoma: {soma} \nMédia: {media}")