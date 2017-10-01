package main
// This is an implementation of a program to take the sum of all multiples of three and five less than 1000 using go channels

import (
	"fmt"
)

func three_five_multiples(c chan int, multiple_of int){
	sum := 0
	i := multiple_of
	for i<1000{
		sum += i
		i += multiple_of
	}
	c <- sum
}

func main(){
	c := make(chan int)
	go three_five_multiples(c, 3)
	go three_five_multiples(c, 5)
	go three_five_multiples(c, 15)

	threes, fives, both := <-c, <-c, <-c


	fmt.Println((threes + fives) - both)
}
