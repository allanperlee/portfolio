package main

import (
	"fmt"
	"math"
)

func main () {
	var primes []int
	for i := 2; i < 200; i++{
		if isPrime(i){
			primes = append(primes, i)
		}
	}
	var limit int = 1000000
	fmt.Println(sixtyNine(limit, primes))
	//prints 510510

}

func isPrime(natural int) bool {
	for i := 2; i <= int(math.Floor(float64(natural) / 2)); i++{
		if natural % i == 0{
			return false
		}
	}
	return natural > 1
}

func sixtyNine(limit int, array []int) int{
	var result = 1
	var j = 0
	for result * array[j] <= limit{
		result *= array[j]
		j++
	}
	return result
} 