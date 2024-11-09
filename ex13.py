def impar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

def separar_impar_par(lista):
    ''' verificar se o numero e impar ou par e retorna as duas listas '''
    impar = []
    par = []
    for num in lista:
        if impar_par(num):
            par.append(num)
        else:
            impar.append(num)
    return impar, par


lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
impar, par = separar_impar_par(lista)
print(f"Números Impar: \n{impar}")
print(f"Números Par: \n{par}")