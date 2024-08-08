class Turma {
  constructor(turno, modalidade, alunos, instrutor) {
    this.turno = turno;
    this.modalidade = modalidade;
    this.alunos = alunos;
    this.instrutor = instrutor;
  }
}

const T0001 = new Turma(
  "noite",
  "presencial",
  [
    "Tiago",
    "Reynald",
    "Gabrielle",
    "Heitor",
    "João",
    "Chris",
    "Rhian",
    "Thiago",
    "Gabriela",
  ],
  "Caio"
);
console.log(T0001);

class Aluno {
  constructor(matricula, nome, idade) {
    this.matricula = matricula;
    this.nome = nome;
    this.idade = idade;
  }
}

const Aluno1 = new Aluno(1001, "Tiago", 19);
const Aluno2 = new Aluno(1002, "Reynald", 23);
console.log(Aluno1, Aluno2);
