package main

import (
	"fmt"
	"math"
)

func main () {
	var foundIt bool = true
	var i int = 144
	var final int = 0
	for foundIt{
		var hexagon = hexagonize(i)
		if isTri(hexagon) && isPent(hexagon){
			foundIt = false
			final = hexagon
		}
	 i++
	}
	fmt.Println(final)
	//prints 1533776805
}

func isTri(natural int) bool {
	var floated float64 = float64(natural)
	var firstStep int = int(math.Sqrt(2 * floated))
	return int(0.5 * float64(firstStep) * float64(firstStep + 1)) == natural
}

func isPent(natural int) bool {
	var i int = 1
	var m int = i
	for m < natural {
		m = (3 * i * i - i) / 2
		i++
	}
	return m == natural
}

func hexagonize(natural int) int {
	return natural*(2 * natural - 1)
}