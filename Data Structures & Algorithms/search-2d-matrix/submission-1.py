class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        look_out_row = -1
        for index, row in enumerate(matrix):
            # index para saber en que row esta mi valor (posiblemente)
            if row[0] <= target <= row[-1]:
                # es aqui!!
                look_out_row = index
                break
        if look_out_row == -1:
            return False
        else:
            return self.searchValue(matrix[look_out_row], target)
        
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