package main

import (
	"fmt"
	"math"
)

func main () {
	var counter int = 0
	var triangle [][]int = pascalTri(101)
	
	for n := 0; n < 101; n++{
		for r := 0; r <= n; r++{
			if math.Abs(float64(triangle[n][r])) >= float64(1000000){
				counter++
			}
		} 
	}
	fmt.Println(counter)

	//prints 4075
}

func pascalTri(depth int) [][]int {
	t := make([][]int, depth)
	for r:= 0; r < depth; r++ {
		t[r] = make([]int, r + 1)
		left, right := 1, r-1
		t[r][left-1], t[r][right+1] = 1, 1
		for c := left; c <= right; c++{
			t[r][c] = t[r-1][c-1] + t[r-1][c]
		}
	}
	return t
}

