# Similar to 20. Valid Parentheses

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)

            else:  # c == ")"
                if not stack:
                    indexes_to_remove.add(i)
                else:
                    stack.pop()

        # stack may not be empty, so need to union
        indexes_to_remove = indexes_to_remove.union(set(stack))

        ans = ""
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                ans += c
        return ans