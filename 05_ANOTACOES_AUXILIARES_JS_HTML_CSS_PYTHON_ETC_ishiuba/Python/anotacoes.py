# No Python, temos tipos de dados primitivos que são usados para representar informações, como:
# - Number: um numero (ex: 1, 2, 3, etc.)
# - String: uma sequencia de caracteres (ex: "Olá", "Hello", "Bom dia", etc.)
# - Boolean: um valor lógico (ex: True ou False)
# - None: um valor nulo (ex: None)
# - List: uma lista de valores (ex: [1, 2, 3, etc.])
# - Tuple: um conjunto de valores (ex: (1, 2, 3, etc.))
# - Dict: um dicionário (ex: {"nome": "João", "idade": 25})

# Variáveis são "caixas" que podemos usar para armazenar valores.
# Para criar uma variável, podemos usar a palavra-chave "nome" seguida 
# do valor da variável e seus parâmetros.
# Exemplo:
nome = "João"

# A palavra-chave "nome" é usada para criar uma variável que pode ser alterada.
# Exemplo:
nome = "João"
nome = "Maria"

# A palavra-chave "None" é usada para criar uma variável que tem um valor nulo (ou vazio).
# Exemplo:
valor = None

# Funções são blocos de codigo que podem ser executados muitas vezes.
# Para criar uma função, podemos usar a palavra-chave "def" seguida do 
# nome da função e seus parâmetros.
# Exemplo:
def somar(a, b):
    return a + b

# A palavra-chave "def" é usada para criar uma função, 
# o que pode ser chamada com os parâmetros especificados.
# Exemplo:
somar(1, 2)

# A palavra-chave "return" é usada para retornar um valor da função que 
# foi chamada com os parâmetros especificados.
# Exemplo:
somar(1, 2)

# A palavra-chave "print" é usada para imprimir um valor na tela.
# Exemplo:
print(somar(1, 2))
print(somar(1,))

# A palavra-chave "if-elif-else" é usada para criar uma condição para um conjunto de valores 
# e executar um bloco de código dependente da condição.
# Exemplo:
if somar(1, 2) == 3:
    print("Sim")
elif somar(2, 2) == 4:
    print("Talvez")
else:
    print("Não")

# A palavra-chave "for" é usada para criar um loop para um conjunto de 
# valores e executar um bloco de código.
# Exemplo:
for i in range(10):
    print(i)
    print("Hello")
    print("Bom dia")

# A palavra-chave "while" é usada para criar um loop enquanto uma condição 
# for verdadeira e executar um bloco de código.
# Exemplo:
i = 0
while i < 10:
    print(i)
    i += 1
    print("Hello")
    print("Bom dia")

# A palavra-chave "break" é usada para interromper um loop.
# Exemplo:
for i in range(10):
    if i == 5:
        break
    print("Hello")
    print("Bom dia")

# A palavra-chave "continue" é usada para pular um loop e 
# continuar a partir do loop seguinte.
# Exemplo:
for i in range(10):
    if i == 5:
        continue
    print("Hello")
    print("Bom dia")

# A palavra-chave "pass" é usada para criar um loop vazio.
# Exemplo:
for i in range(10):
    if i == 5:
        pass
    print("Hello")
    print("Bom dia")

# A palavra-chave "class" é usada para criar uma classe.
# Para criar uma classe, podemos usar a palavra-chave "class" 
# seguida do nome da classe e seus parâmetros.
# Exemplo:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Ola, eu sou {self.nome} e tenho {self.idade} anos.")

# A palavra-chave "import" é usada para importar um arquivo.
# Exemplo:
import math
math.sqrt(4)

# A palavra-chave "as" é usada para renomear uma biblioteca.
# Exemplo:
import math as m
m.sqrt(4)

# A palavra-chave "from" é usada para importar apenas parte de um arquivo.
# Exemplo:
from math import sqrt
sqrt(4)

# A palavra-chave "try" é usada para tentar executar um bloco de código.
# Exemplo:
try:
    1 / 0
except ZeroDivisionError:
    print("Ocorreu um erro")
    print("ZeroDivisionError")

# A palavra-chave "except" é usada para capturar um erro.
# Exemplo:
try:
    1 / 0
except ZeroDivisionError: pass

# A palavra-chave "finally" é usada para executar um bloco de 
# código independente de ocorrer ou não um erro.
# Exemplo:
try:
    1 / 0
except ZeroDivisionError: pass
finally: pass

# A palavra-chave "raise" é usada para gerar um erro.
# Exemplo:
raise ZeroDivisionError

# A palavra-chave "global" é usada para tornar uma variável global.
# Exemplo:
global variavel

# A palavra-chave "nonlocal" é usada para tornar uma variável local.
# Exemplo:
nonlocal variavel

# A palavra-chave "lambda" é usada para criar uma função anonima.
# Exemplo:
# lambda x, y: x + y

# A palavra-chave "yield" é usada para criar um gerador.
# Exemplo:
def gerador():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

for i in gerador():
    print(i)
    if __name__ == "__main__":
        print("Hello, World!")

# A palavra-chave "with" é usada para criar um contexto.
# Exemplo:
with open("arquivo.txt", "r") as arquivo:
    print(arquivo.read())
