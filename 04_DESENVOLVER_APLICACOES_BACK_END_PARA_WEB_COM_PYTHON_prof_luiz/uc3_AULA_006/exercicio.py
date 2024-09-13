vetor = []
for i in range(15):
    num = int(input(f"Informe o {i+1}º número: "))
    vetor.append(num * 3)

print("Vetor após os cálculos: ")
for i, num in enumerate(vetor, start=1):
    print(f"{i}º número: {num}")
