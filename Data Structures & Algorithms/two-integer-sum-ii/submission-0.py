class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        l, r = 0, len(numbers) - 1
        while (l < r):
            sumatory = numbers[l]+numbers[r]
            if (sumatory == target):
                result.append(l+1)
                result.append(r+1)
                return result
            if (sumatory <= target):
                l += 1
            if (sumatory >= target):
                r -= 1

        return result 