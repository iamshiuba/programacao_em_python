// 1 - Faça um algoritmo que verifique se a pessoa tem idade suficiente para dirigir.
// 2 - Apenas se a pessoa tiver 18 anos ou mais ela vai poder dirigir.
// 3 - Definir uma variável chamada "idade" que inicie com algum valor Ex: var idade = 41
// 4 - Será necessário uma condicional que verifique se a idade da pessoa é igual ou maior a 18.
// 5 - vamos utilizar um operador lógico chamado "maior ou igual" na condicional Ex: >=
// 6 - se a idade for maior ou igual a 18 exibir a saída: console.log("Você pode dirigir")
// 7 - se a idade for menor que 18 exibir a saída: console.log("Você não pode dirigir")
// 8 - Abra um terminal nesse arquivo, e execute o código com node "nome_do_arquivo.js"
// 9 - Verifique se a saída faz sentido e corresponde ao exercício.


const primeiraNota = 5;
const segundaNota = 5;
const terceiraNota = 5;
const quartaNota = 5;
const media = 5;
const notaFinal = (primeiraNota + segundaNota + terceiraNota + quartaNota) / 4;


if( notaFinal >= media ){
    console.log("Aluno aprovado!");
} else {
    console.log("Aluno reprovado!");
}