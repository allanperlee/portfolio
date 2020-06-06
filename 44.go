package main

import (
	"fmt"

)

func main () {
	var i int = 1
	var found = true
	var smallest = 0

	for found {
		i++
		var one int = pentagonize(i)
		for j := i - 1; j > 0; j--{
			var two int = pentagonize(j)
			if isPenta(one - two) && isPenta(one + two){
				smallest = one - two
				found = false
			}
		}
	}
	fmt.Println(smallest)
	//prints 5482660
}

func pentagonize(natural int) int {
	return natural * (3*natural - 1) / 2
}

func isPenta(natural int) bool {
	var i int = 1
	var m int = i
	for m < natural {
		m = (3 * i * i - i) / 2
		i++
	}
	return m == natural
}