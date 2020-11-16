# Greedy O(n) O(1)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        max_pos = nums[0]
        max_steps = nums[0]

        jumps = 1
        for i in range(1, n):
            # if to reach this point
            # one needs one more jump
            if max_steps < i:
                jumps += 1
                max_steps = max_pos
            max_pos = max(max_pos, nums[i] + i)

        return jumps


# method 2: dp, record the smallest jumps to reach each number
# O(n*2), time limit exceeded
class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0
        jumps = [n for _ in range(n)]
        jumps[0] = 0  # don't forget !

        for i in range(1, n):
            for j in range(i):
                # save the smallest jump
                if j + nums[j] >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)

        return jumps[-1]