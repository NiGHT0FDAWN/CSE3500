class Solution:
    def reverse(self, x: int) -> int:
        if x//10==0:
            return x
        sign=x//abs(x)
        print(sign)
        ans = int(str(abs(x))[::-1])*sign
        if ans > -2e31 or ans < 2e31-1:
            return ans
        return 0