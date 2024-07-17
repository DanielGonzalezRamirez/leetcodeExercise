class Solution:
    def isPalindrome(self, x):
        palindrome = True
        digits = []

        if x < 0:
            palindrome = False

        while x > 0:
            digits.append(int(x % 10))
            x = int(x / 10)
            print(x)
        
        i = 0
        j = len(digits) - 1

        while palindrome and i < j:
            if digits[i] != digits[j]:
                palindrome = False
            else:
                i += 1
                j -= 1        

        return palindrome
    
def main():
    x = -12345654321
    print(Solution().isPalindrome(x=x))

if __name__ == '__main__':
    main()