class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n 
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # first solution

        n = len(nums)

        res = [0] * n
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*nums[i]


        suffix = [0] * n 
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]


        res[0] = suffix[1] 
        for i in range(1, n-1):
            res[i] = prefix[i-1] * suffix[i+1]
        res[n-1] = prefix[n-2] 


        return res