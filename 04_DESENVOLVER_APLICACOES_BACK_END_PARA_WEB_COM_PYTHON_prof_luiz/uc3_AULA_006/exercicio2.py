vetor = []

for i in range(6):
    numero = int(input(f"Informe o {i+1}º número: "))
    vetor.append(numero)

pares = 0
impares = []
for i in vetor:
    if i % 2 == 0:
        pares += 1
    else:
        impares.append(i)

print(f"A quantidade de números pares é {pares}")
print(f"A quantidade de números ímpares é {len(impares)}")
print(f"Os números ímpares são {impares}")
