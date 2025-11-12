class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.strip().split()
        return " ".join(reversed(splited))