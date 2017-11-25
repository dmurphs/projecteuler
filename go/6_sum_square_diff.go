package main

import(
	"fmt"
)

func sum_of_squares(begin int64, end int64) int64{
	var sum int64
	sum = 0
	var	i int64
	for i = begin; i < end; i++{
		sum += i*i
	}
	return sum
}

func square_of_sums(begin, end int64) int64{
	var total int64
	total = 0
	var i int64
	for i = begin; i<end; i++{
		total += i
	}
	return total*total
}


func main(){
	var x,y int64
	x = sum_of_squares(1, 101)
	y = square_of_sums(1, 101)

	fmt.Println(x)
	fmt.Println(y)

	fmt.Println(y-x)



}

