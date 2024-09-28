especificacoes = {
    100: {'descricao': 'Cachorro quente', 'preco': 1.20},
    101: {'descricao': 'Bauru simples', 'preco': 1.30},
    102: {'descricao': 'Bauru com ovo', 'preco': 1.50},
    103: {'descricao': 'Hambúrger', 'preco': 1.20},
    104: {'descricao': 'Cheeseburguer', 'preco': 1.30},
    105: {'descricao': 'Refrigerante', 'preco': 1.00}
}

total = 0

while True:
    codigo = int(input("Código do item: "))
    if codigo not in especificacoes:
        print("Código inválido")
        continue
    q = int(input("Quantidade: "))
    valor = especificacoes[codigo]['preco'] * q
    total += valor
    print(f"Valor total: {total:.2f}")
    r = input("Deseja continuar? (s/n) ")
    if r == 'n' or r == 'N':
        break
