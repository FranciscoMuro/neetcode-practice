class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        start = 1
        res = []

        for temp in temperatures:

            for i in range (start, len(temperatures)):
                if temp < temperatures[i]:
                    count += 1
                    i = 0
                    break
                if (temp >= temperatures[i]):
                    count += 1

            if (i+1 == len(temperatures)):
                count = 0

                    

            res.append(count)
            count = 0        
            start += 1

        return res