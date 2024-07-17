class Solution:
    def isPalindrome(self, x):
        num = str(x)
        palindrome = True

        i = 0
        j = len(num) - 1

        while i < j and palindrome:
            if num[i] != num[j]:
                palindrome = False
            else:
                i += 1
                j -= 1

        return palindrome