def entrar_valor():
    ''' ler entrada e garante que os valores sejam maior ou igual a zero e não quebra '''
    while True:
        try:
            valor = int(input("Digite um valor Inteiro: "))
            if valor >= 0:
                return valor
            else:
                print("O valor deve ser maior ou igual a zero")
        except:
            print("Erro: Valor informado inválido")
            

valor = entrar_valor()
print(f"Valor digitado: {valor}")