from cadastro import lista

def relatorio(lista):
    print("Relatório de Alunos")
    for aluno in lista:
        media = (aluno['nota1'] + aluno['nota2']) / 2
        print(f"Nome: {aluno['nomealuno']}, Nota1: {aluno['nota1']}, Nota2: {aluno['nota2']}, Média: {media:.2f}")
