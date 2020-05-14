package main

import ("fmt")

func five(num int) bool{
	for i := 2; i < 21; i++{
		if num % i != 0{
			return false
		} 
		}
	return true
	}


func main(){
num := 2520
for five(num) == false{
	num += 20
}
fmt.Println(num)
}

// Prints 232792560
