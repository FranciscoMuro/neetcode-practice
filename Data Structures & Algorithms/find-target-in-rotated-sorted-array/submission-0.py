class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:  # izquierda ordenada
                if nums[left] <= target < nums[mid]:  # ¿target está aquí?
                    right = mid - 1  # busca izquierda
                else:
                    left = mid + 1   # busca derecha
            else:  # derecha ordenada
                if nums[mid] < target <= nums[right]:  # ¿target está aquí?
                    left = mid + 1   # busca derecha
                else:
                    right = mid - 1
        return -1