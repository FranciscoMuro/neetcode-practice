class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(len(nums)*2)
        i = 0
        j = 0
        while i < len(ans):
            if j == len(nums):
                j = 0
            print(i, j)
            ans[i] = nums[j]
            i+=1
            j+=1
        return ans