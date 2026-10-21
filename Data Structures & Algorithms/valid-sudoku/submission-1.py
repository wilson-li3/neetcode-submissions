class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRows = [set() for _ in range(9)]
        seenCols = [set() for _ in range(9)]
        seenBlock = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    k = (i // 3) * 3 + (j // 3)
                    if board[i][j] in seenRows[i] or board[i][j] in seenCols[j] or board[i][j] in seenBlock[k]:
                        return False
                    seenRows[i].add(board[i][j])
                    seenCols[j].add(board[i][j])
                    seenBlock[k].add(board[i][j])
        return True


