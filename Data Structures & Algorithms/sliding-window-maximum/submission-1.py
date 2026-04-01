class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # result stores the max values of each window
        result = []
        # left and right pointer to limit the window (indices)
        l, r = 0, k
        maxVwindow = float('-inf')
        while r <= len(nums):
            for i in range (l, r):
                print(i)
                maxVwindow = max(maxVwindow, nums[i])
            result.append(maxVwindow)
            maxVwindow = float('-inf')
            print(nums[l:r])
            l += 1
            r += 1
        return result
