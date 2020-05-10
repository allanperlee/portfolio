function collatz (integer){
    var counter = 1
    while (integer > 1){
        counter ++;
        if (integer % 2 == 0){
            integer = integer / 2;
        }
        else {
            integer = 3 * integer + 1;
        }
    }
    return counter;
}

sequences = []
for (i = 0; i < 1000000; i++){
    sequences.push(collatz(i));
}

function arrayMax(array){
    return array.reduce(function(a, b){
        return (a > b ? a : b);
        })
}
console.log(sequences.indexOf(525));

//prints 837799