module Utils where

import Data.List

isMultiple :: Int -> Int -> Bool
isMultiple m n = (m `mod` n == 0)

-- Now that we have a sieve, lets write a function to get prime factors of a number
-- largestPrimeFactor :: Int -> Int
-- largestPrimeFactor n = maximum [i | i <- sieve (floor (sqrt (fromIntegral n))), n `mod` i == 0]

isPrime n = (length $ filter (isMultiple n) [2..(n-1)]) == 0
