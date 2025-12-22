from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        seen = {start}
        queue = deque([start])

        while queue:
            node = queue.popleft()

            for jump in [arr[node], -arr[node]]:
                new_idx = node + jump

                if 0 <= new_idx < len(arr) and new_idx not in seen:
                    if arr[new_idx] == 0:
                        return True
                    seen.add(new_idx)
                    queue.append(new_idx)

        return False