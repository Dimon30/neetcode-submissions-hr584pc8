class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                el = board[i][j]
                if el != ".":
                    res.append((1, el, i))
                    res.append((0, el, j))
                    res.append((10, el, (i//3, j//3)))
        return len(res) == len(set(res))

