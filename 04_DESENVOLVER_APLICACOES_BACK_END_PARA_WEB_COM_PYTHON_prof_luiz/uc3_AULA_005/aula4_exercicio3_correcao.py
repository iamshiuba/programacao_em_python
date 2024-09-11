total = 0.00

while True:
    codigo = int(input("Código do item: "))
    quant = int(input("Quantidade: "))

    preco = 0.00
    if codigo == 100:
        preco = 1.2
    elif codigo == 101:
        preco = 1.3
    elif codigo == 102:
        preco = 1.5
    elif codigo == 103:
        preco = 1.2
    elif codigo == 104:
        preco = 1.3
    elif codigo == 105:
        preco = 1.00
    else:
        print("Código inválido.")

    total += (preco * quant)
    r = input("Deseja continuar? (s/n): ")
    if r == 'n' or r == 'N':
        break
print(f"O valor total é: {total:.2f}")
