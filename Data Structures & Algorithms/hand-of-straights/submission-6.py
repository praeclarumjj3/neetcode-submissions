from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for start in sorted(count):
            while count[start] > 0:
                for card in range(start, start + groupSize):
                    if count[card] == 0:
                        return False

                    count[card] -= 1

        return True