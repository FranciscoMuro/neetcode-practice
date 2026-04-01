class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_diff = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store_diff:
                return [store_diff.get(diff), i]
            store_diff[num] = i

        return []        