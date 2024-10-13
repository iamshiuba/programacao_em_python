# Ler indeterminados números
# A condição é o usuário responder "n"
# para a pergunta "Deseja continuar?" (s/n)

soma = 0

while True:
    numero = int(input("Informe um número: "))
    r = input("Deseja continuar? (s/n) ")
    soma = soma + numero
    if r == 'n' or r == 'N':
        break

print(f"A soma é: {soma}")
