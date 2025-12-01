class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars_appeared = set()
        left = 0
        right = 0
        max_len = 0
        while right < len(s):
            while s[right] in chars_appeared:
                chars_appeared.remove(s[left])
                left += 1

            chars_appeared.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len