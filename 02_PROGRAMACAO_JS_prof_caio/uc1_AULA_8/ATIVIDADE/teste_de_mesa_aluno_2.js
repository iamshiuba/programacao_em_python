// Uma empresa rede Educacional chamada "Big Education" que é dona 
// de varios projetos  na área de educação tem um novo projeto.
// Essa rede  de educação tem uma unidade que apenas atende
// pessoas com dificuldade de atividade devido transtornos.
// Nessa mesma unidade eles devem ensinar matemática de forma 
// diferente para que os alunos consigam evoluir melhor nas atividades.

// É necessário um ensino diferente da área de exatas para melhor
// absorção do conteúdo.
// Dessa forma a rede decidiu encomenda um software "Sob demanda"
// Sendo o MVP de uma ferramenta que ensina como formas geométricas
// funcionam (o programa exibe elas em 3 D e também permite interações)

// Profissionais do Produto
// Product Manager (Gestor do Produto - fala com cliente)
// Product Owner (Dono do Produto - Passa os requisitos para a equipe)

// O Product Owner (Dono do Produto) ele vai ter  passar os
// requisitos do cliente traduzidos para você de forma "Técnica"

// 1 - Passar em algoritmo a fórmula para calcular a área
// de um círculo.
// 1: Criar uma constante chamada pi e atribuir o valor 3.14
// 2: Criar uma constante chamada raio e atribuir valor  5
// 3: Criar uma constante área e atribuir pi (raio * raio)

//const pi = 3.14;
//const raio = 5;
//const area = pi (raio * raio)

// 2 - De ultima hora conversei com o cliente e descobri
// que necessito reutilizar essa formula em outros trechos
// do programa/software.

// FUNÇÃO
function calcularAreaCirculo(raio){
	const pi = 3.14;
	return area = pi * (raio * raio);
} console.log(calcularAreaCirculo (10));
	
// 3- Foi solicitado para que voce faça o mesmo procedimento feito com a fórmula de área do círculo
// só que dessa vez você vai fazer com a área do triângulo.
// 1:. Pesquisar a fórmula da área do triângulo.
// 2:. Definir uma função chamada calcularAreaTriangulo
// 3:. Colocar um console.log (calcularAreaTriangulo(10,20))
	
function calcularAreaTriangulo(b,h){
	return area = (b*h)/2;
} console.log (calcularAreaTriangulo(10,20));

// Atividade

function calcularAreaQuadrado (l){
    return area = l*l;
} console.log (calcularAreaQuadrado (5));