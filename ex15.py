MIN_TAMANHO_NOME = 2
FIM = 'FIM'

def entrar_nome():
    ''' faz a leitura e validação se o nome digitado esta correta '''
    while True:
        nome = input("Entre com o nome: ")
        if len(nome) >= MIN_TAMANHO_NOME:
            break
        else:
            print("Erro: nome inválido")
    return nome

def entrar_nota(msg):
    ''' faz uma validação da nota digitada pelo usuário '''
    nota = 0
    while True:
        try:
            nota = float(input(msg))
            if (nota >= 0 and nota <= 10):
                break
            else:
                print("Erro: A nota deve esta 0 e 10")
        except ValueError as e:
            print(f"Erro: Nota inválida : {e}")
    return nota

def entrar_alunos():
    ''' faz a leitura do aluno: Nome, Nota1 e Nota2. Usando outras funções de entradas para uma validação mais clara '''
    turma = []
    nome = entrar_nome()
    while (nome.upper() != FIM):
        nota1 = entrar_nota("Entre com a nota 1: ")
        nota2 = entrar_nota("Entre com a nota 2: ")
        turma.append([nome, nota1, nota2])
        nome = entrar_nome()
    return turma

def calcular_medias(turma):
    ''' percorre a turma somando as notas para calcular a media '''
    medias = []
    for aluno in turma:
        soma_notas = aluno[1] + aluno[2]
        media = soma_notas / 2
        medias.append([aluno[0], media])
    return medias

def calcular_media_turma(turma, medias):
    ''' usar a array com as medias da turma para calcular a media geral '''
    somar_medias = 0
    for media in medias:
        somar_medias += media[1]
    media_geral = somar_medias / len(turma)
    print(f"\nMedia Geral da Turma: {media_geral}\n")

def exibir_resultados(medias):
    for media in medias:
        print(f"Nome: {media[0]} | Média: {media[1]} | Status: {exibir_aprovacao(media)}")

def exibir_aprovacao(media):
    ''' Recebe o valor da media e verificar se o aluno foi aprovado ou não '''
    if media[1] >= 6:
        return "Aprovado"
    else:
        return "Prova final"


turma = entrar_alunos()
medias = calcular_medias(turma)
print("\nResultados:")
exibir_resultados(medias)
calcular_media_turma(turma, medias)
