package main

import (
	"fmt"
)

func fib(n int, c chan int) {
	x, y := 2, 3
	for i := 1; i < n; i ++{
		c <- x
		x, y = y, x+y
	}
	close(c)
}

func main(){
	c := make(chan int, 32)
	go fib(cap(c), c)
	sum := 0
	for i := range c{
		if i % 2 == 0{
			sum += i
		}
	}
	fmt.Println(sum)
}