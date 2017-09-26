module Utils where

import Data.List

--Let's implement the sieve of Eratosthenes first
sieve :: Int -> [Int]
sieve n =
    let
        -- Create a list of True/False to indicate whether given element is prime
        -- We start with 0 and 1 indices as false since they are not prime
        -- Take n-1 more true values so index reaches n
        initialSieveList = [False,False] ++ (take (n-1) $ repeat True)
        -- Start with 2 as first prime
        -- sieve' gives list of booleans where index is true when prime and false o/w
        sieveList = sieve' initialSieveList 2
        zippedSieveList = zip [0..n] sieveList
    in
        [i | (i,_) <- (filter (\(i,isPrime) -> isPrime) zippedSieveList)]


isMultiple :: Int -> Int -> Bool
isMultiple m n = (m `mod` n == 0)

newSieveListMap :: Int -> Int -> [Bool] -> Bool
newSieveListMap index startingPrime oldSieveList = case (index <= startingPrime) of 
    -- Leave all terms smaller than starting prime alone
    True -> oldSieveList !! index
    -- Flip terms that are multiples of the starting prime and not already false
    otherwise -> (oldSieveList !! index) && (not (isMultiple index startingPrime))

sieve' :: [Bool] -> Int -> [Bool]
sieve' sieveList startingPrime =
    let
        sieveListIndices = [0..((length sieveList) - 1)]
        -- Mark all multiples of starting prime as False to indicate not prime
        newSieveList = map (\i -> newSieveListMap i startingPrime sieveList) sieveListIndices
        nextPrime = findIndex (\i -> (i > startingPrime) && (newSieveList !! i)) sieveListIndices
    in
        case nextPrime of
            Nothing -> newSieveList
            Just p -> sieve' newSieveList p

-- Now that we have a sieve, lets write a function to get prime factors of a number
-- largestPrimeFactor :: Int -> Int
-- largestPrimeFactor n = maximum [i | i <- sieve (floor (sqrt (fromIntegral n))), n `mod` i == 0]

isPrime n = (length $ filter (isMultiple n) [2..(n-1)]) == 0

getPrimeFactors n =
    let
        getPrimeFactors' n start factors = if (isMultiple n start) && (isPrime start)
            then  
                let 
                    newN = quot n start
                in
                    if (isPrime (newN)) then ([start,newN] ++ factors) else (getPrimeFactors' newN 2 ([start] ++ factors))
            else getPrimeFactors' n (start+1) factors
    in
        getPrimeFactors' n 2 []