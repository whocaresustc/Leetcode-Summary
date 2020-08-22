from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = list(Counter(tasks).values())
        max_count = max(count)
        max_count_num = count.count(max_count)
        return max(len(tasks), (n + 1) * (max_count - 1) + max_count_num)


# Use 3A3B example
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)  # 3A3B3C3D as example