class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        l_mult = 1
        r_mult = 1



        for left in range(n):
            right = -left -1
            l_arr[left] = l_mult
            r_arr[right] = r_mult
            l_mult *= nums[left]
            r_mult *= nums[right]

        for l, r in zip(l_arr, r_arr):
            res.append(l*r)


        return res;