class Solution:
    def reverse(self, x: int) -> int:
        #
        if x//10==0:
            return x
        sign=x//abs(x)
        ans = int(str(abs(x))[::-1])*sign
        if ans > -2e31 or ans < 2e31-1:
            return ans
        return 0

s = Solution()
print(s.reverse(1534236469))
x = 9646324351
if x > -2e31 and x < 2e31-1:
    print(x)
else: print(0)
if x > -2147483648 and x < 2147483647:
    print(x)
else: print(0)