# Backpack + rolling pointer
# Time O(mn)
# Space O(m)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False

        # Convert into backpack 0/1 problem
        m = sum(nums)//2
        f = [[False] * (m + 1) for _ in range(2)]
        f[0][0] = True

        for i in range(1, n + 1):
            f[i%2][0] = True
            for j in range(1, m + 1):
                if j >= nums[i - 1]:
                    f[i%2][j] = f[(i - 1)%2][j] or f[(i - 1)%2][j - nums[i - 1]]
                else:
                    f[i%2][j] = f[(i - 1)%2][j]

        for i in range(n - 1, -1, -1):
            if f[i%2][m]:
                return True
        return False

# memory 1D array
# O(mn) O(m)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False

        # Convert into backpack 0/1 problem
        m = sum(nums)//2
        f = [False] * (m + 1)   # f[i]:if can form bag size i
        f[0] = True

        for item in nums:
            for j in range(m, -1, -1):
                if j >= item:
                    f[j] = f[j] or f[j - item] # for each item, choose or not

        return f[m]

# Similar to 40 combination sum
# DFS Time Space?
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        # Convert into combination sum
        return self.dfs(sorted(nums), 0, target)

    def dfs(self, candidates, index, target):
        if not target:
            return True
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                continue
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if self.dfs(candidates, i + 1,
                        target - candidates[i]):  # index update to i + 1 since each number can be used once
                return True

        return False







