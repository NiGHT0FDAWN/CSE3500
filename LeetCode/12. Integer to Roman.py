class Solution:
    # O(1) O(1)
    def intToRoman(self, num: int) -> str:
        i2r = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        l = (1000, 500, 100, 50, 10, 5, 1)
        r = ""
        i = 0
        while num > 0:
            while num < l[i]:
                i += 1
            # print(r,l[i],num,end=' ')
            if str(num)[0] == "4":
                # print("!")
                r = r + i2r[l[i]] + i2r[l[i - 1]]
                num -= l[i - 1] - l[i]
            elif str(num)[0] == "9":
                # print("?")
                r = r + i2r[l[i + 1]] + i2r[l[i - 1]]
                num -= l[i - 1] - l[i + 1]
            else:
                # print(".")
                r = r + i2r[l[i]]
                num -= l[i]
        # print("num:", num)
        return r
