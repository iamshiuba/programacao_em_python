VALOR = []

while True:
    preco = float(input("Informe o preço: "))
    VALOR.append(preco)
    r = input("Deseja continuar? (s/n) ")
    if r == "n" or r == "N":
        break

QUANT_INF50 = 0
SOMA_SUP100 = 0
QUANT_SUP100 = 0

for i in VALOR:
    if i < 50:
        QUANT_INF50 += 1
    elif i > 100:
        SOMA_SUP100 += i
        QUANT_SUP100 += 1

print(f"Quantidade de produtos com preço inferior a R$ 50,00: {QUANT_INF50}")
MEDIA_SUP100 = SOMA_SUP100 / QUANT_SUP100
print(f"Média dos preços superiores a R$ 100: {MEDIA_SUP100:.2f}")