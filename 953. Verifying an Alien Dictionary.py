# Time O(NS) Space O(1): at most 26 characters N = len(words), S: max word len in the words

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index_order = {c: i for i, c in enumerate(order)}
        words = [[index_order[c] for c in word] for word in words]
        return all(word1 < word2 for word1, word2 in zip(words, words[1:]))



class Solution:
    def isAlienSorted(self, words, order):
        ind = {c: i for i, c in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] > ind[s2]:
                    return False
        return True



class Solution(object):
    def isAlienSorted(self, words, order):
        order_index = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Find the first difference word1[k] != word2[k].
            for k in range(min(len(word1), len(word2))):
                # If they compare badly, it's not sorted.
                if word1[k] != word2[k]:
                    if order_index[word1[k]] > order_index[word2[k]]:
                        return False
                    break
            else:
                # If we didn't find a first difference, the
                # words are like ("app", "apple").
                if len(word1) > len(word2):
                    return False

        return True
