produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = int(input("Preço: "))
    categoria = input("Categoria: ")
    produtos.append([nome, preco, categoria])
    r = input("Deseja continuar? ")
    if r == 'n' or r == 'N':
        break

for i in produtos:
    print(f'Produto: {i[0]}, preço: {i[1]}, categoria: {i[2]}')
