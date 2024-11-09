def entrar_numero():
    ''' faz a leitura da entrada e previne erros com try '''
    try:
        return int(input("Digite um numero para se esta na lista: "))
    except:
        print("Erro: valor digitado inválido")

def encontrar_numero(num_digitado, lista):
    ''' percorre a array/lista de numeros e verifica se o numeros digitado foi encontrado '''
    posicao = -1
    for i in range(0, len(lista)):
        if lista[i] == num_digitado:
            posicao = i
    if (posicao == -1):
        print(f"Valor não encontrado: {posicao}")
    else:
        print(f"Valor encontrado, posição na array {posicao}")

numeros = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
num_digitado = entrar_numero()
encontrar_numero(num_digitado, numeros)
