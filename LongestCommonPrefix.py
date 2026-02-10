class Solution:
    def longestCommonPrefix(self, strs):
        # Edge case
        if not strs:
            return ""

        prefix = strs[0]

        for i in range(len(prefix)):
            ch = prefix[i]

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != ch:
                    return prefix[:i]

        return prefix
