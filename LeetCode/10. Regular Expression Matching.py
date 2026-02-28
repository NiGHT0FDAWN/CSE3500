# :(

"""class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        i, j = 0, 0
        print(len(s), len(p))
        while i < len(s) or j < len(p):
            print(i, j)
            if i >= len(s) and j < len(p) or i < len(s) and j >= len(p):
                return False
            if j + 1 < len(p) and (p[j + 1] == "*"):
                while i < len(s) and (p[j] == s[i] or p[j] == "."):
                    print(i)
                    i += 1
                j += 2
                continue
            if p[j] == '.' or p[j] == s[i]:
                i += 1
                j += 1
                continue

            return False
        return True

s = Solution()
s.isMatch("aaa", "a*a")"""