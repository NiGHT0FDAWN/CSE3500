class Solution:
    # O(n log n) O(n)
    def longestCommonPrefix(self, strs) -> str:
        strs.sort()
        s,e=strs[0],strs[-1]
        i=0
        while i<len(s) and i<len(e) and s[i]==e[i]:
            i+=1
        return s[:i]