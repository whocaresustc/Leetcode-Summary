# O(n) O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "}":"{", "]":"["}
        store = []
        for char in s:
            if char not in mapping:
                store.append(char)
            else:
                if not store or store.pop() != mapping[char]: # equal and store must be empty
                    return False
        return not store # exactly matching