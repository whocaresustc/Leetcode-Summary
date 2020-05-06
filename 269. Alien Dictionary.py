
# Key is building the in_degree process
from collections import defaultdict, deque, Counter


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break  # break is key, we care for first different character only

            # The last character is the same
            if c == d and len(second_word) < len(first_word):
                return ""

        output = []

        # Topological sort
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

        # there is a cycle

        return "".join(output) if len(output) == len(in_degree) else ""



