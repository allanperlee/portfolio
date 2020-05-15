package main
import ("fmt")

func four(number int) bool{
	var temp, remainder int
	var reverse int = 0

	temp = number
	for {
		remainder = number % 10
		reverse = reverse*10 + remainder
		number /= 10

		if number == 0{
			break
		}
	}
	if temp == reverse{
		return true
	} else{
		return false
	}
}

func main (){
	var i, j int


	for i = 100; i < 1001; i++{
		for j = 100; j < 1001; j++{
				if four(i*j){
					fmt.Println(i*j)
			}
			}
		}
	}

	//the last three printed on the console are 580085, 514415, and 906609, the latter being the correct answer

