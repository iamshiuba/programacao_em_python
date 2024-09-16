listaProduto = []
listaPreco = []

while True:
    nome = input("Nome do produto: ")
    preco = input("Preço: ")
    listaProduto.append(nome)
    listaPreco.append(preco)
    r = input("Deseja continuar? ")
    if r == 'n' or r == 'n':
        break

for n in listaProduto:
    print(n)

for i in listaPreco:
    print(i)
