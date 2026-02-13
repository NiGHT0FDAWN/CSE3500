class Solution:
    def myAtoi(self, s: str) -> int:
        #O(n) O(n)
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        else: sign = 1
        d = ""
        trailing = True
        for c in s:
            if not c.isdigit():
                break
            elif c == '0' and trailing:
                continue
            else:
                d += c
                trailing = False
        if len(d) == 0:
            return 0
        d = int(d)*sign
        if d < -2147483648:
            d = -2147483648
        elif d > 2147483647:
            d = 2147483647
        return d