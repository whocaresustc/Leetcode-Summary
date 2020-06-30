# Classical DP
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        if not dict:
            return not s
        n = len(s)
        f = [True] + [False] * n  # f[i]: if the first i letter of word could be break or not
        maxLength = max([len(w) for w in dict])
        for i in range(1, n + 1):
            for j in range(1, min(i, maxLength) + 1):  # j: starting from i, backward j letters
                if f[i - j] and s[i - j:i] in dict:
                    f[i] = True  # once any j make f[i] become True, then break
                    break
        return f[n]

    
# Backpack DP
class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        if not dict:
            return not s
        n = len(s)
        dp = [True] + [False] * n
        for i in range(1, n + 1): #求解顺序的完全背包问题时，对物品的迭代应该放在最里层，对背包的迭代放在外层，只有这样才能让物品按一定顺序放入背包中。
            for word in dict:
                length = len(word)
                if i >= length and s[(i - length):i] == word:
                    dp[i] = dp[i] or dp[i - length]
        return dp[-1]