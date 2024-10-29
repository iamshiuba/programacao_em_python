// 1 - A partir desse algoritmo pronto modifique-o para que calcule a porcentagem do imposto de renda dependendo do valor e exiba o resultado.
// 2 - Diferente do algoritmo usado na aula, aqui você realmente deve trazer o valor calculado baseado na porcentagem.
// 3 - Defina uma variável chamada salário Ex: var salário
// 4 - Atribua um valor de salário a variavel salario Ex: 1500.00
// 5 - Devemos respeitar a seguintes regras:
// Até 2259,20 -> Isento não paga imposto de renda portanto é ZERO
// De 2259,21 até 2.826,65 -> 7,5%
// De 2.826,66 até 3.751,05 -> 15%
// De 3.751,06 até 4.664,68 -> 22,5%
// Acima de 4.664,68 -> 27,5%
// 6 - Obs: O aluno deve pesquisar posições soluções/abordagens desse algoritmo que estão na linguagem javascript, e assim adaptar ao algoritmo abaixo;
// BÔNUS: Se o aluno tiver interesse, pode optar por escrever comentários que descrevam cada linha única de código e o que ela faz.
// Ex: Linha 15: Define uma variável salário e atribui o valor 1500.00 nela, aqui dessa forma podemos chamar salario e invocar o valor 1500.00


let salario = 1500.00

if (salario <= 2259.20) {
    console.log("0%");
}
else if (salario >= 2259.21 && salario <= 2826.65){
    console.log("7,5%"); 
}
else if (salario >= 2826.66 && salario <= 3751.05){
    console.log("15%");
}
else if (salario >= 3751.05 && salario <= 4664.68){
    console.log("22,5%");
}
else {
    console.log ("27,5%");
}



