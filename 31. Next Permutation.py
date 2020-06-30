class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # find the first descending number
            i -= 1
        if i == 0:  # nums are in descending order
            nums.reverse()
            return

        k = i - 1  # find the number that is just larger than nums[k]
        while nums[j] <= nums[k]:
            j -= 1

        # Swap
        nums[k], nums[j] = nums[j], nums[k]
        l, r = k + 1, len(nums) - 1  # reverse the second part

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1;
            r -= 1