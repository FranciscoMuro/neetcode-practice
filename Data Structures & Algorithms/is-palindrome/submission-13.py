class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimS = s.replace(" ", "").lower()
        l, r = 0, len(trimS) - 1

        while l < r:
            if not trimS[l].isalnum():
                l+=1
                continue
            elif not trimS[r].isalnum():
                r-=1
                continue
            elif trimS[l] != trimS[r]:
                return False
            l+=1
            r-=1
            

        return True
            

