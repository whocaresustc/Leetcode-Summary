# Similar to 20. Valid Parentheses

# Similar to 921. Minimum Add to Make Parentheses Valid
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

        index_to_remove = index_to_remove.union(set(stack))

        for i, c in enumerate(s):
            if i not in index_to_remove:
                ans.append(c)  # don't use string concatenation here since it will be O(n + 1)

        return "".join(ans)


# Two pass O(n) O(1)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.balanceString(s, "(", ")")
        s = self.balanceString(s[::-1], ")", "(")
        return s[::-1]

    def balanceString(self, s, open_symbol, close_symbol):
        balance = 0
        ans = []
        for char in s:
            if char == open_symbol:
                balance += 1
            elif char == close_symbol:
                if balance == 0:
                    continue
                balance -= 1
            ans.append(char)
        return "".join(ans)
