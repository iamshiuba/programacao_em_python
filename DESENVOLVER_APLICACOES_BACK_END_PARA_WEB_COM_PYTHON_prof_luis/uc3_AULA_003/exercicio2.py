idade = int(input("Informe a sua idade: "))

if idade >= 5 and idade <= 7:
    print("nadador infantil A")
elif idade >= 8 and idade <= 10:
    print("nadador infantil B")
elif idade >= 11 and idade <= 13:
    print("nadador juvenil A")
elif idade >= 14 and idade <= 17:
    print("nadador juvenil B")
elif idade >= 18:
    print("nadador adulto")
else:
    print("categoria inválida")