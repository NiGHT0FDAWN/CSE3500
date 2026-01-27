class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n^2) O(n)
        check = ""
        l = 0
        for c in s:
            if c in check:
                l = max(l, len(check))
                check = check[check.index(c) + 1:]
            check = check + c
        l = max(l, len(check))
        return l
