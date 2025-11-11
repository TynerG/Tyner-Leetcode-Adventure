import random

# Problem: did not implement O(1) for getRandom
class RandomizedSet:

    def __init__(self):
        self.set = set()
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False

        self.set.add(val)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False

        self.set.remove(val)
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.list) - 1)

        if self.list[idx] in self.set:
            return self.list[idx]
        else:
            self.list.pop(idx)
            return self.getRandom()
