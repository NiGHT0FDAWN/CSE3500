class Solution:
    def reverse(self, x: int) -> int:
        # O(log n) O(log n)
        if x//10==0:
            return x
        sign=x//abs(x)
        print(sign)
        ans = int(str(x*sign)[::-1])*sign
        if ans > -2147483648 and ans < 2147483647:
            return ans
        return 0