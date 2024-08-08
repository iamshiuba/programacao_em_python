// Escreva um algoritmo que verifique se um número é par ou impar, porém só pode imprimir o valor par se for maior que 10.
// 1 - Você deve definir uma constante chamada valor.
// 2 - Será necessária "uma condicional aninhada dentro de outra condicional e um else".
// 3 - O operador % que é o operador de RESTO será necessário.
// 4 - O operador === que é o operador IDÊNTICO será necessário.
// 6 - O operador de > que é o operador de MAIOR será necessário.
// 7 - Caso a constante valor seja par e maior que 10, imprimir a saída com console.log("O valor é par").
// 8 - Caso contrário imprimir a saída com console.log("O valor é impar").
// 9 - OBS: Usar um único IF com o operador && verificando o resto e o valor maior que 10 ao mesmo tempo vai levar para uma solução errada, tenha cuidado e faça as checagens dessas duas condições de forma independente ou seja separadas.
// 10 - No final executar com node 'nome_do_arquivo.js' para vermos a execução no terminal

const valor = 13;
if (valor % 2 === 0) {
  if (valor > 10) console.log("o valor é par!");
} else {
  console.log("o valor é impar!");
}
