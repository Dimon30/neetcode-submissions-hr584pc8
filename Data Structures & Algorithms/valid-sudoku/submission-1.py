class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_dict = {
            ".": 0, "1": 1, "2": 2, "3": 3, "4": 4, 
            "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
        }
        # isValidRow&Col
        for i, row in enumerate(board):
            arr_row = [0] * (len(row) + 1)
            arr_col = [0] * (len(row) + 1)
            for j, el in enumerate(row):
                arr_row[num_dict[el]] += 1
                arr_col[num_dict[board[j][i]]] += 1
            for n in arr_row[1:]:
                if n > 1:
                    return False
            for n in arr_col[1:]:
                if n > 1:
                    return False
        # isValidBlock
        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                arr_block = [0] * (len(board) + 1)
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        arr_block[num_dict[board[r][c]]] += 1
                for n in arr_block[1:]:
                    if n > 1:
                        return False
        return True