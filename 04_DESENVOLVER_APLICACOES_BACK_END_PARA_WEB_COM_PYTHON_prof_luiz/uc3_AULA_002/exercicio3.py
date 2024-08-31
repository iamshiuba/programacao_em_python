raio=float(input("digite o valor do raio: "))
altura=float(input("digite o valor da altura: "))

#Volume=3.14159*raio*raio*altura
import math
Volume=math.pi*math.pow(raio,2)*altura

print(f"O volume é: {Volume}")