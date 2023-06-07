class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount_of_water = 0
        left = 0
        right = len(height)-1
        while left < right:
            amount_of_water = (right - left) * min(height[left],height[right])
            max_amount_of_water = max(max_amount_of_water, amount_of_water)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return max_amount_of_water