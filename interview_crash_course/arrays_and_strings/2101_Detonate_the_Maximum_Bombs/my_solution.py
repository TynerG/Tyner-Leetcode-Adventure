from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def detonate(bomb: List[int]) -> int:
            nbs = bomb_graph[tuple(bomb)]
            curr_deto = 1

            for nb in nbs:
                if tuple(nb) not in detonated:
                    detonated.add(tuple(nb))
                    curr_deto += detonate(nb)

            return curr_deto

        # create a graph
        bomb_graph = defaultdict(list)
        for bomb in bombs:
            for other_bomb in bombs:
                if bomb != other_bomb:
                    dist = ((bomb[0] - other_bomb[0]) ** 2 + (bomb[1] - other_bomb[1]) ** 2) ** 0.5
                    if dist <= bomb[2]:
                        bomb_graph[tuple(bomb)].append(other_bomb)

        max_deto = 0
        for bomb in bombs:
            detonated = {tuple(bomb)}
            num_deto = detonate(bomb)
            max_deto = max(max_deto, num_deto)

        return max_deto

if __name__ == '__main__':
    s = Solution()
    print(s.maximumDetonation([[1,1,5],[10,10,5]]))