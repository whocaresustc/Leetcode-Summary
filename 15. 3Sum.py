# O(n**2) O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if nums[i] > 0:  # all the rest are larger than zero
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return ans

    # Two pointers
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []
            for i in range(len(nums) - 2):
                if nums[i] > 0:
                    break
                if i > 0 and nums[i] == nums[i - 1]:  # first time is OK
                    continue
                self.TwoSum(i, nums, res)
            return res

        def TwoSum(self, i, nums, res):
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    right -= 1

                elif total > 0:
                    right -= 1
                else:
                    left += 1