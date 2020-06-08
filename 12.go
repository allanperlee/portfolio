package main

import( "fmt";
	"math")

func isTriangle(natural int) bool{
	var otherNatural float64 = float64(natural)
	var firstStep int = int(math.Sqrt(2*otherNatural))
	return  int(0.5 * float64(firstStep) * (float64(firstStep+1))) == natural
}

func divisors(natural int) int{
	var counter int = 0
	var end int = int(math.Sqrt(float64(natural)))
	var i int

	for i = 1; i < end+1; i++{
		if natural % i == 0{
			counter += 1
			if i != natural/i{
				counter += 1
		}
		}
	}
	return counter
}

func continued(natural int) int{
	if isTriangle(natural){
		return int(math.Sqrt(float64(2*natural))) + 1
	} else {
		return 0
	}
}



func main(){
	//a shortcut to the first number that contains 500 divisors
	var shortcut int = int(math.Pow(2, 4)) * int(math.Pow(3, 4)) * int(math.Pow(5, 4)) * 7 * 11
	
	for !isTriangle(shortcut){
		shortcut ++
	}

	var lastItem int = continued(shortcut)

	for divisors(shortcut) <= 500{
		shortcut += lastItem
		lastItem ++
	}

	fmt.Println(shortcut)

}

//prints 76576500
