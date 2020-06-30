# DP O(n^2) O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [False for i in range(len(nums))]  # initialize to False
        ans[0] = True

        for i in range(1, len(nums)):
            for j in range(i, -1, -1):  # avoid TLE in the case[1,1,1,....1,1,1]
                if nums[j] >= (i - j) and ans[j]:
                    ans[i] = True
                    break  # if already know it is True
        return ans[len(nums) - 1]


# Greedy O(n) O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length <= 1:
            return True

        max_length = 0
        for i in range(length - 1):
            if i > max_length:  # early stop
                return False
            else:
                max_length = max(max_length, i + nums[i])
        return max_length >= length - 1