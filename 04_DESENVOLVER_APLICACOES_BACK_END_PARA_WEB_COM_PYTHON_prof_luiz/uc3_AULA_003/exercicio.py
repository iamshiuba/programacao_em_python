altura = float(input("Informe a altura: "))
sexo = input("Informe o sexo (M/F): ")

# = artribui valor == verifica igualdade
if sexo == "M":
    pesoIdeal = (72.7 * altura) - 58
    print(f"O peso ideal masculino é de {pesoIdeal:.3f} kG")
elif sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"O peso ideal feminino é de {pesoIdeal:.3f} kG")
else:
    print("Sexo inválido")
    exit()
