# O(n) O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        m = {")":"(", "}":"{", "]":"["}
        stack = []
        for c in s:
            if c not in m:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif stack.pop() != m[c]:
                    return False
        return not stack