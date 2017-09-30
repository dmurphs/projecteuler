-- Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumSquares :: Integer -> Integer
sumSquares n = sum [i*i | i <- [1..n]]

squareSum :: Integer -> Integer
squareSum n =
    let sumFirstn = sum [1..n]
    in sumFirstn * sumFirstn

sumSquareDifference :: Integer -> Integer
sumSquareDifference = (-) <$> squareSum <*> sumSquares

main :: IO ()
main = print $ sumSquareDifference 100