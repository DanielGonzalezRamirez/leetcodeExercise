class Solution:
    def lengthOfShortestWord(self, amountOfWords, strs):
        # Find the shortest word in the list to limit search
        ans = len(strs[0])
        for i in range(amountOfWords):
            if ans > len(strs[i]):
                ans = len(strs[i])
        return ans

    def longestCommonPrefix(self, strs) -> str:
        prefix = ''
        letter = ''
        amountOfWords = len(strs)
        lengthOfShortestWord = self.lengthOfShortestWord(amountOfWords, strs)
        done = False
        
        i = 0
        # Loop over the characters
        while not done and i < lengthOfShortestWord:
            j = 0
            letter = strs[0][i]
            # Loop over the words
            while not done and j < amountOfWords:
                if strs[j][i] != letter:
                    done = True
                j += 1
            if not done:
                prefix += letter
            i += 1
        return prefix