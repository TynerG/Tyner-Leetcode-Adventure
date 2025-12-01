from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balon_counts = defaultdict(int)
        for c in text:
            if c in ['b', 'a', 'l', 'o', 'n']:
                balon_counts[c] += 1

        counts = [balon_counts['b'], balon_counts['a'], balon_counts['l'] // 2, balon_counts['o'] // 2,
                  balon_counts['n']]
        return min(counts)