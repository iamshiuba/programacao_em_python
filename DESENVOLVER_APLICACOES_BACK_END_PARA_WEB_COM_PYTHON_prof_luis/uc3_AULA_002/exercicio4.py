ddn = int(input(f"Data de nascimento: "))
ano = int(input("Ano atual: "))

idade=ano-ddn
idade=idade*12
idade=idade*31-(5*30)+8
# Essa é a maneira mais interessante que consegui para chegar
# a um resultado próximo ao da calculadora. Mas se quiser algo simples,
# retire tudo depois de idade*31. Outra alternativa é idade*30.

# Uma alternativa sugerida pelo professor
# idade=meses*30

print(f"""Idade: {idade}
      Idade em meses:{idade*12}
      Idade em dias: {idade*31-(5*30)+8}
      """)

