from typing import List

# issue could've checked substrings directly instead of individual chars
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            new_prefix = ""
            for i in range(min(len(s), len(prefix))):
                if prefix[i] == s[i]:
                    new_prefix += prefix[i]
                else:
                    break

            prefix = new_prefix

        return prefix