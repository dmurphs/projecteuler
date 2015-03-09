package main

import (
	"fmt"
)

func main(){
	var num int64
	var largest_factor int64
	num  = 600851475143
	var i int64
	for i = 2; i*i < num; i++{
		var is_prime bool
		if (num % i == 0){
			is_prime = true
			var j int64
			for j = 2; j < i; j++{
				if i%j == 0{
					is_prime = false
					break
				}
			}
			if is_prime{
				largest_factor = i;
			}
		}
	}
	fmt.Println(largest_factor)
}