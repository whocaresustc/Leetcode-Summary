class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        res = None
        count = 0
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == 1:
                    res = i
        return res


from collections import defaultdict
class Solution:

    def __init__(self, nums: List[int]):
        self.store = defaultdict(list)
        for i, num in enumerate(nums):
            self.store[num].append(i)

    def pick(self, target: int) -> int:
        n = len(self.store[target])
        return self.store[target][randint(0, n - 1)]