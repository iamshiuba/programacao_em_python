vetor = []

for i in range(6):
    numero = int(input("Informe o número: "))
    vetor.append(numero)

PARES = 0
impares = []

for i in vetor:
    if i % 2 == 0:
        PARES += 1
    else:
        impares.append(i)

print(f"A quantidade de números PARES é {PARES}")
print(f"A quantidade de números ímpares é {len(impares)}")
print(f"Os números ímpares são {impares}")
