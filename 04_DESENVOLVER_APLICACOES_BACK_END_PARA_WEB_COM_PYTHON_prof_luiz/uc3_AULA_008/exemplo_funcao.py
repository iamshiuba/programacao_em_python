from funcoes import relatorio
produtos = []

def incluir():
    print("Acessando a função incluir")
    while True:
        nome = input("Informe o nome do produto: ")
        preco = float(input("Preço: "))
        cat = input("Categoria: ")
        p = {}
        p['nomeprod'] = nome
        p['precoprod'] = preco
        p['catprod'] = cat
        produtos.append(p)
        r = input("Deseja continuar? (s/n)")
        if r == 'n' or r == 'N':
            break


while True:
    print("Menu")
    print("1 - Cadastro")
    print("2 - Relatório")
    print("0 - Sair")
    op = int(input("Informe uma opção: "))
    if op == 0:
        break
    elif op == 1:
        incluir()
    elif op == 2:
        relatorio(produtos)
