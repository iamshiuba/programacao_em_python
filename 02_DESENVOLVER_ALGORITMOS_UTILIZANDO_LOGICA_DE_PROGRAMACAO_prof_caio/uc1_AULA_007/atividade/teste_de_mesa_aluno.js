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

//                                                       //
//                      TESTE DE MESA                    //
//			                                             //
// PASSOS	        INSTRUÇÕES	           TOTAL	X	 Y
//   1	        let total = 0;               0
//   2	        let y = 0;	           	            0
//   3	        for(x = 0;)		                         0
//   4	        total = total + x + 2;     	 2
//   5	        y++	                       	   	    1
//   6	        x++                           		     1
//   7	        total = total + x + 2;	     5
//   8	        y++		                        	2
//   9	        x++;	                               	 2
//  10	        total = total + x + 2;	     9
//  11	        x++;	                   	        3
//  12	        total = total + x + 2;	    14
//  13	        x++;		                        4
//  14 - Leia	        14
//  15 - Leia	         4
//  16 - Leia	         2