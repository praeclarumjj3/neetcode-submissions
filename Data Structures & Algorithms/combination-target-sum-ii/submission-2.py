class Solution:
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(idx, combo, total):
            if total == target:
                combinations.append(combo.copy())
                return

            for i in range(idx, len(candidates)):
                # Skip duplicates at this recursion level
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                # Since candidates is sorted, later values are also too large
                if total + candidates[i] > target:
                    break

                combo.append(candidates[i])

                # i + 1 because each element can only be used once
                backtrack(i + 1, combo, total + candidates[i])

                # Undo the choice
                combo.pop()

        backtrack(0, [], 0)
        return combinations