// 1 - crie um algoritmo que calcule a área de um círculo, se for maior que 10 exibir a área.
// 2 - Defina uma constante raio e atribua o valor 11;
// 3 - Vamos precisar de uma constante pi com o valor 3.14 Ex: const pi = 3.14
// 4 - Crie uma constante area dessa forma: Ex: const const area = 3.14 * (raio * raio);
// 5 - crie uma condicional que verifica se area é maior que 10;
// 6 - imprimir a saída Ex: console.log(area); que vai exibir o resultado.
// 7 - Obs: Não precisa imprimir nada caso não seja maior que 10.
// 8 - Execute o programa e veja se realmente faz sentido o resultado.

const raio = 11;
const pi = 3.14;
const area = pi * (raio * raio);

if(area > 10){
    console.log(area);
}