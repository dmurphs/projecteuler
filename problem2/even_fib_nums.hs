fib :: Integer -> Integer
fib n = if n < 4
    then n
    else (fib (n-1)) + (fib (n-2))

fibSumEvenToBound :: Integer -> Integer
fibSumEvenToBound n = sum $ takeWhile (< n) [(fib i) | i <- [2,5..]]

main :: IO ()
main = print (fibSumEvenToBound 4000000)