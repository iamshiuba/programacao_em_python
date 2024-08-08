let total = 0;
let y = 0;

for(x = 0; x<4; x++){
    total = total + x + 2;
    if(x < 2){
        y++;
    }
}

console.log(total);
console.log(x);
console.log(y);