produtos = []

while True:
    nome = input("Nome do produto: ")
    preco = int(input('Preço: '))
    produtos.append(nome)
    produtos.append(preco)
    r = input("Deseja continuar? ")
    if r == 'n' or r == 'N':
        break

for i in produtos:
    print(i)
