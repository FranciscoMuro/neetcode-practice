class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
        
#        specialCharacters = ".!?#!@#$%^&*()-+?_=,<>/'"
#        sList = list(s.replace(" ",""))
#
#        r = 0
#        l = len(sList)-1
#        print(sList)
#        while (r < len(sList)-1):
#            print(str(r)+" "+str(l))
#            if (sList[r].lower() in specialCharacters):
#                r += 1
#            if (sList[l].lower() in specialCharacters):
#                l -= 1
#            if(sList[r].lower() != sList[l].lower()):
#                return False
#            r += 1
#            l -= 1
#
#
#        return True        

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))