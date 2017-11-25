-- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
-- What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import Utils

isMultipleOneThroughTwenty :: Int -> Bool
isMultipleOneThroughTwenty n =
    (length $ filter (isMultiple n) nums) == length nums
    where
        nums = [1..20]

smallestMultiple :: Int
smallestMultiple =
    let
        findSmallestMultiple n
            | isMultipleOneThroughTwenty n = n
            -- We can add 20 since we know the number must still be a multiple of 20
            | otherwise                    = findSmallestMultiple (n+20)
    in
        -- We can start at 2520 based on the info given by the problem
        findSmallestMultiple 2520

main :: IO ()
main = print smallestMultiple
