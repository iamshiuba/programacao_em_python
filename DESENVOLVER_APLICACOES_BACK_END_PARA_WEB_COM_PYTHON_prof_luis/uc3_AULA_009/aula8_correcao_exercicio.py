from aula8_correcao_cadastro import incluirAluno
from aula8_correcao_relatorio import relatorioAluno

alunos = []

while True:
    print("Menu")
    print("1 - Cadastro")
    print("2 - Relatório")
    print("0 - Sair")
    op = int(input("Informe uma opção: "))
    if op == 0:
        break
    elif op == 1:
        incluirAluno(alunos)
    elif op == 2:
        relatorioAluno(alunos)

def situacao(m):
    if m >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def relatorioAluno(lista):
    for i in lista:
        media = (i['nota1'] + i['nota2']) / 2
        print(f"""{i["nomeAluno"]} - 
            {i["nota1"]:.2f} - 
            {i["nota2"]:.2f} - 
            {media:.2f} - 
            {situacao(media)}""")