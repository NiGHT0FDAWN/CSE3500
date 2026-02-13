class Solution:
    def isPalindrome(self, x: int) -> bool:
        #O(n) O(n)
        x = str(x)
        if x==x[::-1]:
            return True
        return False