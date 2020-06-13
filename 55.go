package main

import (
	"fmt"
	
)

func main () {
	var counter int = 0
	for i := 10; i < 10000; i++ {
		if isLychrel(i) {
			counter++
		}
	}
	fmt.Println(counter)
	//prints 249
}


func reverse (natural int) int {
	var remainder, reverse int
	for {
		remainder = natural % 10
		reverse = reverse * 10 + remainder
		natural /= 10
		if natural == 0 {
			break
		}
	}
	return reverse
}

func isPalin (natural int) bool {
	var reversed int = reverse(natural)
	return reversed == natural
}

func isLychrel (natural int) bool {
	for i := 0; i < 25; i++ {
		natural += reverse(natural)
		if isPalin(natural) {
			return false
		}
	}
	return true
}