class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}

        # Build the nested dictionary
        for word in words:
            node = trie

            for char in word:
                if char not in node:
                    node[char] = {}

                node = node[char]

            node["#"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(row, col, node):
            char = board[row][col]

            if char not in node:
                return

            next_node = node[char]

            # We completed a word
            if "#" in next_node:
                result.append(next_node["#"])
                del next_node["#"]  # Prevent duplicate results

            board[row][col] = "#"  # Mark as visited

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and board[new_row][new_col] != "#"
                ):
                    dfs(new_row, new_col, next_node)

            board[row][col] = char  # Undo visited mark

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, trie)

        return result