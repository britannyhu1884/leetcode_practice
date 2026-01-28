class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(len(board))]
        columns = [[] for _ in range(len(board))]
        boxes = [[] for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in columns[j]:
                    return False
                box_index = (i // 3) * 3 + (j // 3)
                if board[i][j] in boxes[box_index]:
                    return False
                rows[i].append(board[i][j])
                columns[j].append(board[i][j])
                boxes[box_index].append(board[i][j])
        return True