produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = int(input("Preço: "))
    produtos.append(nome, preco)
    r = input("Deseja continuar? ")
    if r == 'n' or r == 'N':
        break

for i in produtos:
    print(f'{i[0]} - {i[1]}')