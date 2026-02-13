class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(n) O(1)
        maxSpace = 0
        left,right=0,len(height)-1
        while left != right:
            curr = min(height[left], height[right]) * (right-left)
            if maxSpace < curr:
                maxSpace = curr
            if height[left] < height[right]:
                left +=1
            else: right -=1
        return maxSpace