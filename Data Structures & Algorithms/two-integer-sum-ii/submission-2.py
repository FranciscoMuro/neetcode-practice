class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, r = 0, len(numbers)-1

        while l < r:
            sumRes = numbers[l] + numbers[r]
            print(sumRes, numbers[l], numbers[r])
            if sumRes > target:
                r-=1
            elif sumRes < target:
                l+=1
            elif sumRes == target:
                res.append(l+1)
                res.append(r+1)
                break
            
        return res