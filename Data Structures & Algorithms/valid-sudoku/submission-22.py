class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def _count_empty(l):
            num = 0
            for a in l:
                if a == ".":
                    num += 1
            return num
        
        def _is_list_valid(row):
            n_unique = len(set(row))
            if n_unique < 9:
                num_empty = _count_empty(row)

                if num_empty > 0:
                    n_unique -= 1

                if n_unique + num_empty != 9:
                    return False
            return True

        
        for row in board:
            if not _is_list_valid(row):
                return False

    

        for idx in range(9):
            col = [board[i][idx] for i in range(9)]
            if not _is_list_valid(col):
                return False
        
        for idx in [0, 3, 6]:
            for j in [[0,1,2], [3,4,5], [6,7,8]]:
                box = []
                box.extend([board[i][s] for i in range(idx, idx+3) for s in j])
            
                if not _is_list_valid(box):
                    return False
        
        return True


