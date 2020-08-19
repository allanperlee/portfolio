package main

import(
	"fmt"
)

func isAbundant(natural int) bool {
	var counter int = 1

	for i := 2; i < natural; i++ {
		if natural % i == 0 {
			counter += i
		}
	}


	return counter > natural
}

func main (){
	var abundants[]int
	var limit int = 28123
	var counter int = 0
	var isSumOfTwoAbundants[28124]bool

	for i := 2; i < limit; i++{
		if isAbundant(i) {
			abundants = append(abundants, i)
		}
	}

	for j := 0; j < len(abundants); j++ {
		for k := 0; k < len(abundants); k++ {
			if abundants[k] + abundants[j] <= limit {
				isSumOfTwoAbundants[abundants[j] + abundants[k]] = true
			} else {
				break
			}
		}
	}

	for l := 0; l < len(isSumOfTwoAbundants); l++ {
		if !isSumOfTwoAbundants[l] {
			counter += l
		}
	}
	fmt.Println(counter)	
}

//prints 4179871