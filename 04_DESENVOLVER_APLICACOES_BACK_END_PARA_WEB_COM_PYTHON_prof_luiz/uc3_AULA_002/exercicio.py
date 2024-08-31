valor_horaul = float(input("digite o valor da hora aula: "))
horas = float(input("digite o total de horas dadas no mês: "))
descontos = float(input("digite o valor de descontos: "))

salario = valor_horaul * horas - descontos

print(f'Seu salário é de: R$ {salario:.2f}')