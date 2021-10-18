# 126. Word Ladder II

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordSet = set(wordList)  # faster checks against dictionary
        layer = {}
        layer[beginWord] = [
            [beginWord]]  # list of a list # stores current word and all possible sequences how we got to it

        while layer:
            newlayer = collections.defaultdict(list)  # returns [] on missing keys, just to simplify code
            for word in layer:  # for every word in current layer
                if word == endWord:
                    return layer[word]  # return all found sequences

                # for each word
                for i in range(len(word)):  # change every possible letter and check if it's in dictionary
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i + 1:]
                        if newWord in wordSet:
                            newlayer[newWord] += [j + [newWord] for j in layer[
                                word]]  # add new word to all sequences and form new layer element # j is a list

            wordSet -= set(newlayer.keys())  # remove from dictionary to prevent loops: acts like visited
            layer = newlayer  # move down to new layer

        return []


# 279. Perfect Squares print out all paths
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        candidates = [i ** 2 for i in range(1, int(sqrt(n)) + 2)]

        layer = defaultdict(list)
        layer[n] = [[]]
        visited = set()

        # BFS

        while layer:
            if 0 in layer:
                return layer[0]
            newlayer = defaultdict(list)

            for remaining in layer:
                for candidate in candidates:
                    if candidate <= remaining:  # and remaining - candidate not in visited:
                        # visited.add(remaining - candidate)
                        newlayer[remaining - candidate] += [node + [candidate] for node in layer[remaining]]

            layer = newlayer