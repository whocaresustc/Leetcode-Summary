class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        return self.dfs(s, wordDict,
                        {})  # the definition of dfs: find all the the combinations for s in wordDict and store in the memo

    #
    def dfs(self, s, wordDict, memo):
        if not s:
            return

        if s in memo:
            return memo[s]
        partitions = []
        if s in wordDict:  # special case, if s in the wordDict itself
            partitions.append(s)

        for i in range(1, len(s)):  # for loop makes sure it contains all the possibilities
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            sub_partitions = self.dfs(s[i:], wordDict,
                                      memo)  # once find the first part of the sub, find the combinations for all the rest sub_partitions
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)  # append all the rest sub_partitions

        memo[s] = partitions
        return partitions