

    class Solution:
        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            if endWord not in wordList or not endWord or not beginWord or not wordList:
                return 0
            # all words are of the same length
            L = len(beginWord)
            all_dict = defaultdict(list)

            # preprocessing the wordList to avoid TLE
            for word in wordList:
                for i in range(L):
                    all_dict[word[:i] + "*" + word[i + 1:]].append(word)

            queue = collections.deque([(beginWord, 1)])
            visited = set([beginWord])
            while queue:
                cur_word, level = queue.popleft()
                for i in range(L):
                    inter_word = cur_word[:i] + "*" + cur_word[i + 1:]

                    for word in all_dict[inter_word]:
                        if word == endWord:
                            return level + 1
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, level + 1))
                    # all_dict[inter_word] = []

            return 0

