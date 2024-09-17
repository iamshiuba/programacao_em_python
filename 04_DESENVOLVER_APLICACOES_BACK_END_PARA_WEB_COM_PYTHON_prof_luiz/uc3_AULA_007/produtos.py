produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    categoria = input("Categoria: ")
    p = {}
    p['nomeprod'] = nome
    p['precoprod'] = preco
    p['catprod'] = categoria
    produtos.append(p)
    r = input("Deseja continuar? ")
    if r == 'n' or r == 'N':
        break

for i in produtos:
    print(f"{i['nomeprod']} - {i['precoprod']} - {i['catprod']}")