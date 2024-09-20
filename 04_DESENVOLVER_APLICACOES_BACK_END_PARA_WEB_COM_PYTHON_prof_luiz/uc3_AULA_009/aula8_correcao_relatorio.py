def relatorioAluno(lista):
    for i in lista:
        media = (i['nota1'] + i['nota2']) / 2
        print(f"""{i["nomeAluno"]} - 
            {i["nota1"]:.2f} - 
            {i["nota2"]:.2f} - 
            {media:.2f} - 
            {situacao(media)}""")

def situacao(m):
    mensagem = ''
    if m >= 7:
        mensagem = "Aprovado"
    else:
        mensagem = "Reprovado"
    return mensagem
