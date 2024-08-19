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


// Define a variável salário com o valor de R$ 1500.00
var salario = 4664.68;

// Variável para armazenar o valor do imposto de renda
var impostoRenda = 0;

// Verifica se o salário é menor ou igual a R$ 2259.20 (isento)
if (salario <= 2259.20) {
  console.log("ISENTO"); // Se isento, exibe a mensagem "ISENTO"
} else if (salario <= 2826.65) {
    impostoRenda = salario * 0.075; // 7.5% de imposto
  } else if (salario <= 3751.05) {
    impostoRenda = salario * 0.15; // 15% de imposto
  } else if (salario <= 4664.68) {
    impostoRenda = salario * 0.225; // 22.5% de imposto
  } else {
    impostoRenda = salario * 0.275; // 27.5% de imposto
  }

  // Exibe o valor do imposto de renda calculado
  console.log("Imposto de renda:", impostoRenda.toFixed(2)); 
