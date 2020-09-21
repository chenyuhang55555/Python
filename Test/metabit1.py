class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic_last_pos = {}
        i = 0 # start
        max_len = 0
        for j in range(len(s)):
            pass
            ## if s[j] found in dic_last_pos
            if s[j] in dic_last_pos:
                i = dic_last_pos[s[j]]+1 # i <= j
                dic_last_pos[s[j]]=j
            ## if s[j] not found in dic_last_pos
            else:
                dic_last_pos[s[j]] = j
                max_len = max(max_len, j-i+1)

        return  max_len



