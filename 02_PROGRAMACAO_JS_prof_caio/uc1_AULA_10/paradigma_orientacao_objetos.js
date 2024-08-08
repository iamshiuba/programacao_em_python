// 1 - O código da máquina é binário, ou seja:
// 0 ou 1

// 2 - Paradigma da orientação a objetos é uma solução.

// Classe: Cachorro

// Atributos: Nome, Idade, PesokG, Cor, Raça, Porte, Personalidade, Origem
// Método: latir(), correr(), pular(), morder(), dormir()

// const meuCachorro = New Cachorro("Mel", 2, 10);

// meuCachorro.latir();
// console.log(meuCachorro.idade);

// App de Banco
// classe Cliente

// Atributos: nome, cpf, data_de_nascimento, saldo
// Método: consultarSaldo(), executarTransferencia(), ocultarSaldo()

// const novoCliente = new Cliente("Carlos", "155.070.150-54", "01/01/1999", 1500.00);

// novoCliente.ocultarSaldo()
// console.log(novoColiente.saldo);

// classe Humano
// classe Pedreiro
// classe Psicólogo
// ---------------

// classe SerVivo
// classe Animal
// classe Gato

// 1 - Pesquise como fazer o seguinte abaixo em javascript
// definir uma classe chamada Cliente
// definir os atributos: nome, cpf, data_de_nascimento, saldo
// criar os métodos: consultarSaldo(), executarTransferencia(), ocultarSaldo()
// instanciar uma classe Cliente chamada primeiroCliente com os valores:
// "Roberto", "155.070.150-54", "05/05/1981", 5422.22
// exibir os valores com console.log() de saldo e executar o método consultarSaldo()

class Cliente {
  constructor(nome, cpf, data_de_nascimento, saldo) {
    this.nome = nome;
    this.cpf = cpf;
    this.data_de_nascimento = data_de_nascimento;
    this.saldo = saldo;
  }
  consultarSaldo() {
    console.log("O seu saldo é: " + this.saldo);
  }
  executarTransferencia() {
    console.log("Sua transferência foi realizada!");
  }
  ocultarSaldo() {
    console.log("Seu saldo foi ocultado!");
  }
}

const primeiroCliente = new Cliente(
  "Roberto",
  "155.070.150-54",
  "05/05/1981",
  5422.22
);
console.log(primeiroCliente.saldo);
primeiroCliente.consultarSaldo();
primeiroCliente.executarTransferencia();
primeiroCliente.ocultarSaldo();