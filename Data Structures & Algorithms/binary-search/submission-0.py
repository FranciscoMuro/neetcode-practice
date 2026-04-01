class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:   # target está a la DERECHA
                left = mid + 1         # mueve left hacia adelante
            elif nums[mid] > target:   # target está a la IZQUIERDA
                right = mid - 1        # mueve right hacia atrás
        
        return -1