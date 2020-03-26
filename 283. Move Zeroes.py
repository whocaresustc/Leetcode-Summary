# O(N) O(1)
class Solution(object):
    def moveZeroes(self, nums):
        non_zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pointer], nums[i] = nums[i], nums[non_zero_pointer]
                non_zero_pointer += 1