package main
import (
	"fmt"
)
func pythagorean (one, two, three int) bool {
	return (one*one) + (two*two) == three*three
}

func solutionsCount(perimeter int) int {
	var count int
	for i := 1; i < perimeter; i++ {
		for j := 1; j < i; j ++ {
			for k := 1; k < j; k++ {
				if pythagorean(j, k, i) && (i + j + k) == perimeter {
					count++
				}
			}
		}
	}
	return count
}

func findMax(array []int) int{
	var max int = array[0]
	for _, value := range array {
		if value > max {
			max = value
		}
	}
	return max
}

func main () {
	var counts []int
	for i := 1; i < 1000; i++ {
		counts = append(counts, solutionsCount(i))
	}
	//largest is 8
	//fmt.Println(findMax(counts))
	for j := 0; j < len(counts); j++ {
		if counts[j] == 8{
			fmt.Println(j + 1)
			//prints 840
		}
	}	
	
}