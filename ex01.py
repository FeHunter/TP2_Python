FIM = '.'

def entrar_caracteres():
    ''' faz leitura do input e retorna o primeiro caractere (char) '''
    char = ''
    try:
        char = input("Entre com um caractere: ")
    except:
        print("Error: Entrada Invalida")
    return char[0]
    
def exibir_caracteres(lista):
    ''' usar o for percorre a lista de caracteres e exibi-los '''
    for char in lista:
        print(char)

def contar_vogais(lista):
    ''' usar o for para percorre a lista e contar a vogais '''
    contagem = 0
    for char in lista:
        if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            contagem += 1
    print(f"Número de vogais {contagem}")


entrada = entrar_caracteres()
lista_char = []
while(entrada != FIM):
    lista_char.append(entrada)
    entrada = entrar_caracteres()
# exibir_caracteres(lista_char)
contar_vogais(lista_char)

# terminar o programa, mostra as vogais.