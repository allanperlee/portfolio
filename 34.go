package main

import
(
	"fmt"
)

func main () {
	var counter int = 0
	for i := 3; i < 1000000; i++{
		if fullFactorial(i){
			counter += i
		}
	}
	fmt.Println(counter)
	//prints 40730
}

func factorial (natural int) int {
	var counter int = 1
	for i := 1; i < natural + 1; i++{
		counter *= i
	}
	return counter
}

func fullFactorial (natural int) bool{
	var count int = 0
	var copy int
	copy = natural
	for copy > 0 {
		count += factorial(copy % 10)
		copy = copy / 10
	}
	return count == natural
}