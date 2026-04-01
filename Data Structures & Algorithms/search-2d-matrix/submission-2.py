class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        look_out_row = []
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return self.searchValue(matrix[mid], target)
            elif target < matrix[mid][0]:   # target está a la DERECHA
                right = mid - 1        # mueve right hacia atrás
            elif target > matrix[mid][-1]:   # target está a la IZQUIERDA
                left = mid + 1         # mueve left hacia adelante
        return False
        
    def searchValue(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:   # target está a la DERECHA
                left = mid + 1         # mueve left hacia adelante
            elif nums[mid] > target:   # target está a la IZQUIERDA
                right = mid - 1        # mueve right hacia atrás
        return False
        


        