class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                start = idx
                maxArea = max(maxArea, height * (i - idx))
            stack.append([start, h])
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        return maxArea