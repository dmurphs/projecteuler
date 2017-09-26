import Utils (isPrime, isMultiple) -- these functions are in hslib/Utils.hs, make sure to load

largestPrimeFactor n =
    let
        -- we don't want to check any numbers over sqrt n
        maxNum = floor $ sqrt (fromIntegral n)

        -- helper function for recursion
        largestPrimeFactor' n start largestFactor
            | start >= maxNum = largestFactor
            | (isMultiple n start) && (isPrime start || isPrime startQuotient) =
                largestPrimeFactor' n (start + incrementBy) (maxPrime start startQuotient)
            | otherwise = largestPrimeFactor' n (start + incrementBy) largestFactor

            where
                maxPrime a b = maximum $ filter isPrime [a, b]
                startQuotient = quot n start
                -- We add one after the first iteration when start = 2, then
                -- we can add to after that since we only need to check odd
                -- numbers past 2
                incrementBy = if start > 2 then 2 else 1
    in
        largestPrimeFactor' n 2 0

main :: IO ()
main = print $ largestPrimeFactor 600851475143