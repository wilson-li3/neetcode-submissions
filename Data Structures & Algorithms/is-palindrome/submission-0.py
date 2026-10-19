class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        l = 0
        r = len(lower) - 1

        while l < r:
            if not lower[l].isalnum():
                l += 1 
            elif not lower[r].isalnum():
                r -= 1
            else:
                if lower[l] != lower[r]:
                    return False
                l += 1
                r -= 1
        return True