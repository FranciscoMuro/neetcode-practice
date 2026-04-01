class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxWatter = 0

        l, r = 0, len(h)-1

        while l < r:
            calcA = (r - l) * min(h[r], h[l])
            maxWatter = max(maxWatter, calcA)
            if h[l] < h[r]:
                l += 1
            else:
                r -= 1
        
        return maxWatter