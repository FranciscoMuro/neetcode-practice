class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) // 2
            hours = self.getHours(piles, mid)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left

    def getHours(self, piles, k):
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        return hours
