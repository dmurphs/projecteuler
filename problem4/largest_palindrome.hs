-- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
-- Find the largest palindrome made from the product of two 3-digit numbers.

-- Probably not the fastest implementation but it works :)

isPalindrome :: Integer -> Bool
isPalindrome n = strN == reverse strN
    where strN = show n

threeDigitNums :: [Integer]
threeDigitNums = [100..999]

threeDigitNumProducts :: [Integer]
threeDigitNumProducts = [i*j | i <- threeDigitNums, j <- threeDigitNums]

productPalindromes :: [Integer]
productPalindromes = filter isPalindrome threeDigitNumProducts

maxPalindrome :: Integer
maxPalindrome = maximum productPalindromes

main :: IO ()
main = print maxPalindrome