class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]] * len(nums)
        postfix = [nums[len(nums) - 1]] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        result = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                result[i] = postfix[i+1]
            elif i == len(nums) - 1:
                result[i] = prefix[i-1]
            else:
                result[i] = prefix[i-1] * postfix[i+1]

        return result