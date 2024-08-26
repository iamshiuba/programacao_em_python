class Veiculo {
    constructor(fabricante, modelo, cor, origem, ano) {
        let _fabricante = fabricante;
        let _modelo = modelo;
        let _cor = cor;
        let _origem = origem;
        let _ano = ano;

        this.getFabricante = () => _fabricante;
        this.getModelo = () => _modelo;
        this.getCor = () => _cor;
        this.getOrigem = () => _origem;
        this.getAno = () => _ano;
    }

    acelerar(){
        return "Acelerando";
    }

    frear(){
        return "Freando";
    }
}

const meuCarro = new Veiculo("Honda", "Civic", "Preto", "Japão", "1973");
console.log(meuCarro.fabricante);