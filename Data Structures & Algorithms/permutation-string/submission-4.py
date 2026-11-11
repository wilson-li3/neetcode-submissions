class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        satisfied = 0
        n = len(s1)
        l = 0

        for r in range(len(s2)):
            if r - l == n:
                if s2[l] in counts:
                    counts[s2[l]] += 1
                    if counts[s2[l]] == 1:
                        satisfied -= 1
                l += 1
                
            if s2[r] in counts:
                counts[s2[r]] -= 1
                if counts[s2[r]] == 0:
                    satisfied += 1

            if satisfied == len(counts):
                return True

        return False
                