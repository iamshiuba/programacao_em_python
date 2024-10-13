import mysql.connector

try:
    conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escola'
    )

    cursor = conexao.cursor()

    nome = input("Informe o nome: ")
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))

    sql = "insert into alunos (nome, nota1, nota2) values (%s, %s, %s)"
    info = (nome, nota1, nota2)
    cursor.execute(sql, info)
    conexao.commit()

    cursor.close()
    conexao.close()
except:
    print("Erro ao cadastrar!")