class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len_word = float("inf")
        for word in strs:
            min_len_word = min(min_len_word, len(word))
        if min_len_word == 0:
            return ""

        res = ""
        for i in range(min_len_word):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res