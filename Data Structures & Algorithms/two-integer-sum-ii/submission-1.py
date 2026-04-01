class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        r, l = 0, len(numbers)-1

        while (r < l):
            sum = numbers[r] + numbers[l]
            if sum > target:
                l -= 1
            if sum < target:
                r += 1
            if sum == target:
                res.append(r+1)
                res.append(l+1)
                break
        return res