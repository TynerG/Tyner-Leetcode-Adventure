from collections import defaultdict
from typing import List


# improvement: could populate a list of length matches * 2 that contain all the possible
# players in ascending order. Doing this can avoid from sorting at the end.
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_counts = defaultdict(int)

        for match in matches:
            lost_counts[match[0]] += 0
            lost_counts[match[1]] += 1

        winners = [[], []]
        for player in lost_counts:
            if lost_counts[player] == 0:
                winners[0].append(player)
            elif lost_counts[player] == 1:
                winners[1].append(player)

        winners[0].sort()
        winners[1].sort()

        return winners