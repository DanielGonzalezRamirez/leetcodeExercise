class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        p_num = 0
        c_num = 0
        ans = 0

        i = len(s) - 1
        while i >= 0:
            c_num = numbers[s[i]]
            if c_num >= p_num:
                ans += c_num
            else:
                ans -= c_num
            i -= 1
            p_num = c_num

        return ans