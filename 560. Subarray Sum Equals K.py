# Check 325. Maximum Size Subarray Sum Equals k
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = defaultdict(int)
        pre_sum[0] = 1 # the continous subarrays staring from index 0
        cur_sum = 0
        ans = 0
        for num in nums:
            cur_sum += num
            ans += pre_sum[cur_sum - k]
            pre_sum[cur_sum] += 1    # store how many times the cur_sum appears
        return ans

#     def subarraySum(self, nums, k):
#         count, cur, res = {0: 1}, 0, 0
#         for v in nums:
#             cur += v
#             res += count.get(cur - k, 0)
#             count[cur] = count.get(cur, 0) + 1
#         return res