# Check 325. Maximum Size Subarray Sum Equals k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        range_sum = {0: 1}  # for the case that start from index 0
        acc_sum = 0
        for val in nums:
            acc_sum += val
            ans += range_sum.get(acc_sum - k, 0)
            range_sum[acc_sum] = range_sum.get(acc_sum,
                                               0) + 1  # store the how many times the acc_sum appear
        return ans

#     def subarraySum(self, nums, k):
#         count, cur, res = {0: 1}, 0, 0
#         for v in nums:
#             cur += v
#             res += count.get(cur - k, 0)
#             count[cur] = count.get(cur, 0) + 1
#         return res