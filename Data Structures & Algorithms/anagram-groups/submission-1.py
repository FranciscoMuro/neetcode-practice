class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # FIRST we can do a hash map to count the amout of letters of one type we have 
        # our key will be the count of how many letter of each will have one word like
        # act and cat have one c one a and one t 
        # thats our key and our value will be the words matching that count
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26 # a -- z 
            for c in s: # here we count each letter
                count[ord(c)-ord("a")] += 1 # we can get the value ascii of each char (c) 
                # and we can map each letter to a index a - 0, b - 1 and so on

            res[tuple(count)].append(s) # here we add the words we the same number of letters

        return list(res.values())