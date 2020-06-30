
#For each letter encountered, process the last occurrence of that letter, extending the current partition [anchor, j] appropriately.
# Greedy O(N) O(1)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_positions = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last_positions[c]) # the maximum index for current partition
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1 # staring index of a new partition
        return ans