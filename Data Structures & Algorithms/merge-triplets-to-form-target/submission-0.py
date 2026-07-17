class Solution:
    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:
        matched = [False, False, False]

        for triplet in triplets:
            # This triplet is unusable if it exceeds target anywhere
            if any(triplet[i] > target[i] for i in range(3)):
                continue

            # Record which target coordinates this triplet can provide
            for i in range(3):
                if triplet[i] == target[i]:
                    matched[i] = True

        return all(matched)