class Solution(object):
    def removeDuplicates(self, nums):
        tail = 0
        for num in nums:
            if tail < 2 or num != nums[tail - 2]:
                nums[tail] = num
                tail += 1
        return tail