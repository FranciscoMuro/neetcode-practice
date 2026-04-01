class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,res = 0,0,1
        subString = []
        while(l < len(s)):
            if(s[l] not in subString):
                subString.append(s[l])       
                l+=1
                print(subString)
            else:
                res = max(res, len(subString))
                subString.clear()
                r += 1
                l = r

        return 0 if len(s) == 0 else max(res, len(subString))
