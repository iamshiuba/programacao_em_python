// 1 - Criar uma classe abstrata(Ex: serVivo).
// 2 - Tema do jogo: RPG

class Player {
  constructor(name, health, mana, xp, dmg, stamina) {
    this.name = name;
    this.health = health;
    this.mana = mana;
    this.xp = xp;
    this.dmg = dmg;
    this.stamina = stamina;
  }
  move() {}
  attack() {}
  communicate() {}
}

class Elf extends Player {
  constructor(name, health, mana, xp, dmg, stamina) {
    super(name, health, mana, xp, dmg, stamina);
  }
  move() {
    if (this.stamina > 25) {
      console.log("O elfo subindo as paredes e deslizando como o Légolas!");
    } else {
      console.log("O elfo está muito cansado, aguarde um momento!");
    }
  }
  attack() {
    console.log("O elfo ataca utilizando seu arco e flecha!");
  }
  communicate() {
    console.log("kha'oel si'sa law'bu");
  }
}

const MainPlayer = new Elf("Laber", 100, 100, 30, 25, 75);
console.log(MainPlayer);
MainPlayer.move;
MainPlayer.attack;
MainPlayer.communicate;