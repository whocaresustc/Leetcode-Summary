# Two pointers
# O(n) O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        left, right = 0, n - 1
        left_max, right_max = height[0], height[n - 1]
        ans = 0
        while left <= right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:  # move the smaller side
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1
        return ans
