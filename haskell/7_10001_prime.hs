-- By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
-- What is the 10 001st prime number?

-- We can start at three and just check odd numbers to see if they are prime

primes :: [Integer]
primes = filterPrime [2..]
  where filterPrime (p:xs) = p : filterPrime [x | x <- xs, x `mod` p /= 0]

main :: IO
main = maximum $ take 10001 primes
