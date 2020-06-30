from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(Counter(tasks).values())
        max_count = max(count)
        max_count_num = count.count(max_count)
        return max(len(tasks), (n + 1) * (max_count - 1) + max_count_num)
