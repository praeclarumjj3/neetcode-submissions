class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        combinations = []

        def backtrack(current, idx):
            if idx == len(digits):
                combinations.append("".join(current))
                return

            for letter in mapping[digits[idx]]:
                current.append(letter)
                backtrack(current, idx + 1)
                current.pop()

        backtrack([], 0)
        return combinations