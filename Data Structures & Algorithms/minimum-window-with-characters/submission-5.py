class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        # count of the char of t
        countT = {}
        # Count of the char of s
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        #left pointer
        l = 0
        # have and need are the variables that are going to tell us if we have a
        # substring with t chars in it
        have, need = 0, len(countT)
        # res and resLen
        res = [-1,-1]
        resLen = float("infinity")
        
        # lets count into window 
        # r right pointer
        for r in range(len(s)):
            c = s[r]
            #c counting now in window
            window[c] = 1 + window.get(c,0)
            # Here we check if current char (c) is in countT (hashmap of t)
            # and  we have the same amout of this char in window
            # a = 1 in counT and a = 1 in window as an example
            if (c in countT and window[c] == countT[c]):
                have += 1
            
            # if we have the same amout of have and need
            # we start reducing the substring until we get a smaller one
            while have == need:
                 # we check the length of the current substring and check if is the smal than the last one
                if (r - l + 1) < resLen:
                    res = [l, r] # current smalest window
                    resLen = r - l + 1 # the size of the window
                
                window[s[l]] -= 1 # we count down the quantity of the char we just remove from a = 1 to a = 0
                # if we just pop one of the chars in t we reduce have 
                if (s[l] in countT and window[s[l]] < countT[s[l]]):
                    have -= 1 
                # move left 
                l += 1
            
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""