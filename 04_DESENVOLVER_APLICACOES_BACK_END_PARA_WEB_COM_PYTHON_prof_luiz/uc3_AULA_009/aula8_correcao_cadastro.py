def incluir(lista):
        nome = input("Informe o nome do aluno: ")
        nota1 = float(input("Coloque sua primeira nota: "))
        nota2 = float(input("Coloque sua segunda nota: "))
        a = {}
        a["nomeAluno"] = nome
        a["nota1"] = nota1
        a["nota2"] = nota2
        lista.append(a)
        r = input("Deseja continuar? (s/n) ")
        if r == 'n' or r == 'N':
            break
