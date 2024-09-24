import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escola'
)

cursor = conexao.cursor()

sql = "select * from alunos order by nome"
cursor.execute(sql)
resultado = cursor.fetchall()
cursor.close()
conexao.close()

for r in resultado:
    print(r)