# agora eu quero 10 números inteiros e
# imprimir a soma

soma = 0

for i in range(10):
    print(i)
    j = i + 1
    numero = int(input(f"informe o {j}º número: "))
    soma += numero
print(f"A soma é: {soma}")

'''
UC1
for(var i = 1; i < 10; i++){
    comandos;
}
'''
