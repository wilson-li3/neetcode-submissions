class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = -1
        for p in piles:
            maximum = max(maximum, p)
        
        l,r = 1, maximum
        k = maximum
        while(l <= r):
            m = (l + r) // 2
            currHours = 0
            for p in piles:
                currHours += math.ceil(p / m)
                if currHours > h:
                    break
            if currHours <= h:
                r = m - 1
                k = min(k, m)
            else:
                l = m + 1
        return k





