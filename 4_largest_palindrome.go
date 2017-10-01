package main

import(
	"fmt"
	"strconv"
)

func is_palindrome(s string) bool{
	var value bool
	if s == reverse_string(s){
		value = true
	}
	return value
}

func reverse_string(s string) string{
	length := len(s)
	for _, v := range s{
		s = string(v) + s
	}
	return s[:length]
}

func largest_palindrome() int{
	var value int
	value = 0
	for i := 100; i < 1000; i++{
		for j := 100; j < 1000; j++{
			product := strconv.Itoa(i*j)
			if is_palindrome(product){
				if i*j > value{
					value = i*j
				}
			}
		}
	}
	return value
}

func main(){
	fmt.Println(largest_palindrome())
}