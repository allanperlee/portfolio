package main

import(
	"fmt"
	"math"
)

func main () {
	var counter int = 0
	var primer int = 1

	for counter < 10001 {
		primer++
		if isPrime(primer){
			counter++
		}
	}
	fmt.Println(primer)
}

func isPrime(natural int) bool {
	var limit int = int(math.Sqrt(float64(natural)))
	for i := 2; i < limit + 1; i++ {
		if natural % i == 0{
			return false
		}
		}
		return true
	}

//prints 104743