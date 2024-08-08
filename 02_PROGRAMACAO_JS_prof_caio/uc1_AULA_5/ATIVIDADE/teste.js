class Pessoa { 
    constructor(nome, idade) { 
      this.nome = nome; 
      this.idade = idade; 
    } // classe nomeDaClasse { construtor(parametros, do, construtor) { isto.parametros É parametros; isto.do É do; isto.construtor É construtor; } 
   
    apresentar() { 
      console.log("Olá, meu nome é " + this.nome + " e tenho " + this.idade + " anos."); 
     } 
   } 
   
   const pessoa1 = new Pessoa("João", 30); // ‘new’ cria uma nova instância/novo objeto. 
   pessoa1.apresentar(); // Saída: "Olá, meu nome é João e tenho 30 anos." 