'''
array / vetor / conjunto / colecao == lista
'''
# Declarando um vetor
vetor = []
vetor.append(5)
vetor.append(7)
print(type(vetor))
print(vetor)

vetor.append(4.3)
vetor.append("Renato")
print(vetor)
print(f"Quantidade de elementos: {len(vetor)}")

# Primeira posição começa em 0
print(vetor[0])
