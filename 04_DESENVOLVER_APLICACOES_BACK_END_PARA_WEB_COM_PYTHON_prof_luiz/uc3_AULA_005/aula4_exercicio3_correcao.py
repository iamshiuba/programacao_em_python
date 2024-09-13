TOTAL = 0.00

while True:
    codigo = int(input("Código do item: "))
    quant = int(input("Quantidade: "))

    PRECO = 0.00
    if codigo == 100:
        PRECO = 1.2
    elif codigo == 101:
        PRECO = 1.3
    elif codigo == 102:
        PRECO = 1.5
    elif codigo == 103:
        PRECO = 1.2
    elif codigo == 104:
        PRECO = 1.3
    elif codigo == 105:
        PRECO = 1.00
    else:
        print("Código inválido.")

    TOTAL += (PRECO * quant)
    r = input("Deseja continuar? (s/n): ")
    if r == 'n' or r == 'N':
        break
print(f"O valor total é: {TOTAL:.2f}")
