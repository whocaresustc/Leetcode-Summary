# Left and Right product lists O(n) O(1)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):
            # product for the left of index 'i'
            ans[i] = nums[i - 1] * ans[i - 1]

        R = 1
        for i in reversed(range(n)):
            ans[i] = ans[i] * R
            R *= nums[i]

        return ans