from cadastro import incluir
from relatorio import relatorio, lista

while True:
    print("Menu")
    print("1 - Cadastro")
    print("2 - Relatório")
    print("0 - Sair")
    op = int(input("Informe uma opção: "))
    if op == 0:
        break
    elif op == 1:
        incluir()
    elif op == 2:
        relatorio(lista)
