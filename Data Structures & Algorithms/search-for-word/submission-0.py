class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(r, c, i):
            # Entire word matched
            if i == len(word):
                return True

            # Invalid cell or wrong character
            if (
                r < 0 or r >= rows
                or c < 0 or c >= cols
                or board[r][c] != word[i]
            ):
                return False

            # Temporarily mark cell as visited
            char = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    board[r][c] = char
                    return True

            # Undo visited marking
            board[r][c] = char
            return False

        # The word can start from any cell
        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False