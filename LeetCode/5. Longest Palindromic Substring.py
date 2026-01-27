class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Without help: O(N^3) O(N) (absolutely horrid lol)
        """if len(s) <= 1:
            return s
        counter = {}
        ans=s[0]
        for i,c in enumerate(s):
            if c in counter:
                counter[c].append(i)
            else:
                counter[c] = [i]
        for c,i in counter.items():
            if len(i)==1:
                continue
            elif len(i)>=2:
                for _ in range(len(i)-1):
                    for __ in range(_+1,len(i)):
                        check = s[int(i[_]):int(i[__])+1]
                        if check==check[::-1]:
                            if len(check)>len(ans):
                                ans=check
        return ans"""

        # With help O(N^2) O(1)
        if len(s) <= 1 or s==s[::-1]:
            return s
        bl,br = 0,0
        for _ in range(1,len(s)):
            l=r=_
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if (r-l-2)>(br-bl):
                bl = l+1
                br = r-1
            l=_-1
            r=_
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            if (r-l-2)>(br-bl):
                bl = l+1
                br = r-1
        return s[bl:br+1]

