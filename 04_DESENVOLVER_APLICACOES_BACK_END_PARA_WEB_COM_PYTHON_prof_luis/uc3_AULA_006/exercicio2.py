vetor = []

for i in range(6):
    numero = int(input("Informe um número: "))
    vetor.append(numero)

QUANT_PARES = 0
QUANT_IMPARES = 0

for elemento in vetor:
    if elemento % 2 == 0:
        QUANT_PARES = QUANT_PARES + 1
    else:
        QUANT_IMPARES = QUANT_IMPARES + 1
        print(elemento)
print(f"Quantidade de números pares: {QUANT_PARES}")
print(f"Quantidade de números ímpares: {QUANT_IMPARES}")
