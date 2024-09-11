vetor = []
while True:
    numero = int(input("Informe um número: "))
    if numero == 0:
        break
    vetor.append(numero)

soma = sum(vetor)
media = soma / len(vetor)

print(f"A soma é: {soma}")
print(f"A média é: {media:.2f}")
print(f"Quantidade de elementos: {len(vetor)}")
