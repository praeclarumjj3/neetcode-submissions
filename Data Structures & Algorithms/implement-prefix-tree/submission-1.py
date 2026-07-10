class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        used_cols = set()
        used_diag1 = set()  # row - col
        used_diag2 = set()  # row + col

        positions = []

        def backtrack(row):
            if row == n:
                board = []

                for col in positions:
                    board.append("." * col + "Q" + "." * (n - col - 1))

                solutions.append(board)
                return

            for col in range(n):
                if (
                    col in used_cols
                    or row - col in used_diag1
                    or row + col in used_diag2
                ):
                    continue

                positions.append(col)
                used_cols.add(col)
                used_diag1.add(row - col)
                used_diag2.add(row + col)

                backtrack(row + 1)

                positions.pop()
                used_cols.remove(col)
                used_diag1.remove(row - col)
                used_diag2.remove(row + col)

        backtrack(0)
        return solutions