class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)

        num_jewels = 0
        for stone in stones:
            if stone in jewels_set:
                num_jewels += 1

        return num_jewels