memoizedFib :: Int -> Integer
memoizedFib = (map fib [0 ..] !!)
   where fib 1 = 1
         fib 2 = 2
         fib n = memoizedFib (n-2) + memoizedFib (n-1)

fibSumEvenToBound :: Integer -> Integer
fibSumEvenToBound n = sum $ takeWhile (< n) [(memoizedFib i) | i <- [2,5..]]

main :: IO ()
main = print (fibSumEvenToBound 4000000)
