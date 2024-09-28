# Um programa que ao ler a idade de uma pessoa, o programa informa se ela é
# menor de idade.

idade = int(input("Informe a idade: "))

if idade < 18:
    print("Menor de idade")
else:
    print("Maior de idade")