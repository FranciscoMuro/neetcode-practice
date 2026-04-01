class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_diff = {}
    
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in store_diff:
                return [store_diff.get(diff), i]
            store_diff[nums[i]] = i
            
        return []
