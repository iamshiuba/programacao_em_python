VALOR = []
SOMA = 0
CONTADOR = 0

while True:
    produto = float(input("Valor: "))
    r = input("Deseja continuar? (s/n) ")
    VALOR.append(produto)
    if r == 'n' or r == 'N':
        break

for i in VALOR:
    if i < 50:
        CONTADOR += 1
    if i > 100:
        SOMA += i

print(f"Quantidade de produtos com pre o inferior a R$ 50,00: {CONTADOR}")
print(f"M dia dos pre os dos produtos com pre o superior a R$ 100,00: {SOMA / len([i for i in VALOR if i > 100]):.2f}")
