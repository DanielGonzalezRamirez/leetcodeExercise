class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        maxAreas = [-1] * n

        for i in range(0,n):
            for j in range(0,n):
                h1 = height[i]
                h2 = height[j]

                hForArea = min([h1,h2])
                bForArea = abs(j-i)

                area = hForArea * bForArea

                if area > maxAreas[i]:
                    maxAreas[i] = area

        return max(maxAreas)
