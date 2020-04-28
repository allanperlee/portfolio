function nine(n){
    for (i = 0; i < 500; i++){
        for (j = 0; j < 500; j++){
            for (k = 0; k < 500; k++ ){
                if (i + j + k == n){
                    if (i**2 + j**2 == k**2){
                        return i*k*j
                    }
                }
            }
        }
    }
}

console.log(nine(1000))
//prints 3187500