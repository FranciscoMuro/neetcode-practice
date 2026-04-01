class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[len(height)-1]
        l, r = 0, len(height) - 1
        watter = 0
        
        while l < r:
            if (maxL <= maxR):
                l+=1
                result = maxL - height[l]
                if (result>0):
                    watter += result
                if (maxL < height[l]):
                    maxL = height[l]
            if (maxL > maxR):
                r-=1
                result = maxR - height[r]
                if (result>0):
                    watter += result
                if (maxR < height[r]):
                    maxR = height[r]

        return watter