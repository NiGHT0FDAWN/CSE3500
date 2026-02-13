class Solution:
    def maxArea(self, height: list[int]) -> int:
        # O(n) O(1)
        max_space = 0
        left, right = 0, len(height) - 1
        while left != right:
            curr = min(height[left], height[right]) * (right - left)
            if max_space < curr:
                max_space = curr
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_space
