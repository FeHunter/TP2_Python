def entrar_op():
    ''' faz a leitura da operação e garante que o valor digitado esteja correto '''
    entrada = ""
    while True:
        entrada = input("[+] [-] [*] [/] ) \nEscolhar a operação: ")
        if (entrada == '+' or entrada == '-' or entrada == '*' or entrada == '/'):
            break
    return entrada
        
def tabuada_multi(op):
    ''' verificar a operação para gerar a tabuada '''
    if op == "+":
        for i in range(1, 11):
            for j in range(1, 11):
                re = i + j
                print(f"{i} + {j} = {re}")
    
    if op == "-":
        for i in range(1, 11):
            for j in range(1, 11):
                re = i - j
                print(f"{i} - {j} = {re}")
                
    if op == "*":
        for i in range(1, 11):
            for j in range(1, 11):
                re = i * j
                print(f"{i} x {j} = {re}")
                
    if op == "/":
        for i in range(1, 11):
            for j in range(1, 11):
                re = i / j
                print(f"{i} / {j} = {re}")

op = entrar_op()
tabuada_multi(op)