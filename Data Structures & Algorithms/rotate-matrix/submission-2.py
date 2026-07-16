class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for row in range(n // 2):
            for col in range(row, n - row - 1):
                temp = matrix[row][col]

                # left -> top
                matrix[row][col] = matrix[n - 1 - col][row]

                # bottom -> left
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]

                # right -> bottom
                matrix[n - 1 - row][n - 1 - col] = matrix[col][n - 1 - row]

                # top -> right
                matrix[col][n - 1 - row] = temp