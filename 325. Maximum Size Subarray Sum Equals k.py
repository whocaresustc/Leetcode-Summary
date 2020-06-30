# range sum idea

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        ans = 0
        range_sum = {0: -1}
        acc_sum = 0
        for i, val in enumerate(nums):
            acc_sum += val
            if acc_sum not in range_sum:  # don't update because we want longest
                range_sum[acc_sum] = i

            if acc_sum - k in range_sum:
                ans = max(ans, i - range_sum[acc_sum - k])
        return ans