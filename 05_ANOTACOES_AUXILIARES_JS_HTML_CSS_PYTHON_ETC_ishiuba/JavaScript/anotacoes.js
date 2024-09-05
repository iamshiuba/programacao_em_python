// No JavaScript, temos tipos de dados primitivos que são usados para representar informações
// Os tipos de dados primitivos são:
// - Number: um número (ex: 1, 2, 3, etc.)
// - String: uma sequência de caracteres (ex: "Olá", "Hello", "Bom dia", etc.)
// - Boolean: um valor lógico (ex: true ou false)
// - Null: um valor nulo (ex: null)
// - Undefined: um valor indefinido (ex: undefined)

// Variáveis são "caixas" que podemos usar para armazenar valores.
// Para criar uma variável, podemos usar a palavra-chave "let", "const" ou "var".
// Exemplo: 
let nome = "João";

// A palavra-chave "let" é usada para criar uma variável que pode ser alterada.
// Exemplo: 
let idade = 25; idade = 30; // idade agora vale 30

// A palavra-chave "const" é usada para criar uma variável que não pode ser alterada.
// Exemplo: 
const PI = 3.14; PI = 4; // Erro! PI é uma constante e não pode ser alterada.

// A palavra-chave "var" é usada para criar uma variável que pode ser alterada, mas tem um escopo mais amplo do que "let" e "const".
// Exemplo: 
var nome = "João"; // nome é uma variável global e pode ser acessada em qualquer lugar do código

// Funções são blocos de código que podem ser executados muitas vezes.
// Para criar uma função, podemos usar a palavra-chave "function".
// Exemplo:
function somar(a, b) {
  return a + b;
}

// Funções podem possuir parâmetros, que são valores passados para a função
// quando ela é chamada. No exemplo acima, "a" e "b" são parâmetros da função
// "somar".

// Funções podem também possuir um valor de retorno, que é o valor que a
// função retorna quando é chamada. No exemplo acima, o valor de retorno da
// função "somar" será a soma de "a" e "b".

// Funções podem ser chamadas quantas vezes forem necessárias, e elas
// vão executar o código novamente. Isso é muito útil quando precisamos
// executar uma mesma tarefa muitas vezes em um programa.

// Exemplo: uma função que calcula o valor de uma conta pode ser chamada
// muitas vezes em um programa, para calcular o valor de diferentes contas.
function calcularConta(valor) {
  return valor * 1.10;
}

// Exemplo: uma função que verifica se um número é par ou ímpar pode ser
// chamada muitas vezes em um programa, para verificar se diferentes números
// são pares ou ímpares.
function numeroPar(numero) {
  return numero % 2 === 0;
}

// Existem ainda outros tipos de dados no JavaScript, como:
// - Array: uma lista de valores (ex: [1, 2, 3, etc.]).
//   Arrays no JavaScript são heterogêneos, ou seja, podem conter valores de
//   diferentes tipos, como números, strings, objetos, etc.

//   Arrays no JavaScript têm métodos e propriedades úteis, como o método
//   "push" que adiciona um novo elemento no final do array, o método "pop"
//   que remove o último elemento do array e retorna o valor removido, o
//   método "indexOf" que retorna o índice do elemento no array ou -1 se o
//   elemento não existir, entre outros.

// Exemplos de como podemos usar arrays no JavaScript:
const numeros = [1, 2, 3];
const nomes = ["João", "Maria", "Pedro"];
const objetos = [
  {nome: "João", idade: 25},
  {nome: "Maria", idade: 30},
  {nome: "Pedro", idade: 35}
];

// Adicionando um elemento no final do array
numeros.push(4);
console.log(numeros); // [1, 2, 3, 4]

// Removendo o último elemento do array e retornando o valor removido
const elementoRemovido = numeros.pop();
console.log(elementoRemovido); // 4

// Verificando se o elemento existe no array
const existe = nomes.indexOf("João");
console.log(existe); // 0

// Verificando se o elemento existe no array e retornando -1 se não existir
const naoExiste = nomes.indexOf("Ana");
console.log(naoExiste); // -1

// - Object: um conjunto de chave-valor (ex: {nome: "João", idade: 25}).
//   Objetos no JavaScript são como dicionários, onde as chaves são strings e
//   os valores podem ser de qualquer tipo, como números, strings, objetos,
//   etc.

//   Objetos no JavaScript têm métodos e propriedades úteis, como o método
//   "hasOwnProperty" que retorna true se o objeto tem uma propriedade com o
//   nome especificado, o método "keys" que retorna uma lista de todas as
//   chaves do objeto, entre outros.

// Exemplos de como podemos usar objetos no JavaScript:
const pessoa = {
    nome: "João",
    idade: 25
};

console.log(pessoa.nome); // João
console.log(pessoa.idade); // 25

const chave = "nome";
console.log(pessoa[chave]); // João

if (pessoa.hasOwnProperty("nome")) {
    console.log("A pessoa tem o nome!");
}

const todasAsChaves = Object.keys(pessoa);
console.log(todasAsChaves); // [ "nome", "idade" ]

// - Symbol: um tipo de dado único, que pode ser usado como chave em um
//   objeto. Symbols são criados com a função "Symbol" e são únicos, ou seja,
//   nunca existirão dois symbols iguais.

//   Symbols são úteis quando você precisa criar uma chave única para um
//   objeto, como por exemplo, quando você precisa criar um cache de
//   objetos.

const simbolo1 = Symbol();
const simbolo2 = Symbol();

console.log(simbolo1 === simbolo2); // false

const objeto = {
  [simbolo1]: "valor 1",
  [simbolo2]: "valor 2"
};

console.log(objeto[simbolo1]); // valor 1
console.log(objeto[simbolo2]); // valor 2

// - BigInt: um tipo de dado numérico que pode representar valores muito
//   grandes. BigInts são criados com a função "BigInt" e são usados para
//   representar valores que são muito grandes para serem representados por
//   Number.

//   BigInts são úteis quando você precisa representar valores muito
//   grandes para serem representados por Number.

const bigInt = BigInt(1234567890123456789012345678901234567890);
console.log(bigInt); // 1234567890123456789012345678901234567890n

// Existem ainda operadores que podem ser usados para fazer operações com
// os valores, como por exemplo:

// Aritméticos:
const soma = 1 + 2;
console.log(soma); // 3

const subtracao = 5 - 3;
console.log(subtracao); // 2

const multiplicacao = 5 * 2;
console.log(multiplicacao); // 10

const divisao = 10 / 2;
console.log(divisao); // 5

const resto = 7 % 3;
console.log(resto); // 1

// Comparativos:
const igualdade = 5 == 5;
console.log(igualdade); // true

const diferente = 5 != 3;
console.log(diferente); // true

const igualdadeEstrita = 5 === "5";
console.log(igualdadeEstrita); // false

const diferenteEstrito = 5 !== "5";
console.log(diferenteEstrito); // true

const menor = 5 < 3;
console.log(menor); // false

const maior = 5 > 3;
console.log(maior); // true

const menorOuIgual = 5 <= 5;
console.log(menorOuIgual); // true

const maiorOuIgual = 5 >= 5;
console.log(maiorOuIgual); // true

// Lógicos:
const and = true && true;
console.log(and); // true

const or = true || false;
console.log(or); // true

const not = !true;
console.log(not); // false

// Atribuição:
let valor = 5;
valor += 2;
console.log(valor); // 7

valor -= 3;
console.log(valor); // 4

valor *= 2;
console.log(valor); // 8

valor /= 2;
console.log(valor); // 4

valor %= 3;
console.log(valor); // 1

// Existem ainda ainda outros recursos, como:
// - Loops: for, while, do-while

const lista = [1, 2, 3, 4, 5];
for (let i = 0; i < lista.length; i++) {
    console.log(lista[i]);
}

let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}

let j = 0;
do {
    console.log(j);
    j++;
} while (j < 5);

// - Condicionais: if, else, switch

const cor = 'verde';
if (cor === 'verde') {
    console.log('A cor é' + cor);
} else {
    console.log('A cor não é' + cor);
}

switch (cor) {
    case 'verde':
        console.log('A cor é verde');
        break;
    case 'amarelo':
        console.log('A cor é amarelo');
        break;
    default:
        console.log('A cor não é verde nem amarelo');
        break;
}

// - Funções de array: map, filter, reduce, etc.

const numeros = [1, 2, 3, 4, 5];

const dobro = numeros.map(numero => numero * 2);
console.log(dobro); // [2, 4, 6, 8, 10]

const numerosPares = numeros.filter(numero => numero % 2 === 0);
console.log(numerosPares); // [2, 4]

const soma = numeros.reduce((acumulador, atual) => acumulador + atual, 0);
console.log(soma); // 15
