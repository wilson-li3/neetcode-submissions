class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)

        for key, value in counts.items():
            buckets[value].append(key)

        result = []
        length = len(result)
        
        for i in range(len(buckets) - 1, -1, -1):
            if length == k:
                return result
            for j in range(len(buckets[i])):
                result.append(buckets[i][j])
                length += 1
        
        