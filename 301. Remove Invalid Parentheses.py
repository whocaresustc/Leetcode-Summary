# O(2**N) O(N)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.ans = set()
        self.min_removed = float("inf")

        def dfs(depth, left, right, removed, cur):
            if depth == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[depth] not in ["(", ")"]:  # keep searching the next possible solution
                    dfs(depth + 1, left, right, removed, cur + s[depth])
                else:
                    dfs(depth + 1, left, right, removed + 1, cur)  # delete it
                    if s[depth] == "(":
                        dfs(depth + 1, left + 1, right, removed, cur + "(")
                    elif s[depth] == ")" and right < left:  # pruning the dfs
                        dfs(depth + 1, left, right + 1, removed, cur + ")")

        dfs(0, 0, 0, 0, "")
        return list(self.ans)


# Optimized DFS: better than O(2**N) O(N)
# Check 1249. Minimum Remove to Make Valid Parentheses

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.ans = set()
        self.min_removed = self.minAddToMakeValid(s)

        def dfs(depth, balanced, removed, cur):
            if depth == len(s):
                if balanced == 0 and removed == self.min_removed:
                    self.ans.add(cur)
            else:
                if removed <= self.min_removed:  # early pruning
                    if s[depth] not in ["(", ")"]:  # not parentheses
                        dfs(depth + 1, balanced, removed, cur + s[depth])
                    else:
                        dfs(depth + 1, balanced, removed + 1, cur)  # delete it
                        if s[depth] == "(":
                            dfs(depth + 1, balanced + 1, removed, cur + "(")  # add it
                        elif s[depth] == ")" and balanced > 0:  # pruning the dfs
                            dfs(depth + 1, balanced - 1, removed, cur + ")")  # add it

        dfs(0, 0, 0, "")
        return list(self.ans)

    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        for char in S:
            if char == "(":
                left += 1
            elif char == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1
        return left + right