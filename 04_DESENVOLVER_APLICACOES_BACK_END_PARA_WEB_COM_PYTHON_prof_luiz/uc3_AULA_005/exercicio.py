vetor = []
while True:
    numero = int(input("Informe um número: "))
    vetor.append(numero)
    if numero == 0:
        break

soma = 0
for i in vetor:
    soma += i

media = soma / len(vetor)
print(f"A soma dos elementos: {soma}")
print(f"A média dos elementos: {media}")
print(f"Número de elementos: {len(vetor)}")
