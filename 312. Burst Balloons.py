# Top down DP: O(N**3) O(N**2)
class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """

    def maxCoins(self, nums):
        if not nums:
            return 0

        # [4,1,5] => [1,4,1,5,1]
        nums = [1] + nums + [1]
        return self.memo_search(nums, 0, len(nums) - 1, {})

    def memo_search(self, nums, i, j, memo): # max for nums[i+1: j-1]
        if i + 1 == j:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        best = 0
        for k in range(i + 1, j): # k is the last one to burst: nums[i, k, j]
            left = self.memo_search(nums, i, k, memo)
            right = self.memo_search(nums, k, j, memo)
            best = max(best, left + right + nums[i] * nums[k] * nums[j])

        memo[(i, j)] = best
        return best