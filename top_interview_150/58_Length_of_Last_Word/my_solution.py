# Be mindful not to early return to adapt for string with length of 1.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        s = s.strip()
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                length += 1
            else:
                break

        return length
