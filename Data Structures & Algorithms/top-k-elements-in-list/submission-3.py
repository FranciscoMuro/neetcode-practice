class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = {}
        res = []
        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1
        for i in range(k):
            max_val_key = max(nums_freq, key=nums_freq.get)
            res.append(max_val_key)
            nums_freq.pop(max_val_key)
        return res