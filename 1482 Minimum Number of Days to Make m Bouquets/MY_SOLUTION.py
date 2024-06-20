class Solution:
    # This solution timeouts on larger inputs but should work for most of them
    def currentlyBloomed(self, bloomDay, currentDay):
        bloomed = []
        for i in range(len(bloomDay)):
            if bloomDay[i] <= currentDay:
                bloomed.append(i)
    
        return bloomed

    def setsOfConsecutives(self, bloomed, k):
        sets = 0
        counter = 0

        i = 0
        while i < len(bloomed):
            j = 0
            consecutiveFound = True
            while j < k and consecutiveFound:
                print(bloomed)
                print('i: ' + str(i) + ' j: ' + str(j) + ' sets: ' + str(sets) + ' counter: ' + str(counter))
                if i+j < len(bloomed) and bloomed[i] + j == bloomed[i+j]:
                    counter += 1
                    if counter >= k:
                        counter = 0
                        sets += 1
                        i += k
                else:
                    counter = 0
                    i += j
                    consecutiveFound = False
                print('i: ' + str(i) + ' j: ' + str(j) + ' sets: ' + str(sets) + ' counter: ' + str(counter))
                j += 1

        return sets
    
    def minDays(self, bloomDay, m, k) -> int:
        days = -1
        currentDay = min(bloomDay)
        complete = False
        bloomers = {}

        while currentDay <= max(bloomDay) and not complete:
            bloomers[currentDay] = self.currentlyBloomed(bloomDay, currentDay)
            sets = self.setsOfConsecutives(bloomers[currentDay], k)

            if sets >=  m:
                days = currentDay
                complete = True

            currentDay += 1

        return days
    
if __name__ == '__main__':
    bloomDay = [1000000000,1000000000]
    m = 1
    k = 1
    ans = Solution()
    print(ans.minDays(bloomDay = bloomDay, m = m, k = k))
    