class Veiculo {

    #fabricante;
    #modelo;
    #cor;
    #origem;
    #ano;

    constructor(fabricante, modelo, cor, origem, ano) {
    this.#fabricante = fabricante;
    this.#modelo = modelo;
    this.#cor = cor;
    this.#origem = origem;
    this.#ano = ano;
   }
   acelerar(){
    return "Acelerando";
   }
   frear(){
    return "Freando";
   }
}

const meuCarro = new Veiculo("Honda", "Civic", "Preto", "Japão", "1973")
console.log(meuCarro);