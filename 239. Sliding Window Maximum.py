import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        res = []
        queue = collections.deque([])

        for i in range(len(nums)):
            self.push(queue, nums, i)
            if i >= k - 1:
                res.append(nums[queue[0]])
                if queue[0] == i - k + 1:
                    queue.popleft()

        return res

    def push(self, queue, nums, i):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        queue.append(i)