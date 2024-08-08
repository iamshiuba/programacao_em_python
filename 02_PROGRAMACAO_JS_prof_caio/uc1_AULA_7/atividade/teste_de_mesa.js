let total = 0;

for (x = 0; x < 3; x++) {
  total = total + x + 1;
}

console.log(total);
console.log(x);

//                                                   //
//                     TESTE DE MESA	             //
//		                                             //
// PASSOS	    INSTRUÇÕES	             TOTAL       X
// 1	        total = 0;	               0
// 2	        for(x = 0;)		                     0
// 3	        total = total + x + 1;	   1
// 4	        x++		                             1
// 5	        total = total + x + 1; 	   3
// 6	        x++		                             2
// 7	        total = total + x + 1;	   6
// 8	        x++	                            	 3
// 9 - Leia	        6
// 10 - Saida         3
