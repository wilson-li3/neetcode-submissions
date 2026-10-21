class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
        
        # check cols
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    seen.add(board[j][i])

        # check 3x3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] != ".":
                            if board[i+x][j+y] in seen:
                                return False
                            seen.add(board[i+x][j+y])
        
        return True

