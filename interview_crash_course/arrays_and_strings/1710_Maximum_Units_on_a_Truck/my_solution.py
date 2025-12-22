from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ordered = sorted(boxTypes, key=lambda boxType: boxType[1])

        num_units = 0
        while ordered and truckSize > 0:
            if ordered[-1][0] >= truckSize:
                num_units += ordered[-1][1] * truckSize
                truckSize = 0

            else:
                boxType = ordered.pop()
                num_units += boxType[1] * boxType[0]
                truckSize -= boxType[0]

        return num_units