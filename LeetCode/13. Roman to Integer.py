class Solution:
    # O(n) O(1)
    def romanToInt(self, s: str) -> int:
        i2r49 = {"CM":900, "CD":400, "XC":90, "XL":40, "IX":9, "IV":4}
        i2r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        r = 0
        skip = False
        for i,c in enumerate(s):
            if skip:
                skip = False
                continue
            if i+1<len(s) and c+s[i+1] in i2r49:
                r+=i2r49[c+s[i+1]]
                skip = True
            else:
                r+=i2r[c]
        return r