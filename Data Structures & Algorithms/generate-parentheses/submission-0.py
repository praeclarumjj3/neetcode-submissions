class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings = []

        def backtrack(st, open_count, close_count):
            if len(st) == 2 * n:
                strings.append(st)
                return

            # Add "(" while we still have some available
            if open_count < n:
                backtrack(st + "(", open_count + 1, close_count)

            # Add ")" only when it can match an existing "("
            if close_count < open_count:
                backtrack(st + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return strings