class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest = 0
        print(seq)
        for num in seq:
            if (num - 1) not in seq:
                length = 1
                while (num + length) in seq:
                    length += 1
                longest = max(length, longest)
        return longest

        