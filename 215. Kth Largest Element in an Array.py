# Heapq solution 1
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


# Heapq solution 2
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for i in range(k):
            heapq.heappush(minHeap, nums[i])

        for i in range(k, len(nums)):
            heapq.heappushpop(minHeap, nums[i])

        return heapq.heappop(minHeap)


# Quickselect
class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)  # here is len(A)-k, so convert into kth smallest problem

    def partition(self, nums, start, end, k):  # this k comes from len(A)-k
        """
        During the process, it's guaranteed start <= k <= end
        """
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left, right = left + 1, right - 1

        # left is larger than right
        if k <= right:
            return self.partition(nums, start, right, k)

        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k]