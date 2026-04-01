class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if is the start of the seq
            if (n - 1 ) not in numSet:
                length = 0
                while (n + length) in numSet:
                    print(n + length)
                    length += 1
                longest = max(length, longest)
        return longest        




        #count = 0
        #sequence = []
        #print(sorted(nums))
        #for number in sorted(nums):
        #    if (len(sequence) == 0):
        #        sequence.append(number)
        #    if(number not in sequence and sequence[-1]+1 == number):
        #        sequence.append(number)
        #return len(sequence)