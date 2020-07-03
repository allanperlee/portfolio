package main

import(
	"fmt"
)

func main () {
	fmt.Println(latticePath(40))
	//prints 137846528820
}

func pascalTriangle (depth int) [][]int {
	triangle := make([][]int, depth)
	
	for row := 0; row < depth; row++ {
		triangle[row] = make([]int, row + 1)
		left, right := 1, row - 1
		triangle[row][left - 1], triangle[row][right + 1] = 1, 1
		for column := left; column <= right; column++ {
			triangle[row][column] = triangle[row - 1][column - 1] + triangle[row - 1][column]
		}

	}
	return triangle
}

func latticePath (gridSize int) int {
	triangle := pascalTriangle(gridSize + 1)
	return triangle[len(triangle) - 1][len(triangle) / 2]
}