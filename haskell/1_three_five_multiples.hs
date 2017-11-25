-- Find sum of all multiples of 3 or 5 below 1000

threeFiveMultiples :: [Integer]
threeFiveMultiples = [i | i <- [1..999], i `mod` 3 == 0 || i `mod` 5 == 0]

sumThreeFiveMultiples :: Integer
sumThreeFiveMultiples  = sum threeFiveMultiples

main :: IO ()
main = print sumThreeFiveMultiples