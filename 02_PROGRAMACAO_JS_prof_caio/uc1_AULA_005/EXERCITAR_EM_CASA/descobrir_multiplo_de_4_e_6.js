// Crie um algoritmo que determine se um número é divisível por 4 e 6 ao mesmo tempo.
// 1 - Você deve definir uma constante chamada valor;
// 2 - Será necessária um if e também um else;
// 3 - O operador % que é o operador de RESTO será necessário.
// 4 - O operador === que é o operador IDÊNTICO será necessário.
// 6 - O operador && que é o operador "E" será necessário.
// 7 - Caso a constante valor seja divisível por 4 e 6 ao mesmo tempo imprimir a saída com console.log("O número é divisível por 4 e 6 ao mesmo tempo");
// 8 - Caso contrário imprimir a saída com console.log("O número não é divisível por 4 e 6 ao mesmo tempo");
// 9 - No final executar com node 'nome_do_arquivo.js' para vermos a execução no terminal

const valor = 24
if (valor % 4 === 0 && valor % 6 ===0){
    console.log("O número é divisível por 4 e 6 ao mesmo tempo");   
}
else{
console.log("O número não é divisível por 4 e 6 ao mesmo tempo");
}




