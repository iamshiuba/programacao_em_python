lista = []

def incluir():
    print("Acessando a função incluir")
    while True:
        nome = input("Informe o nome do aluno: ")
        nota1 = float(input("Coloque sua primeira nota: "))
        nota2 = float(input("Coloque sua segunda nota: "))
        aluno = {'nomealuno': nome, 'nota1': nota1, 'nota2': nota2}
        lista.append(aluno)
        r = input("Deseja continuar? (s/n) ")
        if r == 'n' or r == 'N':
            break
