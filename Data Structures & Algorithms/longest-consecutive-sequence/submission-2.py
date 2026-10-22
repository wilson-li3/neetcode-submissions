class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0
        for i in seen:
            if i-1 not in seen:
                curr = 1
                while i + curr in seen:
                    curr += 1
                res = max(curr, res)
        return res


# we need to put all the numbers into a set or map for fast lookup
# then iterate through all the values and see if the next one exists and keep a max window like that
# the only issue is when iterating, how do we know the range of numbers we are iterating through, we could keep a min max and iterate through that range to help the time complexity