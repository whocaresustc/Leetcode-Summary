# Similar to 20. Valid Parentheses

# O(n) O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        stack = []
        ans = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if not stack:
                    index_to_remove.add(i)
                else:
                    stack.pop()

        # stack may not be empty meaning there is left parentheses remaining
        index_to_remove = index_to_remove.union(set(stack))

        for i, c in enumerate(s):
            if i not in index_to_remove:
                ans.append(c)  # don't use string concatenation here since it will be O(n + 1)

        return "".join(ans)