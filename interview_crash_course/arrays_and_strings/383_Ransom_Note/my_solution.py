from collections import defaultdict

# improvement: didn't have to create the second hashmap, we can just check the letter of mag
# on the go.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransome_counts = defaultdict(int)
        for r in ransomNote:
            ransome_counts[r] += 1

        magazine_counts = defaultdict(int)
        for m in magazine:
            magazine_counts[m] += 1

        for ransome_count in ransome_counts:
            if ransome_count not in magazine_counts:
                return False

            if ransome_counts[ransome_count] > magazine_counts[ransome_count]:
                return False

        return True



